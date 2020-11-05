"""
    - THIS FILE IS GENERATED -

dependencies/CDF/Cpp/NodeManager/CDFNodeAgentDefinition.jid

"""

from attr import attrib, attrs
from datetime import datetime
from enum import auto
from typing import Dict, List, Optional as Opt, Union
from .root import CASING, CoveoInterface, JidEnumFlag, JidType, api
from .component_definition import ComponentDefinition


@attrs(kw_only=True, auto_attribs=True)
class MonitoredProcessConfig(JidType, hint="Coveo.Cdf.NodeAgent.MonitoredProcessConfig"):
    """A structure that represents the configuration of a monitored process or instance.

    Attributes:
        executable_path: The absolute path to an executable process.
        command_parameters: The command line parameters to use when launching the executable.
        path: The absolute path to the working folder. This enables instances or processes to benefit from independent data folders, if they support it.
        environment: A collection of environment variables that are set for the process exclusively.
        is_started: Indicates if the agent is actively monitoring the process or instance. When set to false, the process is dormant.
    """

    executable_path: Opt[str] = None
    command_parameters: Opt[str] = None
    path: Opt[str] = None
    environment: Opt[Dict[str, str]] = None
    is_started: Opt[bool] = None

    def __init__(
        self,
        *,
        executable_path: Opt[str] = None,
        command_parameters: Opt[str] = None,
        path: Opt[str] = None,
        environment: Opt[Dict[str, str]] = None,
        is_started: Opt[bool] = None,
    ) -> None:
        """

        Parameters:
            executable_path: The absolute path to an executable process.
            command_parameters: The command line parameters to use when launching the executable.
            path: The absolute path to the working folder. This enables instances or processes to benefit from independent data folders, if they support it.
            environment: A collection of environment variables that are set for the process exclusively.
            is_started: Indicates if the agent is actively monitoring the process or instance. When set to false, the process is dormant.
        """


@attrs(kw_only=True, auto_attribs=True)
class MonitoredProcess(JidType, hint="Coveo.Cdf.NodeAgent.MonitoredProcess"):
    """A structure that represents a generic process that can be started, stopped and monitored by this agent.

    Attributes:
        name: The name of the monitored process. Used as Id, unique per agent.
        description: The description of the monitored process.
        configuration: The monitored process's configuration.
    """

    name: Opt[str] = None
    description: Opt[str] = None
    configuration: Opt[MonitoredProcessConfig] = None

    def __init__(
        self, *, name: Opt[str] = None, description: Opt[str] = None, configuration: Opt[MonitoredProcessConfig] = None
    ) -> None:
        """

        Parameters:
            name: The name of the monitored process. Used as Id, unique per agent.
            description: The description of the monitored process.
            configuration: The monitored process's configuration.
        """


@attrs(kw_only=True, auto_attribs=True)
class Component(JidType, hint="Coveo.Cdf.NodeAgent.Component"):
    """A structure that represents a component installed on this agent.

    Attributes:
        definition: The component package definition.
        path: The path to the binary files, relative to the agent's component folder.
        deployment_params: The list of parameters that were applied when this component was installed.
    """

    definition: Opt[ComponentDefinition] = None
    path: Opt[str] = None
    deployment_params: Opt[Dict[str, str]] = None

    def __init__(
        self,
        *,
        definition: Opt[ComponentDefinition] = None,
        path: Opt[str] = None,
        deployment_params: Opt[Dict[str, str]] = None,
    ) -> None:
        """

        Parameters:
            definition: The component package definition.
            path: The path to the binary files, relative to the agent's component folder.
            deployment_params: The list of parameters that were applied when this component was installed.
        """


@attrs(kw_only=True, auto_attribs=True)
class InstanceFile(JidType, hint="Coveo.Cdf.NodeAgent.InstanceFile"):
    """A structure that represents a file deployed to an instance.

    Attributes:
        id_: The file's identifier on the manager.
        path: The file's path, relative to the instance directory.
        hash_: A hash of the file's content.
    """

    id_: Opt[str] = attrib(default=None, metadata={CASING: "Id"})
    path: Opt[str] = None
    hash_: Opt[str] = attrib(default=None, metadata={CASING: "Hash"})

    def __init__(
        self,
        *,
        id_: Opt[str] = attrib(default=None, metadata={CASING: "Id"}),
        path: Opt[str] = None,
        hash_: Opt[str] = attrib(default=None, metadata={CASING: "Hash"}),
    ) -> None:
        """

        Parameters:
            id_: The file's identifier on the manager.
            path: The file's path, relative to the instance directory.
            hash_: A hash of the file's content.
        """


