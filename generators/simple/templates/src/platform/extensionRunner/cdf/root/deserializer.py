import functools
from datetime import datetime
from types import FunctionType, MethodType
from typing import Type, Any, List, Dict, Union, Callable, Optional

from cdf.root.jid_type import JidTypeNotFoundException
from corepyutils.annotations import find_annotations
from corepyutils.casing import flexcase, unflex
from corepyutils.dispatch import dispatch

from .enum import JidEnumFlag
from .jid_type import JidType

TypeHint = Optional[Union[Type, Callable]]
Deserializer = Callable[..., Any]

try:
    from typing import GenericMeta
except ImportError:
    # 3.6: isinstance(type, List[str]) is False
    # 3.7: isinstance(type, List[str] is True
    # this little patch lets us support both
    GenericMeta = type(None)  # type: ignore


def deserialize(value: Any, *, hint: TypeHint = None) -> Any:
    """Deserialize objects coming from a CDF api response.
    Basic types like str, int, float, bool, (bytes?) are assumed to be already converted.

    You may omit `hint` if you have a _type. You may use `dict` and `list` as hints if the items contained
    all have a _type.
    """
    if value is None:
        return None

    if isinstance(value, dict) and '_type' in value:
        # we override the provided type annotation for two reasons:
        # 1) Service exceptions are allowed regardless of type_hint and we want to catch them all.
        # 2) It's the absolute source of truth when determining an object's kind.
        try:
            hint = JidType.get_jid_type(value['_type'])
        except JidTypeNotFoundException:
            # todo: some types (like MetaDataMap) don't follow the MapOf_ and ListOf_ naming conventions.
            value = value.copy()
            del value['_type']  # fallback to the type annotation

    return __deserialize(value, hint=hint)


__python_3_6_5_container_types = {
    List: list,
    Dict: dict,
}


@dispatch(switch_pos='hint')
def __deserialize(value: Any, *, hint: TypeHint = None) -> Any:
    """The fallback dispatch handles a limited set of generic annotation classes from the typing module:
        - Dict[]
        - List[]
        - Optional[] (note: Optional[Union[t, etc]] is not supported)
    """
    if hint is None:
        hint = type(value)

    if hasattr(hint, '__origin__'):
        container_type = hint.__origin__  # type: ignore
        # noinspection PyUnresolvedReferences
        generic_types = hint.__args__  # type: ignore

        container_type = __python_3_6_5_container_types.get(container_type, container_type)

        if container_type is Union:
            # the typical use case for Union is Optional[t]: it's translated to Union[None, t]
            if len(generic_types) == 2 and type(None) in generic_types:
                return deserialize(value, hint=next(hint for hint in generic_types if not isinstance(hint, type(None))))
            else:
                # More than one possible type; skip type hinting (notable use case: Union[None, str, bytes])
                return deserialize(value)

        elif container_type is list:
            if isinstance(value, str):
                raise ValueError("Expected list; string found.")
            item_type, = generic_types  # one-tuple unpacking
            return container_type(deserialize(item, hint=item_type) for item in value)

        elif container_type is dict:
            _, value_type = generic_types
            return {key: deserialize(value, hint=value_type) for key, value in value.items()}

        raise Exception('Unknown annotation type.')

    return value


@__deserialize.register(dict)
def _deserialize_dict(value: Dict[str, Any], *, hint: Type[dict]) -> Dict[str, Any]:
    if isinstance(hint, GenericMeta):
        # py3.6 path
        # noinspection PyUnresolvedReferences
        item_type = hint.__args__[1] if hint.__args__ else None
        try:
            return {key: deserialize(value, hint=item_type) for key, value in value.items()}
        except AttributeError:
            print("!")

    # noinspection PyArgumentList
    return hint((k, deserialize(v)) for k, v in value.items())


@__deserialize.register(list)
def _deserialize_list(value: List[Any], *, hint: Type[list]) -> List:
    if isinstance(value, str):
        raise ValueError

    if isinstance(hint, GenericMeta):
        # py3.6 path
        # noinspection PyUnresolvedReferences
        item_type = hint.__args__[0] if hint.__args__ else None
        return [deserialize(v, hint=item_type) for v in value]

    # noinspection PyArgumentList
    return hint(deserialize(v) for v in value)


@__deserialize.register(JidType)
def _deserialize_jid_type(value: Dict[str, Any], *, hint: Type[JidType]) -> JidType:
    """Most cases should be handled by the shortcircuit in _deserialize; this one handles cases where the
    service returns a correctly formatted object without a _type hint."""
    if isinstance(value, JidType):
        return value

    if hint is JidType or not issubclass(hint, JidType):
        raise TypeError(f'Unable to infer JidType: {value}')

    return flexcase(hint)(**{k: v for k, v in value.items() if v is not None})


@__deserialize.register(FunctionType)
@__deserialize.register(MethodType)
def _deserialize_from_callable(value: Dict[str, Any], *, hint: Callable) -> Dict[str, Any]:
    """Use annotations from fn to deserialize value. Extra args will be stripped out and casing is flexible."""
    assert isinstance(value, dict)
    value = unflex(hint, value)  # fix the case of keys in value
    for argument_name, annotation in find_annotations(hint).items():
        if argument_name == 'return':
            continue
        # set the deserialized value
        value[argument_name] = deserialize(value[argument_name], hint=annotation)
    return value


@__deserialize.register(datetime)
def _deserialize_datetime(value: float, *, hint: Type[datetime]) -> datetime:
    if isinstance(value, datetime):
        return value
    return hint.utcfromtimestamp(value)


# @__deserialize.register(StringEnum)
@__deserialize.register(JidEnumFlag)
def _deserialize_enum(value: str, *, hint: Type[JidEnumFlag]) -> JidEnumFlag:
    if isinstance(value, JidEnumFlag):
        return value

    if isinstance(value, list) and len(value) == 1:
        # in SOAP, these are contained within a list.
        value = value[0]

    if isinstance(value, int):
        # noinspection PyArgumentList
        return hint(value)

    value = value.replace('None', 'None_')

    if '+' in value:
        # noinspection PyArgumentList
        return functools.reduce(
            lambda x, y: x | y,
            (hint[flag] for flag in value.split('+')))

    # noinspection PyArgumentList
    try:
        return hint[value]
    except KeyError as ex:
        if value.isnumeric():
            # noinspection PyArgumentList
            return hint(int(value))
        raise ex
