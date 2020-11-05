"""
    - THIS FILE IS GENERATED -

dependencies/CDF/Cpp/LogDefinition/CoveoLogger.jid

"""

from attr import attrs
from datetime import datetime
from enum import auto
from typing import Dict, Optional as Opt
from .root import CoveoInterface, ExceptionBase, JidEnumFlag, JidType


class SeverityType(JidEnumFlag):
    """Defines log severities.

    Attributes:
        Notification: Remark: The 'Notification' severity cannot be filtered out.
    """

    Debug: int = auto()
    Detail: int = auto()
    Normal: int = auto()
    Important: int = auto()
    Warning: int = auto()
    Error: int = auto()
    Fatal: int = auto()
    Notification: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class LogEntry(JidType, hint="Coveo.LogEntry"):
    """A structure that represents a log entry.

    Attributes:
        severity: The severity.
        comment: The main comment/description/message.
        fields: A collection of fields and values that provide additional information.
        date: The creation date time
        duration: The duration
    """

    severity: SeverityType = SeverityType.Normal
    comment: Opt[str] = None
    fields: Opt[Dict[str, str]] = None
    date: Opt[datetime] = None
    duration: Opt[float] = None

    def __init__(
        self,
        *,
        severity: SeverityType = SeverityType.Normal,
        comment: Opt[str] = None,
        fields: Opt[Dict[str, str]] = None,
        date: Opt[datetime] = None,
        duration: Opt[float] = None,
    ) -> None:
        """

        Parameters:
            severity: The severity.
            comment: The main comment/description/message.
            fields: A collection of fields and values that provide additional information.
            date: The creation date time
            duration: The duration
        """


class ILog(CoveoInterface):
    """The logger API exposes methods to add, update and close log entries."""


@attrs(kw_only=True, auto_attribs=True)
class LogException(ExceptionBase, hint="Coveo.LogException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidLogEntryException(LogException, hint="Coveo.InvalidLogEntryException"):
    def __init__(self) -> None:
        ...