@attrs(kw_only=True, auto_attribs=True)
class Instance(MonitoredProcess, hint="Coveo.Cdf.NodeAgent.Instance"):
    """A structure that represents an instance that can be started, stopped and monitored by this agent.

    Attributes:
        component_name: The name of the associated component.
        component_version: The version of the associated component.
        instance_type: The name of the instance template that was used to deploy this instance.
        deployment_params: The list of parameters that were applied when this instance was deployed.
        files: A collection of deployed files with their respective hash.
    """

    component_name: Opt[str] = None
    component_version: Opt[str] = None
    instance_type: Opt[str] = None
    deployment_params: Opt[Dict[str, str]] = None
    files: Opt[List[InstanceFile]] = None

    def __init__(
        self,
        *,
        component_name: Opt[str] = None,
        component_version: Opt[str] = None,
        instance_type: Opt[str] = None,
        deployment_params: Opt[Dict[str, str]] = None,
        files: Opt[List[InstanceFile]] = None,
    ) -> None:
        """

        Parameters:
            component_name: The name of the associated component.
            component_version: The version of the associated component.
            instance_type: The name of the instance template that was used to deploy this instance.
            deployment_params: The list of parameters that were applied when this instance was deployed.
            files: A collection of deployed files with their respective hash.
        """


@attrs(kw_only=True, auto_attribs=True)
class NodeAgentConfig(JidType, hint="Coveo.Cdf.NodeAgent.NodeAgentConfig"):
    """A structure that represents the basic configuration of an agent.

    Attributes:
        name: The name of the agent. Used as Id, unique per node manager.
        description: The description of the agent.
        uri: The URI of the agent.
        ip: The IP address of the agent.
        components_path: The absolute path to the root folder where unpacked component files are stored.
        instances_path: The absolute path to the root folder where instance data folders are created.
        reporting_period_s: The interval, in seconds, between each status report to the node manager.
        process_timeout_s: The allotted time, in seconds, for a process to complete a task (i.e.: to become responsive).
        nb_retries_on_failure: The number of times the process is restarted after failing to start, before giving up (-1 = infinite).
    """

    name: Opt[str] = None
    description: Opt[str] = None
    uri: Opt[str] = None
    ip: Opt[str] = attrib(default=None, metadata={CASING: "IP"})
    components_path: Opt[str] = None
    instances_path: Opt[str] = None
    reporting_period_s: Opt[int] = attrib(default=None, metadata={CASING: "ReportingPeriod_s"})
    process_timeout_s: Opt[int] = attrib(default=None, metadata={CASING: "ProcessTimeOut_s"})
    nb_retries_on_failure: Opt[int] = None

    def __init__(
        self,
        *,
        name: Opt[str] = None,
        description: Opt[str] = None,
        uri: Opt[str] = None,
        ip: Opt[str] = attrib(default=None, metadata={CASING: "IP"}),
        components_path: Opt[str] = None,
        instances_path: Opt[str] = None,
        reporting_period_s: Opt[int] = attrib(default=None, metadata={CASING: "ReportingPeriod_s"}),
        process_timeout_s: Opt[int] = attrib(default=None, metadata={CASING: "ProcessTimeOut_s"}),
        nb_retries_on_failure: Opt[int] = None,
    ) -> None:
        """

        Parameters:
            name: The name of the agent. Used as Id, unique per node manager.
            description: The description of the agent.
            uri: The URI of the agent.
            ip: The IP address of the agent.
            components_path: The absolute path to the root folder where unpacked component files are stored.
            instances_path: The absolute path to the root folder where instance data folders are created.
            reporting_period_s: The interval, in seconds, between each status report to the node manager.
            process_timeout_s: The allotted time, in seconds, for a process to complete a task (i.e.: to become responsive).
            nb_retries_on_failure: The number of times the process is restarted after failing to start, before giving up (-1 = infinite).
        """


