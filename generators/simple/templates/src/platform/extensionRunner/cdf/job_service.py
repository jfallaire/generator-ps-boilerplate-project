"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/CoveoJobService.jid

"""

from attr import attrib, attrs
from enum import auto
from typing import Dict, Optional as Opt
from .root import CASING, CoveoInterface, JidEnumFlag, JidType, api
from .config_definition import Parameter


class JobStatus(JidEnumFlag):
    """Possible status of the Jobs.

    Attributes:
        Ready: The Job is still pending for execution.
        Running: The Job is currently running.
        Done: The Job is completed.
        Error: The Job failed to be executed.
        Interrupted: A resumable Job was interrupted.
    """

    Ready: int = auto()
    Running: int = auto()
    Done: int = auto()
    Error: int = auto()
    Interrupted: int = auto()


class JobPriority(JidEnumFlag):
    """Priority level associated to a job."""

    Highest: int = auto()
    High: int = auto()
    Normal: int = auto()
    Low: int = auto()
    Lowest: int = auto()


class JobInterrupt(JidEnumFlag):
    """Possible interruptions that can be received after a heatbeat.

    Attributes:
        Continue: Continue current operation
        Stop: Stop
        Pause: Pause
        Dump: Dump
    """

    Continue: int = auto()
    Stop: int = auto()
    Pause: int = auto()
    Dump: int = auto()


class JobHandlerType(JidEnumFlag):
    """Possible interruptions that can be received after a heatbeat.

    Attributes:
        Clustered: Hosted in the cloud cluster
        Dedicated: Hosted in a dedicated loud instance
        OnPremises: hosted on-premises
        ClusteredTask: Hosted in the cloud cluster in task mode
    """

    Clustered: int = auto()
    Dedicated: int = auto()
    OnPremises: int = auto()
    ClusteredTask: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class JobHandlerInformation(JidType, hint="Coveo.JobService.JobHandlerInformation"):
    """Job Handler Information. Contains informations on the physical machine the handler is running on.

    Attributes:
        name: The instance name of the Job Handler.
        host_name: The name of the host machine the job handler is running on.
        assembly_version: The version of the Job Handler's dlls.
    """

    name: Opt[str] = None
    host_name: Opt[str] = None
    assembly_version: Opt[str] = None

    def __init__(self, *, name: Opt[str] = None, host_name: Opt[str] = None, assembly_version: Opt[str] = None) -> None:
        """

        Parameters:
            name: The instance name of the Job Handler.
            host_name: The name of the host machine the job handler is running on.
            assembly_version: The version of the Job Handler's dlls.
        """


@attrs(kw_only=True, auto_attribs=True)
class JobHeartbeat(JidType, hint="Coveo.JobService.JobHeartbeat"):
    """A structure that represents a Job Heartbeat.

    Attributes:
        job_handler_information: Informations about the Job Handler currently running the job.
        status: The status of the job.
        metrics: Job metrics collected by the job handler.
    """

    job_handler_information: Opt[JobHandlerInformation] = None
    status: Opt[JobStatus] = None
    metrics: Opt[Dict[str, str]] = None

    def __init__(
        self,
        *,
        job_handler_information: Opt[JobHandlerInformation] = None,
        status: Opt[JobStatus] = None,
        metrics: Opt[Dict[str, str]] = None,
    ) -> None:
        """

        Parameters:
            job_handler_information: Informations about the Job Handler currently running the job.
            status: The status of the job.
            metrics: Job metrics collected by the job handler.
        """


@attrs(kw_only=True, auto_attribs=True)
class JobHandlerConfig(JidType, hint="Coveo.JobService.JobHandlerConfig"):
    """Job Handler Configuration

    Attributes:
        organization_id: The organization Id that this Job Handler is dedicated to, if any.
        instance_id: The instance Id that this Job Handler is dedicated to, if any.
        service_uri: The Uri of the service the Job Handler must use.
        node_agent_uri: The Uri of the Node Agent used to create crawler instances.
        node_agent_blob_store_uri: The Uri of the BlobStore set on the Node Agent to download packages.
        node_manager_uri: The Uri of the Node Manager used to update packages.
        api_key: The API Key used to authenticate to the service.
        polling_interval: Interval, in seconds, at which the handler polls for a pending job to execute.
        heartbeat_interval: Interval, in seconds, at which the handler reports status of a job being executed.
        parameters: Additionnal Parameters
    """

    organization_id: Opt[str] = None
    instance_id: Opt[str] = None
    service_uri: Opt[str] = None
    node_agent_uri: Opt[str] = None
    node_agent_blob_store_uri: Opt[str] = None
    node_manager_uri: Opt[str] = None
    api_key: Opt[str] = attrib(default=None, metadata={CASING: "APIKey"})
    polling_interval: int = 5
    heartbeat_interval: int = 30
    parameters: Opt[Dict[str, Parameter]] = None

    def __init__(
        self,
        *,
        organization_id: Opt[str] = None,
        instance_id: Opt[str] = None,
        service_uri: Opt[str] = None,
        node_agent_uri: Opt[str] = None,
        node_agent_blob_store_uri: Opt[str] = None,
        node_manager_uri: Opt[str] = None,
        api_key: Opt[str] = attrib(default=None, metadata={CASING: "APIKey"}),
        polling_interval: int = 5,
        heartbeat_interval: int = 30,
        parameters: Opt[Dict[str, Parameter]] = None,
    ) -> None:
        """

        Parameters:
            organization_id: The organization Id that this Job Handler is dedicated to, if any.
            instance_id: The instance Id that this Job Handler is dedicated to, if any.
            service_uri: The Uri of the service the Job Handler must use.
            node_agent_uri: The Uri of the Node Agent used to create crawler instances.
            node_agent_blob_store_uri: The Uri of the BlobStore set on the Node Agent to download packages.
            node_manager_uri: The Uri of the Node Manager used to update packages.
            api_key: The API Key used to authenticate to the service.
            polling_interval: Interval, in seconds, at which the handler polls for a pending job to execute.
            heartbeat_interval: Interval, in seconds, at which the handler reports status of a job being executed.
            parameters: Additionnal Parameters
        """


class IJobHandler(CoveoInterface):
    @api("GET/config")
    def get_config(self) -> JobHandlerConfig:
        ...

    @api("PUT/config")
    def set_config(self, *, config: JobHandlerConfig) -> None:
        ...
