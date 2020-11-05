"""
    - THIS FILE IS GENERATED -

dependencies/CMF.Net/Cmf/Tracking/CoveoTracking.jid

"""

from attr import attrib, attrs
from datetime import datetime
from enum import auto
from typing import Any, List, Optional as Opt
from .root import CASING, CoveoInterface, ExceptionBase, JidEnumFlag, JidType, api
from .data import DataTuple, DbRowState


@attrs(kw_only=True, auto_attribs=True)
class TrackingException(ExceptionBase, hint="Coveo.Tracking.TrackingException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidStatusEntryException(TrackingException, hint="Coveo.Tracking.InvalidStatusEntryException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class Feedback(JidType, hint="Coveo.Tracking.Feedback"):
    """A structure that represents a feedback indirectly given from a status follower/subscriber to the status producer.

    Attributes:
        ts: The feedback's timestamp.
        input_: The feedback.
    """

    ts: Opt[datetime] = None
    input_: Opt[str] = attrib(default=None, metadata={CASING: "Input"})

    def __init__(
        self, *, ts: Opt[datetime] = None, input_: Opt[str] = attrib(default=None, metadata={CASING: "Input"})
    ) -> None:
        """

        Parameters:
            ts: The feedback's timestamp.
            input_: The feedback.
        """


@attrs(kw_only=True, auto_attribs=True)
class FeedbackPair(JidType, hint="Coveo.Tracking.FeedbackPair"):
    """A structure that represents a [int, Feedback] pair."""

    index: Opt[int] = None
    feedback: Opt[Feedback] = None

    def __init__(self, *, index: Opt[int] = None, feedback: Opt[Feedback] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class TimedEntry(JidType, hint="Coveo.Tracking.TimedEntry"):
    """A structure that represents a timed entry.

    Attributes:
        ts: The timestamp. The integral component is the number of seconds since epoch. The fractional part represents the sub-second fraction.
    """

    ts: Opt[datetime] = None

    def __init__(self, *, ts: Opt[datetime] = None) -> None:
        """

        Parameters:
            ts: The timestamp. The integral component is the number of seconds since epoch. The fractional part represents the sub-second fraction.
        """


@attrs(kw_only=True, auto_attribs=True)
class MetricEntry(TimedEntry, hint="Coveo.Tracking.MetricEntry"):
    """A structure that represents a metric entry."""

    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class StatusEntry(TimedEntry, hint="Coveo.Tracking.StatusEntry"):
    """A structure that represents a status entry.

    Attributes:
        id_: The status entry unique id (will be assigned if not given).
        parent_id: Optional parent id.
        row_state: The status change (Added/Updated/Deleted).
        name: Human-readable name for the status. Ex: Id :proc-234, Name: MirrorManager.
        revocation_ts: After that timestamp, auto-delete the status.
        feedback: This is used to queue requests/feedback for the entity sending the statuses. Something like Cancel/Suspend/Resume, but could be anything understood by the sender.
        any_status: Fit any status in here.
    """

    id_: Opt[str] = attrib(default=None, metadata={CASING: "Id"})
    parent_id: Opt[str] = None
    row_state: Opt[DbRowState] = None
    name: Opt[str] = None
    revocation_ts: Opt[datetime] = None
    feedback: Opt[Feedback] = None
    any_status: Opt[str] = None

    def __init__(
        self,
        *,
        id_: Opt[str] = attrib(default=None, metadata={CASING: "Id"}),
        parent_id: Opt[str] = None,
        row_state: Opt[DbRowState] = None,
        name: Opt[str] = None,
        revocation_ts: Opt[datetime] = None,
        feedback: Opt[Feedback] = None,
        any_status: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            id_: The status entry unique id (will be assigned if not given).
            parent_id: Optional parent id.
            row_state: The status change (Added/Updated/Deleted).
            name: Human-readable name for the status. Ex: Id :proc-234, Name: MirrorManager.
            revocation_ts: After that timestamp, auto-delete the status.
            feedback: This is used to queue requests/feedback for the entity sending the statuses. Something like Cancel/Suspend/Resume, but could be anything understood by the sender.
            any_status: Fit any status in here.
        """


class CallStatus(JidEnumFlag):
    """Defines calls statuses.

    Attributes:
        Killed: Defines a cancelled call.
    """

    NotStarted: int = auto()
    InProgress: int = auto()
    Done: int = auto()
    Killed: int = auto()
    Suspended: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class CallProgress(StatusEntry, hint="Coveo.Tracking.CallProgress"):
    """A structure that represents a call status.

    Attributes:
        call_status: The status of the call.
        percent: The progress percentage.
        reply: The reply as json/xml. Will be set when the Status turns to Done and all went well.
        exception: The reply exception as json/xml. Will be set when the Status turns to Done but an exception was thrown, or to Killed (the call was cancelled).
    """

    call_status: Opt[CallStatus] = None
    percent: Opt[int] = None
    reply: Opt[str] = None
    exception: Opt[str] = None

    def __init__(
        self,
        *,
        call_status: Opt[CallStatus] = None,
        percent: Opt[int] = None,
        reply: Opt[str] = None,
        exception: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            call_status: The status of the call.
            percent: The progress percentage.
            reply: The reply as json/xml. Will be set when the Status turns to Done and all went well.
            exception: The reply exception as json/xml. Will be set when the Status turns to Done but an exception was thrown, or to Killed (the call was cancelled).
        """


class IMetricsTracker(CoveoInterface):
    """The MetricsTracker API exposes methods to add and query metric entries."""

    @api("PUT/metrics")
    def add_metric(self, *, metric: DataTuple) -> None:
        """Adds a metric entry.

        Parameters:
            metric: The MetricEntry.
        """

    @api("PUT/metrics?batch")
    def add_metrics(self, *, metrics: List[DataTuple]) -> None:
        """Adds multiple metric entries.

        Parameters:
            metrics: The Metric Entries.
        """

    @api("GET/metrics/{type}", type_="Type")
    def get_metrics(self, *, type_: str) -> List[DataTuple]:
        """Gets all status entries of a given type.

        Parameters:
            type_: The MetricEntry type.
        """

    @api("GET/metrics/{type}?query={query}", type_="Type")
    def query_metrics(self, *, type_: str, query: str) -> List[DataTuple]:
        """Executes a query directly on the underlying storage.

        Parameters:
            type_: The MetricEntry type.
            query: The query.
        """

    @api("GET/metrics/{type}?cmd={command}", type_="Type")
    def run_command_on_metrics(self, *, type_: str, command: str) -> List[DataTuple]:
        """Run an arbitrary command directly on the underlying storage.

        Parameters:
            type_: The MetricEntry type.
            command: The command.
        """


class IStatusTracker(CoveoInterface):
    """The StatusTracker API exposes methods to add/query status entries."""

    @api("PUT/statuses")
    def set_status(self, *, status_entry: DataTuple) -> Feedback:
        """Adds/Updates/Deletes a status entry.

        Parameters:
            status_entry: The StatusEntry.
        """

    @api("PUT/statuses?batch")
    def set_statuses(self, *, status_entries: List[DataTuple]) -> List[FeedbackPair]:
        """Adds/Updates/Deletes status entries.

        Parameters:
            status_entries: The StatusEntry's.
        """

    @api("PUT/statuses?type={Type}", type_="Type")
    def set_statuses_for_type(self, *, type_: str, status_entries: List[DataTuple]) -> List[FeedbackPair]:
        """Adds/Updates/Deletes status entries. Automatically computes the delta.

        Parameters:
            type_: The type to overwrite.
            status_entries: The StatusEntry's.
        """

    @api("GET/statuses/{type}/{id}", type_="Type", id_="Id")
    def get_status(self, *, type_: str, id_: str) -> DataTuple:
        """Gets a status entry.

        Parameters:
            type_: The StatusEntry type.
            id_: The Id to look for.
        """

    @api("GET/statuses/{type}", type_="Type")
    def get_statuses(self, *, type_: str) -> List[DataTuple]:
        """Gets all status entries.

        Parameters:
            type_: The StatusEntry type.
        """

    @api("PUT/statuses/{id}", type_="Type", id_="Id")
    def set_status_feedback(self, *, type_: str, id_: str, feedback: str) -> None:
        """Sets the Feedback field of a status entry.

        Parameters:
            type_: The StatusEntry type.
            id_: The Id to look for.
            feedback: The feedback to set.
        """

    @api("GET/statuses/{type}?query={query}", type_="Type")
    def query_statuses(self, *, type_: str, query: str) -> List[DataTuple]:
        """Executes a query directly on the underlying storage.

        Parameters:
            type_: The StatusEntry type.
            query: The query.
        """

    @api("GET/statuses/{type}?cmd={command}", type_="Type")
    def run_command_on_statuses(self, *, type_: str, command: str) -> List[DataTuple]:
        """Run an arbitrary command directly on the underlying storage.

        Parameters:
            type_: The StatusEntry type.
            command: The command.
        """


@attrs(kw_only=True, auto_attribs=True)
class Metric(JidType, hint="Coveo.Tracking.Metric"):
    name: Opt[str] = None
    value: Opt[Any] = None

    def __init__(self, *, name: Opt[str] = None, value: Opt[Any] = None) -> None:
        ...


class IMetricAggregator(CoveoInterface):
    ...