@attrs(kw_only=True, auto_attribs=True)
class NodeAgentConnectionInfo(JidType, hint="Coveo.Cdf.NodeAgent.NodeAgentConnectionInfo"):
    """A structure that contains the connection information to a node manager.

    Attributes:
        node_manager_uri: The URI of a node manager.
        status_tracker_uri: The URI of a status tracker.
        blob_store_uri: The URI of the node manager's blob store.
    """

    node_manager_uri: Opt[str] = None
    status_tracker_uri: Opt[str] = None
    blob_store_uri: Opt[str] = None

    def __init__(
        self, *, node_manager_uri: Opt[str] = None, status_tracker_uri: Opt[str] = None, blob_store_uri: Opt[str] = None
    ) -> None:
        """

        Parameters:
            node_manager_uri: The URI of a node manager.
            status_tracker_uri: The URI of a status tracker.
            blob_store_uri: The URI of the node manager's blob store.
        """


@attrs(kw_only=True, auto_attribs=True)
class NodeAgentDefinition(JidType, hint="Coveo.Cdf.NodeAgent.NodeAgentDefinition"):
    """A structure that contains information relevant to the configuration and the content of an agent.

    Attributes:
        configuration: The basic configuration of the agent.
        connection_info: The connection info used to contact the node manager.
        components: A collection of installed components.
        instances: A collection of deployed instances.
        monitored_processes: A collection of monitored processes.
        platform: The platform running the agent.
        version: The build version of the agent.
    """

    configuration: Opt[NodeAgentConfig] = None
    connection_info: Opt[NodeAgentConnectionInfo] = None
    components: Opt[List[Component]] = None
    instances: Opt[List[Instance]] = None
    monitored_processes: Opt[List[MonitoredProcess]] = None
    platform: Opt[str] = None
    version: Opt[str] = None

    def __init__(
        self,
        *,
        configuration: Opt[NodeAgentConfig] = None,
        connection_info: Opt[NodeAgentConnectionInfo] = None,
        components: Opt[List[Component]] = None,
        instances: Opt[List[Instance]] = None,
        monitored_processes: Opt[List[MonitoredProcess]] = None,
        platform: Opt[str] = None,
        version: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            configuration: The basic configuration of the agent.
            connection_info: The connection info used to contact the node manager.
            components: A collection of installed components.
            instances: A collection of deployed instances.
            monitored_processes: A collection of monitored processes.
            platform: The platform running the agent.
            version: The build version of the agent.
        """


@attrs(kw_only=True, auto_attribs=True)
class NodeAgentConfigFile(JidType, hint="Coveo.Cdf.NodeAgent.NodeAgentConfigFile"):
    """A structure that represents the XML configuration file of an agent.

    Attributes:
        configuration: The configuration of the agent.
        connection_info: The connection info used to communicate with the node manager.
    """

    configuration: Opt[NodeAgentConfig] = None
    connection_info: Opt[NodeAgentConnectionInfo] = None

    def __init__(
        self, *, configuration: Opt[NodeAgentConfig] = None, connection_info: Opt[NodeAgentConnectionInfo] = None
    ) -> None:
        """

        Parameters:
            configuration: The configuration of the agent.
            connection_info: The connection info used to communicate with the node manager.
        """


@attrs(kw_only=True, auto_attribs=True)
class NodeAgentContentFile(JidType, hint="Coveo.Cdf.NodeAgent.NodeAgentContentFile"):
    """A structure that represents the XML content file of an agent.

    Attributes:
        components: The collection of installed components.
        instances: The collection of deployed instances.
        monitored_processes: The collection of monitored processes.
    """

    components: Opt[List[Component]] = None
    instances: Opt[List[Instance]] = None
    monitored_processes: Opt[List[MonitoredProcess]] = None

    def __init__(
        self,
        *,
        components: Opt[List[Component]] = None,
        instances: Opt[List[Instance]] = None,
        monitored_processes: Opt[List[MonitoredProcess]] = None,
    ) -> None:
        """

        Parameters:
            components: The collection of installed components.
            instances: The collection of deployed instances.
            monitored_processes: The collection of monitored processes.
        """


class NodeAgentStatusType(JidEnumFlag):
    """Defines agent statuses."""

    Error: int = auto()
    OK: int = auto()
    OutOfSync: int = auto()
    Unreachable: int = auto()


class MonitoredProcessStatusType(JidEnumFlag):
    """Defines monitored process statuses."""

    Unknown: int = auto()
    Stopped: int = auto()
    Running: int = auto()
    Starting: int = auto()
    Stopping: int = auto()
    UnableToStart: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class MonitoredProcessStatus(JidType, hint="Coveo.Cdf.NodeAgent.MonitoredProcessStatus"):
    """A structure that represents the status of a monitored process or instance.

    Attributes:
        status: The status of the monitored process or instance.
        last_start_stop_time: The last time the monitored process or instance was started or stopped.
        process_id: The monitored process' id.
        comment: An optional comment that may be used to detail the status.
    """

    status: Opt[MonitoredProcessStatusType] = None
    last_start_stop_time: Opt[datetime] = None
    process_id: Opt[int] = None
    comment: Opt[str] = None

    def __init__(
        self,
        *,
        status: Opt[MonitoredProcessStatusType] = None,
        last_start_stop_time: Opt[datetime] = None,
        process_id: Opt[int] = None,
        comment: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            status: The status of the monitored process or instance.
            last_start_stop_time: The last time the monitored process or instance was started or stopped.
            process_id: The monitored process' id.
            comment: An optional comment that may be used to detail the status.
        """


@attrs(kw_only=True, auto_attribs=True)
class NodeAgentStatus(JidType, hint="Coveo.Cdf.NodeAgent.NodeAgentStatus"):
    """A structure that represents the status of an agent.

    Attributes:
        status: The status of the agent.
        start_time: The last time the agent was started.
        last_configuration_update: The last update of the agent's configuration or content definition.
        comment: An optional comment that may be used to detail the status.
        monitored_processes: The collection of monitored process and instance statuses.
    """

    status: Opt[NodeAgentStatusType] = None
    start_time: Opt[datetime] = None
    last_configuration_update: Opt[datetime] = None
    comment: Opt[str] = None
    monitored_processes: Opt[Dict[str, MonitoredProcessStatus]] = None

    def __init__(
        self,
        *,
        status: Opt[NodeAgentStatusType] = None,
        start_time: Opt[datetime] = None,
        last_configuration_update: Opt[datetime] = None,
        comment: Opt[str] = None,
        monitored_processes: Opt[Dict[str, MonitoredProcessStatus]] = None,
    ) -> None:
        """

        Parameters:
            status: The status of the agent.
            start_time: The last time the agent was started.
            last_configuration_update: The last update of the agent's configuration or content definition.
            comment: An optional comment that may be used to detail the status.
            monitored_processes: The collection of monitored process and instance statuses.
        """


class INodeAgent(CoveoInterface):
    """The node agent API exposes methods to interact with this node agent."""

    @api("GET/definition")
    def get_definition(self) -> NodeAgentDefinition:
        """Returns the definition of this agent."""

    @api("GET/configuration")
    def get_config(self) -> NodeAgentConfig:
        """Returns the configuration of this agent."""

    @api("PUT/configuration")
    def set_config(self, *, configuration: NodeAgentConfig) -> None:
        """Sets the configuration of this agent.

        Parameters:
            configuration: A node agent configuration.
        """

    @api("GET/connection_info")
    def get_connection_info(self) -> NodeAgentConnectionInfo:
        """Returns the connection info of this agent."""

    @api("PUT/connection_info")
    def set_connection_info(self, *, connection_info: NodeAgentConnectionInfo) -> None:
        """Sets the connection info of this agent.

        Parameters:
            connection_info: The connection info.
        """

    @api("POST/synchronize")
    def request_synchronization(self) -> None:
        """Forces synchronization to occur now between this agent and the node manager it reports to."""

    @api("POST/components")
    def add_component(self, *, component_def: ComponentDefinition, parameters: Dict[str, str]) -> None:
        """Installs a component on this agent.

        Parameters:
            component_def: A component definition.
            parameters: A list of configuration parameters to apply before installing the component.
        """

    @api("GET/components/{component_name}/versions/{component_version}")
    def get_component(self, *, component_name: str, component_version: str) -> Component:
        """Returns information about an installed component.

        Parameters:
            component_name: The name of a component.
            component_version: The version of the component.
        """

    @api("DELETE/components/{component_name}/versions/{component_version}")
    def remove_component(self, *, component_name: str, component_version: str) -> None:
        """Uninstalls a component from this agent.

        Parameters:
            component_name: The name of a component.
            component_version: The version of the component.
        """

    @api("POST/processes")
    def add_instance(self, *, instance: Instance) -> None:
        """Deploys an instance of a component on this agent.

        Parameters:
            instance: An instance to deploy.
        """

    @api("GET/processes/{instance_name}")
    def get_instance(self, *, instance_name: str) -> Instance:
        """Returns information about a deployed instance.

        Parameters:
            instance_name: The name of an instance.
        """

    @api("PUT/processes/{instance_name}/component")
    def bind_instance_to_component(self, *, instance_name: str, component_name: str, component_version: str) -> None:
        """Binds an instance to a new component and/or version. Remark: It is not possible to switch to a different instance template - a template of the same name (i.e.: type) must exist within the definition of the target component.

        Parameters:
            instance_name: The name of an instance.
            component_name: The name of an updated component.
            component_version: The version of the updated component.
        """

    @api("POST/processes/{instance_name}/deployed_files")
    def add_file_to_instance(
        self, *, instance_name: str, file_id: str, file_path: str, contents: Union[str, bytes]
    ) -> None:
        """Pushes a file to an instance.

        Parameters:
            instance_name: The name of the instance.
            file_id: The file id as known to the NodeManager.
            file_path: Path of the file, relative to the instance folder.
            contents: The file to be added.
        """

    @api("PUT/processes/{instance_name}/deployed_files/{file_id}")
    def update_file_on_instance(
        self, *, instance_name: str, file_id: str, file_path: str, contents: Union[str, bytes]
    ) -> None:
        """Pushes a file to an instance.

        Parameters:
            instance_name: The instance to receive the file update.
            file_id: The file id as known to the NodeManager.
            file_path: The file path of the file to update, relative to the instance folder.
            contents: The new file contents.
        """

    @api("DELETE/processes/{instance_name}/deployed_files/{file_id}")
    def remove_file_from_instance(self, *, instance_name: str, file_id: str, file_path: str) -> None:
        """Removes a file from an instance.

        Parameters:
            instance_name: The name of the instance.
            file_id: The file id as known to the NodeManager.
            file_path: The file path of the file to update, relative to the instance folder.
        """

    @api("POST/processes?type=generic")
    def add_process(self, *, process: MonitoredProcess) -> None:
        """Adds a generic monitored process to this agent.

        Parameters:
            process: A monitored process.
        """

    @api("GET/processes/{process_name}?type=generi}")
    def get_process(self, *, process_name: str) -> MonitoredProcess:
        """Returns information about a monitored process.

        Parameters:
            process_name: The name of a monitored process.
        """

    @api("DELETE/processes/{process_name}")
    def remove_process(self, *, process_name: str) -> None:
        """Stops and removes a monitored process from this agent.

        Parameters:
            process_name: The name of a monitored process.
        """

    @api("POST/processes/{process_name}/start")
    def start_process(self, *, process_name: str) -> None:
        """Starts the specified instance or monitored process.

        Parameters:
            process_name: The name of an instance or monitored process.
        """

    @api("POST/processes/{process_name}/stop")
    def stop_process(self, *, process_name: str) -> None:
        """Stops the specified instance or monitored process.

        Parameters:
            process_name: The name of an instance or monitored process.
        """

    @api("POST/processes/{process_name}/stop?timeout={Timeout_s}", timeout_s="Timeout_s")
    def stop_process_ex(self, *, process_name: str, timeout_s: int) -> None:
        """Stops the specified instance or monitored process. Overrides the shutdown timeout of the process.

        Parameters:
            process_name: The name of an instance or monitored process.
            timeout_s: The maximum number of seconds before killing the process. Set to 0 to kill instantly.
        """

    @api("PUT/processes/{process_name}?type=generi}")
    def update_process(self, *, process_name: str, config: MonitoredProcessConfig) -> None:
        """Sets/updates the configuration of a monitored process.

        Parameters:
            process_name: The name of a monitored process.
            config: The new or updated configuration.
        """

    @api("GET/ports")
    def get_ports_in_use(self) -> List[int]:
        """Gets the ports in use on the agent machine."""

    @api("GET/fullstatus")
    def get_full_status(self) -> NodeAgentStatus:
        """Returns the full status of this agent."""

    @api("GET/status")
    def get_status(self) -> NodeAgentStatusType:
        """Returns the current status of this agent."""
