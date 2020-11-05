"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/CoveoDocumentTracker.jid

"""

from attr import attrib, attrs
from datetime import datetime
from enum import auto
from typing import Any, Dict, Optional as Opt
from .root import CASING, CoveoInterface, JidEnumFlag, JidType, api


class TaskType(JidEnumFlag):
    Streaming: int = auto()
    Consuming: int = auto()
    Crawling: int = auto()
    Processing: int = auto()
    Mapping: int = auto()
    Extension: int = auto()
    Indexing: int = auto()
    Detection: int = auto()


class OperationType(JidEnumFlag):
    Add: int = auto()
    Delete: int = auto()
    AddByReference: int = auto()


class ResultType(JidEnumFlag):
    Completed: int = auto()
    Warning: int = auto()
    Rejected: int = auto()
    Error: int = auto()
    Skipped: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class TrackingInformation(JidType, hint="Coveo.DocumentTracker.TrackingInformation"):
    uri: Opt[str] = attrib(default=None, metadata={CASING: "URI"})
    organization_id: Opt[str] = None
    source_id: Opt[str] = None
    request_id: Opt[str] = None
    date_time: Opt[datetime] = None
    task: Opt[TaskType] = None
    operation: Opt[OperationType] = None
    result: Opt[ResultType] = None
    meta: Opt[Dict[str, Any]] = None
    resource_id: Opt[str] = None

    def __init__(
        self,
        *,
        uri: Opt[str] = attrib(default=None, metadata={CASING: "URI"}),
        organization_id: Opt[str] = None,
        source_id: Opt[str] = None,
        request_id: Opt[str] = None,
        date_time: Opt[datetime] = None,
        task: Opt[TaskType] = None,
        operation: Opt[OperationType] = None,
        result: Opt[ResultType] = None,
        meta: Opt[Dict[str, Any]] = None,
        resource_id: Opt[str] = None,
    ) -> None:
        ...


class IDocumentTracker(CoveoInterface):
    @api("POST/add")
    def add(self, *, information: TrackingInformation) -> None:
        ...
