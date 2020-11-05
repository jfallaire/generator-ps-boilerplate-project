"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/ProviderJobService.jid

"""

from attr import attrs
from datetime import datetime
from enum import auto
from typing import List, Optional as Opt
from .root import CoveoInterface, JidEnumFlag, JidType, api
from .security_provider import SID, SecurityProviderConfig
from .security import SecurityCacheOperationStatus
from .job_service import JobHandlerType, JobHeartbeat, JobInterrupt, JobPriority


@attrs(kw_only=True, auto_attribs=True)
class ExpansionOptions(JidType, hint="Coveo.ProviderJobService.ExpansionOptions"):
    """

    Attributes:
        expand_members_and_mappings: Whether to expand identities members and mappings.
        expand_well_known_groups: Whether to expand identities well known groups.
    """

    expand_members_and_mappings: bool = True
    expand_well_known_groups: bool = True

    def __init__(self, *, expand_members_and_mappings: bool = True, expand_well_known_groups: bool = True) -> None:
        """

        Parameters:
            expand_members_and_mappings: Whether to expand identities members and mappings.
            expand_well_known_groups: Whether to expand identities well known groups.
        """


class ExpansionScope(JidEnumFlag):
    """The scope of entities to expand for a security provider.

    Attributes:
        Single: A specific entity
        All: All entities of the security provider
        InError: Entities in error
        NotUpdated: Entities that have never been updated
    """

    Single: int = auto()
    All: int = auto()
    InError: int = auto()
    NotUpdated: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class SecurityProviderJob(JidType, hint="Coveo.ProviderJobService.SecurityProviderJob"):
    """A structure that represents a security provider expansion job.

    Attributes:
        organization_id: Organization Identifier.
        instance_id: The id of the security provider instance.
        instance_type: The type of security provider to run this job on.
        instance_version: The package version of the security provider.
        operation_id: The operation id associated to this job.
        config: The security provider configuration.
        identities: The identities to expand.
        expansion_result_uri: Uri of the service where expansion results must be reported.
        expansion_options: Options for the expansion job.
        expansion_scope: Scope of the expansion job.
        max_last_expansion_date: Max update date of entities to expand.
        min_last_expansion_date: Min update date of entities to expand.
    """

    organization_id: Opt[str] = None
    instance_id: Opt[str] = None
    instance_type: Opt[str] = None
    instance_version: Opt[str] = None
    operation_id: Opt[str] = None
    config: Opt[SecurityProviderConfig] = None
    identities: Opt[List[SID]] = None
    expansion_result_uri: Opt[str] = None
    expansion_options: Opt[ExpansionOptions] = None
    expansion_scope: Opt[ExpansionScope] = None
    max_last_expansion_date: Opt[datetime] = None
    min_last_expansion_date: Opt[datetime] = None

    def __init__(
        self,
        *,
        organization_id: Opt[str] = None,
        instance_id: Opt[str] = None,
        instance_type: Opt[str] = None,
        instance_version: Opt[str] = None,
        operation_id: Opt[str] = None,
        config: Opt[SecurityProviderConfig] = None,
        identities: Opt[List[SID]] = None,
        expansion_result_uri: Opt[str] = None,
        expansion_options: Opt[ExpansionOptions] = None,
        expansion_scope: Opt[ExpansionScope] = None,
        max_last_expansion_date: Opt[datetime] = None,
        min_last_expansion_date: Opt[datetime] = None,
    ) -> None:
        """

        Parameters:
            organization_id: Organization Identifier.
            instance_id: The id of the security provider instance.
            instance_type: The type of security provider to run this job on.
            instance_version: The package version of the security provider.
            operation_id: The operation id associated to this job.
            config: The security provider configuration.
            identities: The identities to expand.
            expansion_result_uri: Uri of the service where expansion results must be reported.
            expansion_options: Options for the expansion job.
            expansion_scope: Scope of the expansion job.
            max_last_expansion_date: Max update date of entities to expand.
            min_last_expansion_date: Min update date of entities to expand.
        """


@attrs(kw_only=True, auto_attribs=True)
class ProviderJobHeartbeat(JobHeartbeat, hint="Coveo.ProviderJobService.ProviderJobHeartbeat"):
    """A structure that represents a security provider job Heartbeat.

    Attributes:
        operation_status: The status of the expansion operation.
    """

    operation_status: Opt[SecurityCacheOperationStatus] = None

    def __init__(self, *, operation_status: Opt[SecurityCacheOperationStatus] = None) -> None:
        """

        Parameters:
            operation_status: The status of the expansion operation.
        """


@attrs(kw_only=True, auto_attribs=True)
class GetProviderJobModel(SecurityProviderJob, hint="Coveo.ProviderJobService.GetProviderJobModel"):
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
    @api("POST/v1/organizations/{organization_id}/providers/{instance_id}/jobs", id_="Id")
    def add_job(
        self,
        *,
        organization_id: str,
        instance_id: str,
        job: SecurityProviderJob,
        priority: JobPriority,
        handler_type: JobHandlerType,
        id_: str,
    ) -> None:
        """Adds a security provider job

        Parameters:
            id_: The job unique Identifier.
        """


class IJobConsumer(CoveoInterface):
    @api("GET/v1/providers/jobs")
    def get_job(self) -> GetProviderJobModel:
        """Retrieves a pending job for any job handler, if there is any."""

    @api("GET/v1/organizations/{organization_id}/providers/jobs")
    def get_organization_job(self, *, organization_id: str) -> GetProviderJobModel:
        """Retrieves a pending job for a job handler dedicated to a specific organization, if any."""

    @api("GET/v1/organizations/{organization_id}/providers/{instance_id}/jobs")
    def get_dedicated_job(self, *, organization_id: str, instance_id: str) -> GetProviderJobModel:
        """Retrieves a pending job for a job handler dedicated to a specific security provider instance, if any."""

    @api("POST/v1/organizations/{organization_id}/providers/{instance_id}/jobs/{job_id}/status")
    def report_status(
        self, *, organization_id: str, instance_id: str, job_id: str, heartbeat: ProviderJobHeartbeat
    ) -> JobInterrupt:
        """Send the status of the job currently being executed.

        Parameters:
            heartbeat: The status of the job.
        """
