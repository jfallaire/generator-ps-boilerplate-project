import json
from datetime import datetime, date
from functools import singledispatch
from typing import Any, Dict, List, Union

from .jid_type import JidType, ExceptionBase
from .enum import JidEnumFlag


class JidEncoder(json.JSONEncoder):
    """A JSON encoder class that uses serialize() for everything."""
    def default(self, obj: Any) -> Any:
        return serialize(obj)


@singledispatch
def serialize(obj: Any) -> Any:
    """Serialize an object."""
    return obj


@serialize.register(dict)
def _serialize_dict(obj: dict) -> Dict[str, Any]:
    return {serialize(k): serialize(v) for k, v in obj.items() if v is not None}


@serialize.register(list)
def _serialize_list(obj: list) -> List:
    assert not isinstance(obj, str)
    return [serialize(i) for i in obj if i is not None]


@serialize.register(JidType)
@serialize.register(ExceptionBase)
@serialize.register(Exception)
def _serialize_jid_type(obj: Union[JidType, ExceptionBase, Exception]) -> Dict[str, Any]:
    """CDFException is a JidType+Exception, we handle both to eliminate any ambiguity."""
    if isinstance(obj, JidType):
        return serialize(obj.as_dict())  # type: ignore
    assert isinstance(obj, Exception)
    return serialize(ExceptionBase.from_exception(obj))  # type: ignore


@serialize.register(JidEnumFlag)
def _serialize_enum(obj: JidEnumFlag) -> str:
    return str(obj)


@serialize.register(datetime)
def _serialize_datetime(obj: datetime) -> int:
    return int((obj - datetime(1970, 1, 1, tzinfo=obj.tzinfo)).total_seconds())


@serialize.register(date)
def _serialize_date(obj: date) -> int:
    return int((obj - date(1970, 1, 1)).total_seconds())


@serialize.register(bytes)
def _serialize_bytes(obj: bytes) -> str:
    return obj.decode()
