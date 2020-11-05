from abc import ABCMeta, abstractmethod
from typing import ClassVar, Dict, Type, Optional, Any, TypeVar, Tuple, Iterator, Mapping, Callable

import attr
from inflection import camelize

from corepyutils.itertools import filter_keys
from corepyutils.annotations import find_annotations


CASING = 'CASING'

T = TypeVar('T', bound='JidType')


class _JidTypeCache:
    def __init__(self, cls: Type['JidType']):
        # find_annotations() will find the class variables/etc as well.
        # clean it by removing anything that attr doesn't know.
        self.fields: Dict[str, Type] = dict(filter_keys(source=find_annotations(cls, globals()),
                                                        keys={field.name for field in attr.fields(cls)}))
        # create snake_case -> CamelCase lookup.
        self.from_snake: Dict[str, str] = {field.name: field.metadata.get(CASING, camelize(field.name))
                                           for field in attr.fields(cls)}


class JidTypeNotFoundException(Exception):
    ...


class JidTypeInterface(metaclass=ABCMeta):
    @abstractmethod
    def as_dict(self) -> Dict[str, Any]:
        """Since dataclasses.asdict() isn't customizable, we need to provide our own."""

    @classmethod
    @abstractmethod
    def get_jid_type(cls, jid_type_hint: str) -> Type['JidTypeInterface']:
        """Returns the correct jid type. (jid_type_hint = _type)"""


@attr.s
class JidType(JidTypeInterface):
    """Base class for generated data classes."""
    __namespace: ClassVar[Dict[str, Type['JidType']]] = {}
    __type: ClassVar[str]
    __cache_storage: ClassVar[Optional[_JidTypeCache]]
    __deserializer: ClassVar[Optional[Callable[..., Any]]] = None

    # noinspection PyMethodOverriding
    def __init_subclass__(cls, hint: str, **kwargs: Any) -> None:
        """Register the current class into the namespace."""
        assert not kwargs
        cls.__type = hint  # each subclass gets its own __type.
        cls.__cache_storage = None
        cls.__register_subclass(hint, cls)

    def __setattr__(self, key: str, value: Any) -> None:
        """JIT-deserializer"""
        try:
            super().__setattr__(key, self.__deserialize(self.__cache.fields[key], value))
        except KeyError:
            if hasattr(self, key):
                raise  # the key should work; not supposed to happen.
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute {key}") from None

    @property
    def __cache(self) -> _JidTypeCache:
        return self.__get_cache()

    def as_dict(self) -> Dict[str, Any]:
        """Since dataclasses.asdict() isn't customizable, we need to provide our own."""
        to_translate = ((field_name, getattr(self, field_name)) for field_name in self.__cache.fields)
        return dict(self.__translate(to_translate, lookup=self.__cache.from_snake), _type=self.__type)

    @classmethod
    def get_jid_type(cls, jid_type_hint: str) -> Type['JidType']:
        """Returns the correct jid type. (jid_type_hint = _type)"""
        try:
            return cls.__namespace[jid_type_hint]
        except KeyError:
            raise JidTypeNotFoundException(jid_type_hint)

    def __deserialize(self, type_: Type, value: Any) -> Any:
        """Break the circular import cycle. :shame: """
        cls = self.__class__
        if cls.__deserializer is None:
            from .deserializer import deserialize
            cls.__deserializer = deserialize
        assert cls.__deserializer is not None
        return cls.__deserializer(value, hint=type_)  # using self.__deserializer() here will break things

    @classmethod
    def __register_subclass(cls, hint: str, klass: Type) -> None:
        """Register a class into the namespace."""
        assert hint not in cls.__namespace
        cls.__namespace[hint] = klass

    @classmethod
    def __get_cache(cls) -> _JidTypeCache:
        if cls.__cache_storage is None:
            cls.__cache_storage = _JidTypeCache(cls)
        assert cls.__cache_storage is not None
        return cls.__cache_storage

    @staticmethod
    def __translate(kvps: Iterator[Tuple[str, Any]], lookup: Mapping[str, str]) -> Iterator[Tuple[str, Any]]:
        """Iterate kvps but substitute the key for the one in lookup. Strips out _type."""
        yield from ((lookup.get(key, key), value) for key, value in kvps if key != '_type')


@attr.s(auto_attribs=True, kw_only=True)
class ExceptionBase(JidType, Exception, hint='ExceptionBase'):
    """Wraps exceptions thrown by CDF; hint is fake."""
    what: Optional[str] = None
    name: Optional[str] = None
    inner: Optional[Exception] = None  # only exists for the duration of __init__

    # noinspection PyUnusedLocal
    def __init__(self, *, what: str = None, name: str = None, inner: Exception = None):  # type: ignore
        ...

    def __attrs_post_init__(self) -> None:
        self.what = self.what or (str(self.inner) if self.inner else 'No Exception message was available.')
        super(Exception, self).__init__(self.what)
        if self.inner:
            super(Exception, self).__setattr__('__cause__', self.inner)
        self.inner = None  # hide the callstack from JidType.as_dict()

    @classmethod
    def from_exception(cls, exception: Exception) -> 'ExceptionBase':
        """return an instance of CDFException out of any exception"""
        exception_message = str(exception).strip('"').strip("'")
        return cls(what=exception_message, name=exception.__class__.__name__, inner=exception)

    def __str__(self) -> str:
        return self.what or super().__str__()


