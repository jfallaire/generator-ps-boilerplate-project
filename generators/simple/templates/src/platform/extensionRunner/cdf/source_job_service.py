"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/SourceJobService.jid

"""

from attr import attrs
from enum import auto
from typing import Dict, Optional as Opt
from .root import CoveoInterface, JidEnumFlag, JidType, api
from .job_service import JobHandlerInformation, JobHandlerType, JobInterrupt, JobPriority, JobStatus
from .crawler import Config, RefreshStatus


class SourceJobOperationType(JidEnumFlag):
    """Possible operation types in source jobs.

    Attributes:
        Rebuild: Rebuild
        Full_Refresh: Full Refresh
        Incremental_Refresh: Incremental Refresh
        Source_Resume: Resume a paused refresh
        Delete_Source: Deletes persistent crawling data associated with a source
    """

    Rebuild: int = auto()
    Full_Refresh: int = auto()
    Incremental_Refresh: int = auto()
    Source_Resume: int = auto()
    Delete_Source: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class SourceJobHeartbeat(JidType, hint="Coveo.SourceJobService.SourceJobHeartbeat"):
    """A structure that represents a source job Heartbeat.

    Attributes:
        job_handler_information: Informations about the Job Handler currently running the job.
        organization_id: Organization Identifier.
        instance_id: The id of the source instance.
        operation_id: The Operation Id currently running on the job handler.
        refresh_status: The refresh status of the crawler running the source job.
        status: The status of the Source Job that was retrieved by the job handler.
        metrics: Job metrics collected by the job handler.
        error_details: Additionnal details if an error occurred.
    """

    job_handler_information: Opt[JobHandlerInformation] = None
    organization_id: Opt[str] = None
    instance_id: Opt[str] = None
    operation_id: Opt[str] = None
    refresh_status: Opt[RefreshStatus] = None
    status: Opt[JobStatus] = None
    metrics: Opt[Dict[str, str]] = None
    error_details: Opt[str] = None

    def __init__(
        self,
        *,
        job_handler_information: Opt[JobHandlerInformation] = None,
        organization_id: Opt[str] = None,
        instance_id: Opt[str] = None,
        operation_id: Opt[str] = None,
        refresh_status: Opt[RefreshStatus] = None,
        status: Opt[JobStatus] = None,
        metrics: Opt[Dict[str, str]] = None,
        error_details: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            job_handler_information: Informations about the Job Handler currently running the job.
            organization_id: Organization Identifier.
            instance_id: The id of the source instance.
            operation_id: The Operation Id currently running on the job handler.
            refresh_status: The refresh status of the crawler running the source job.
            status: The status of the Source Job that was retrieved by the job handler.
            metrics: Job metrics collected by the job handler.
            error_details: Additionnal details if an error occurred.
        """


@attrs(kw_only=True, auto_attribs=True)
class SourceJob(JidType, hint="Coveo.SourceJobService.SourceJob"):
    """A structure that represents a source job.

    Attributes:
        organization_id: Organization Identifier.
        instance_id: The id of the source instance.
        instance_type: The type of instance to run this job on.
        instance_version: The package version of the instance.
        operation_id: The operation id.
        config: The source configuration.
        source_id: The source identifier.
        operation_type: The operation type.
    """

    organization_id: Opt[str] = None
    instance_id: Opt[str] = None
    instance_type: Opt[str] = None
    instance_version: Opt[str] = None
    operation_id: Opt[str] = None
    config: Opt[Config] = None
    source_id: Opt[str] = None
    operation_type: Opt[SourceJobOperationType] = None

    def __init__(
        self,
        *,
        organization_id: Opt[str] = None,
        instance_id: Opt[str] = None,
        instance_type: Opt[str] = None,
        instance_version: Opt[str] = None,
        operation_id: Opt[str] = None,
        config: Opt[Config] = None,
        source_id: Opt[str] = None,
        operation_type: Opt[SourceJobOperationType] = None,
    ) -> None:
        """

        Parameters:
            organization_id: Organization Identifier.
            instance_id: The id of the source instance.
            instance_type: The type of instance to run this job on.
            instance_version: The package version of the instance.
            operation_id: The operation id.
            config: The source configuration.
            source_id: The source identifier.
            operation_type: The operation type.
        """


@attrs(kw_only=True, auto_attribs=True)
class GetSourceJobModel(SourceJob, hint="Coveo.SourceJobService.GetSourceJobModel"):
    """

    Attributes:
        job_id: The job unique Identifier.
        execution_timeout: The timespan in seconds before this job expires unless the Job Handler reports status.
    """

    job_id: Opt[str] = None
    execution_timeout: Opt[int] = None

    def __init__(self, *, job_id: Opt[str] = None, execution_timeout: Opt[int] = None) -> None:
        """

        Parameters:
            job_id: The job unique Identifier.
            execution_timeout: The timespan in seconds before this job expires unless the Job Handler reports status.
        """


class IJobProducer(CoveoInterface):
    @api("POST/v1/organizations/{organization_id}/sources/{instance_id}/jobs", id_="Id")
    def add_job(
        self,
        *,
        organization_id: str,
        instance_id: str,
        job: SourceJob,
        priority: JobPriority,
        handler_type: JobHandlerType,
        id_: str,
    ) -> None:
        """Adds a source job

        Parameters:
            id_: The job unique Identifier.
        """

    @api("POST/v1/organizations/{organization_id}/sources/{instance_id}/jobs/{job_id}/interrupt/{interrupt}")
    def interrupt_job(self, *, organization_id: str, instance_id: str, job_id: str, interrupt: JobInterrupt) -> None:
        """Interrupts a source job

        Parameters:
            interrupt: The type of job interrupt.
        """


class IJobConsumer(CoveoInterface):
    @api("GET/v1/sources/jobs")
    def get_job(self) -> GetSourceJobModel:
        """Retrieves a pending job for any job handler, if there is any."""

    @api("GET/v1/organizations/{organization_id}/sources/jobs")
    def get_organization_job(self, *, organization_id: str) -> GetSourceJobModel:
        """Retrieves a pending job for a job handler dedicated to a specific organization, if any."""

    @api("GET/v1/organizations/{organization_id}/sources/{instance_id}/jobs")
    def get_dedicated_job(self, *, organization_id: str, instance_id: str) -> GetSourceJobModel:
        """Retrieves a pending job for a job handler dedicated to a specific security provider instance, if any."""

    @api("POST/v1/organizations/{organization_id}/sources/{instance_id}/jobs/{job_id}/status")
    def report_status(
        self, *, organization_id: str, instance_id: str, job_id: str, heartbeat: SourceJobHeartbeat
    ) -> JobInterrupt:
        """Send the status of the job currently being executed."""
