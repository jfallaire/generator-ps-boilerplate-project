"""
    - THIS FILE IS GENERATED -

dependencies/CDF/Cpp/NodeManager/CDFNodeManagerDefinition.jid

"""

from attr import attrib, attrs
from datetime import datetime
from typing import Dict, List, Optional as Opt, Union
from .root import CASING, CoveoInterface, JidType, api
from .component_definition import ComponentDefinition
from .node_agent import (
    MonitoredProcess,
    MonitoredProcessConfig,
    NodeAgentConnectionInfo,
    NodeAgentDefinition,
    NodeAgentStatus,
)


@attrs(kw_only=True, auto_attribs=True)
class NodeManagerConfig(JidType, hint="Coveo.Cdf.NodeManager.NodeManagerConfig"):
    """A structure that represents the basic configuration of this node manager.

    Attributes:
        name: The name of this node manager.
        access_point_uri: The URI that should be used when Node Manager work together in a Cluster.
        status_tracker_uri: The URI of the Status Tracker.
        db_connection_string: The database connection string.
        storage_location: The blobstore location.
    """

    name: Opt[str] = None
    access_point_uri: Opt[str] = None
    status_tracker_uri: Opt[str] = None
    db_connection_string: Opt[str] = None
    storage_location: Opt[str] = None

    def __init__(
        self,
        *,
        name: Opt[str] = None,
        access_point_uri: Opt[str] = None,
        status_tracker_uri: Opt[str] = None,
        db_connection_string: Opt[str] = None,
        storage_location: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            name: The name of this node manager.
            access_point_uri: The URI that should be used when Node Manager work together in a Cluster.
            status_tracker_uri: The URI of the Status Tracker.
            db_connection_string: The database connection string.
            storage_location: The blobstore location.
        """


@attrs(kw_only=True, auto_attribs=True)
class FileToDeploy(JidType, hint="Coveo.Cdf.NodeManager.FileToDeploy"):
    """A structure that represents a file to deploy to instances.

    Attributes:
        id_: Unique id. Useful to allow 2 identical Paths for files that target different instances.
        hash_: The file's contents' hash.
        uri: Uri where the NodeManager stores the file.
        path: The file's path, relative to the instance directory. If set, this file is auto-deployed on all instances.
    """

    id_: Opt[str] = attrib(default=None, metadata={CASING: "Id"})
    hash_: Opt[str] = attrib(default=None, metadata={CASING: "Hash"})
    uri: Opt[str] = None
    path: Opt[str] = None

    def __init__(
        self,
        *,
        id_: Opt[str] = attrib(default=None, metadata={CASING: "Id"}),
        hash_: Opt[str] = attrib(default=None, metadata={CASING: "Hash"}),
        uri: Opt[str] = None,
        path: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            id_: Unique id. Useful to allow 2 identical Paths for files that target different instances.
            hash_: The file's contents' hash.
            uri: Uri where the NodeManager stores the file.
            path: The file's path, relative to the instance directory. If set, this file is auto-deployed on all instances.
        """


@attrs(kw_only=True, auto_attribs=True)
class NodeManagerDefinition(JidType, hint="Coveo.Cdf.NodeManager.NodeManagerDefinition"):
    """A structure that contains information relevant to the configuration and the content of this node manager and registered node agents.

    Attributes:
        cluster_id: The id of the node manager cluster.
        version: The 'transactional' version of this node manager. Used for concurrency control.
        configuration: The basic configuration of this node manager.
        components: The collection of available component packages.
        agents: The collection of node agents that report to this node manager.
        files: The collection of files that have been added to instances.
    """

    cluster_id: Opt[str] = None
    version: Opt[str] = None
    configuration: Opt[NodeManagerConfig] = None
    components: Opt[List[ComponentDefinition]] = None
    agents: Opt[List[NodeAgentDefinition]] = None
    files: Opt[List[FileToDeploy]] = None

    def __init__(
        self,
        *,
        cluster_id: Opt[str] = None,
        version: Opt[str] = None,
        configuration: Opt[NodeManagerConfig] = None,
        components: Opt[List[ComponentDefinition]] = None,
        agents: Opt[List[NodeAgentDefinition]] = None,
        files: Opt[List[FileToDeploy]] = None,
    ) -> None:
        """

        Parameters:
            cluster_id: The id of the node manager cluster.
            version: The 'transactional' version of this node manager. Used for concurrency control.
            configuration: The basic configuration of this node manager.
            components: The collection of available component packages.
            agents: The collection of node agents that report to this node manager.
            files: The collection of files that have been added to instances.
        """


@attrs(kw_only=True, auto_attribs=True)
class AgentStatus(JidType, hint="Coveo.Cdf.NodeManager.AgentStatus"):
    """A structure that contains information about the status of a node agent.

    Attributes:
        last_contact: The last time communication was established between the node agent and this node manager.
        node_agent: The status of the node agent which includes its monitored processes and instances.
    """

    last_contact: Opt[datetime] = None
    node_agent: Opt[NodeAgentStatus] = None

    def __init__(self, *, last_contact: Opt[datetime] = None, node_agent: Opt[NodeAgentStatus] = None) -> None:
        """

        Parameters:
            last_contact: The last time communication was established between the node agent and this node manager.
            node_agent: The status of the node agent which includes its monitored processes and instances.
        """


@attrs(kw_only=True, auto_attribs=True)
class ServedCall(JidType, hint="Coveo.Cdf.NodeManager.ServedCall"):
    """A structure that describes a call being served.

    Attributes:
        method_args: The method name + the call arguments
        time_started: The time the call was dispatched.
    """

    method_args: Opt[str] = None
    time_started: Opt[datetime] = None

    def __init__(self, *, method_args: Opt[str] = None, time_started: Opt[datetime] = None) -> None:
        """

        Parameters:
            method_args: The method name + the call arguments
            time_started: The time the call was dispatched.
        """


@attrs(kw_only=True, auto_attribs=True)
class UriCacheStatus(JidType, hint="Coveo.Cdf.NodeManager.UriCacheStatus"):
    """A structure that describes the agent uri cache.

    Attributes:
        nb_entries: The number of entries in the cache.
        nb_hits: The number of times the agent name was found.
        nb_misses: The number of times the agent name was not found.
    """

    nb_entries: Opt[int] = None
    nb_hits: Opt[int] = None
    nb_misses: Opt[int] = None

    def __init__(self, *, nb_entries: Opt[int] = None, nb_hits: Opt[int] = None, nb_misses: Opt[int] = None) -> None:
        """

        Parameters:
            nb_entries: The number of entries in the cache.
            nb_hits: The number of times the agent name was found.
            nb_misses: The number of times the agent name was not found.
        """


@attrs(kw_only=True, auto_attribs=True)
class NodeManagerStatus(JidType, hint="Coveo.Cdf.NodeManager.NodeManagerStatus"):
    """A structure that contains information about the status of this node manager.

    Attributes:
        start_time: The last time when this manager was launched.
        last_configuration_update: The last update of this 'NodeManagerDefinition'.
        comment: An optional comment that may be used to detail the status.
        agents: A collection of 'AgentStatus' structures which detail the state of each node agent and their associated entities.
        config_lock_info: Info about the configuration lock.
        served_calls: Info about the calls being served.
        uri_cache_status: Info about the agent uri cache.
    """

    start_time: Opt[datetime] = None
    last_configuration_update: Opt[datetime] = None
    comment: Opt[str] = None
    agents: Opt[Dict[str, AgentStatus]] = None
    config_lock_info: Opt[str] = None
    served_calls: Opt[List[ServedCall]] = None
    uri_cache_status: Opt[UriCacheStatus] = None

    def __init__(
        self,
        *,
        start_time: Opt[datetime] = None,
        last_configuration_update: Opt[datetime] = None,
        comment: Opt[str] = None,
        agents: Opt[Dict[str, AgentStatus]] = None,
        config_lock_info: Opt[str] = None,
        served_calls: Opt[List[ServedCall]] = None,
        uri_cache_status: Opt[UriCacheStatus] = None,
    ) -> None:
        """

        Parameters:
            start_time: The last time when this manager was launched.
            last_configuration_update: The last update of this 'NodeManagerDefinition'.
            comment: An optional comment that may be used to detail the status.
            agents: A collection of 'AgentStatus' structures which detail the state of each node agent and their associated entities.
            config_lock_info: Info about the configuration lock.
            served_calls: Info about the calls being served.
            uri_cache_status: Info about the agent uri cache.
        """


@attrs(kw_only=True, auto_attribs=True)
class NodeManagerSnapshot(JidType, hint="Coveo.Cdf.NodeManager.NodeManagerSnapshot"):
    """A structure that a node manager snapshot.

    Attributes:
        configuration: The configuration.
        agents: The list of agents.
        components: The list of components.
        files: The list of files to deploy.
        status: The current status.
    """

    configuration: Opt[NodeManagerConfig] = None
    agents: Opt[List[NodeAgentDefinition]] = None
    components: Opt[List[ComponentDefinition]] = None
    files: Opt[List[FileToDeploy]] = None
    status: Opt[NodeManagerStatus] = None

    def __init__(
        self,
        *,
        configuration: Opt[NodeManagerConfig] = None,
        agents: Opt[List[NodeAgentDefinition]] = None,
        components: Opt[List[ComponentDefinition]] = None,
        files: Opt[List[FileToDeploy]] = None,
        status: Opt[NodeManagerStatus] = None,
    ) -> None:
        """

        Parameters:
            configuration: The configuration.
            agents: The list of agents.
            components: The list of components.
            files: The list of files to deploy.
            status: The current status.
        """


class INodeManager(CoveoInterface):
    """The node manager API exposes methods to interact with this node manager and registered node agents. It provides a focal point of administration for all nodes, components and instances."""

    @api("GET/configuration")
    def get_config(self) -> NodeManagerConfig:
        """Returns the basic configuration of this node manager."""

    @api("PUT/configuration")
    def set_config(self, *, configuration: NodeManagerConfig) -> None:
        """Sets/updates the basic configuration of this node manager.

        Parameters:
            configuration: A node manager configuration.
        """

    @api("GET/status")
    def get_status(self) -> NodeManagerStatus:
        """Get status of the node manager."""

    @api("GET/snapshot")
    def get_snapshot(self) -> NodeManagerSnapshot:
        """Get a snapshot of the current state."""

    @api("GET/readiness")
    def get_readiness(self) -> str:
        """Used by Kubernetes readiness probe to test the state of the pod."""

    @api("POST/packages")
    def add_component_package(self, *, package: Union[str, bytes]) -> None:
        """Adds a component package to the blob store so it can be deployed to node agents.

        Parameters:
            package: A component package.
        """

    @api("POST/packages?from_uri")
    def add_component_package_from_uri(self, *, uri: str) -> None:
        """Adds a component package to the blob store so it can be deployed to node agents.

        Parameters:
            uri: A URI to locate the component package. The node manager must be able to access this location using its current login credentials.
        """

    @api("POST/packages?from_definition")
    def add_component_package_definition(self, *, package: ComponentDefinition) -> None:
        """Adds a component package definition so it can be deployed to node agents.

        Parameters:
            package: A component package definition.
        """

    @api("PUT/packages/{package_name}/versions/{package_version}/platforms/{package_platform}")
    def update_component_package_location(
        self, *, package_name: str, package_version: str, package_platform: str, location: str
    ) -> None:
        """Updates a component package location.

        Parameters:
            package_name: The name of a component.
            package_version: The version of the component.
            package_platform: The platform of the component.
            location: The new location of the package in the blobstore.
        """

    @api("GET/packages")
    def get_component_packages_list(self) -> List[ComponentDefinition]:
        """Returns the list of all component packages contained in the blob store."""

    @api("GET/packages?latest=true")
    def get_latest_component_packages_list(self) -> List[ComponentDefinition]:
        """Returns the list of latest component packages contained in the blob store."""

    @api("GET/packaged/{package_name}/versions/{package_version}")
    def get_component_packages_definition(
        self, *, package_name: str, package_version: str, package_platform: str
    ) -> ComponentDefinition:
        """Returns the definition of the requested component packages.

        Parameters:
            package_name: The name of a component.
            package_version: The version of the component.
            package_platform: The platform of the component.
        """

    @api("DELETE/packages/{package_name}/versions/{package_version}")
    def remove_component_package(self, *, package_name: str, package_version: str, package_platform: str) -> None:
        """Removes a component package from the blob store. Does not actually remove the package from node agents (see 'UninstallComponent').

        Parameters:
            package_name: The name of a component.
            package_version: The version of the component.
            package_platform: The platform of the component.
        """

    @api("POST/agents")
    def add_agent(self, *, agent_uri: str) -> None:
        """Registers a node agent to report to this node manager.

        Parameters:
            agent_uri: The URI of a node agent.
        """

    @api("GET/agents/{agent_name}")
    def get_agent(self, *, agent_name: str) -> NodeAgentDefinition:
        """Returns the complete definition of a node agent.

        Parameters:
            agent_name: The name of a node agent.
        """

    @api("GET/agents/{agent_name}?except_component}")
    def get_agent_except_components(self, *, agent_name: str) -> NodeAgentDefinition:
        """Returns the complete definition of a node agent.

        Parameters:
            agent_name: The name of a node agent.
        """

    @api("POST/agents/{agent_name}/synchronize")
    def synchronize_agent(self, *, agent_name: str) -> None:
        """Forces synchronization to occur now between this node manager and a node agent.

        Parameters:
            agent_name: The name of a node agent.
        """

    @api("DELETE/agents/{agent_name}")
    def remove_agent(self, *, agent_name: str) -> None:
        """De-registers a node agent from this node manager. The node agent will remain fully operational and independent, but will no longer report to this node manager.

        Parameters:
            agent_name: The name of a node agent.
        """

    @api("GET/agents")
    def get_agent_list(self) -> List[NodeAgentDefinition]:
        """Returns a list of all node agents contained in this node manager's definition."""

    @api("GET/agent_names")
    def get_agents_list(self) -> List[str]:
        """Returns a list of the names of all node agents contained in this node manager's definition."""

    @api("GET/agents/{agent_name}/status")
    def get_agent_status(self, *, agent_name: str) -> NodeAgentStatus:
        """Returns the full status of this agent.

        Parameters:
            agent_name: The name of a node agent.
        """

    @api("PUT/agents")
    def set_agent_definition(self, *, agent_definition: NodeAgentDefinition) -> NodeAgentConnectionInfo:
        """Sets/updates the definition of a node agent.

        Parameters:
            agent_definition: A node agent definition.
        """

    @api("DELETE/agents/{agent_name}/definition")
    def reset_agent_definition(self, *, agent_name: str) -> None:
        """Resets/clears the definition of a node agent.

        Parameters:
            agent_name: The name of a node agent.
        """

    @api("POST/agents/{agent_name}/components")
    def install_component(
        self, *, agent_name: str, package_name: str, package_version: str, params: Dict[str, str]
    ) -> None:
        """Instructs a node agent to download a package in order to install it as a component.

        Parameters:
            agent_name: The name of a node agent.
            package_name: The name of a component package.
            package_version: The version of the component package.
            params: A list of configuration parameters to apply before installing the component package.
        """

    @api("DELETE/agents/{agent_name}/components/{component_name}/versions/{component_version}")
    def uninstall_component(self, *, agent_name: str, component_name: str, component_version: str) -> None:
        """Uninstalls a component from a node agent.

        Parameters:
            agent_name: The name of a node agent.
            component_name: The name of a component.
            component_version: The version of the component.
        """

    @api("POST/agents/{agent_name}/processes")
    def add_instance(
        self,
        *,
        agent_name: str,
        component_name: str,
        component_version: str,
        instance_type: str,
        instance_name: str,
        instance_decription: str,
        params: Dict[str, str],
    ) -> None:
        """Creates an instance of a component on a node agent. The component must already exist on the node agent (see 'InstallComponent').

        Parameters:
            agent_name: The name of a node agent.
            component_name: The name of an installed component.
            component_version: The version of the component.
            instance_type: The name (i.e.: type) of the instance template to use.
            instance_name: The name to give to this instance. Used as Id, unique per node agent.
            instance_decription: An optional description for this instance.
            params: A list of configuration parameters to apply when deploying the instance.
        """

    @api("PUT/agents/{agent_name}/processes/{instance_name}/component")
    def bind_instance_to_component(
        self, *, agent_name: str, instance_name: str, component_name: str, component_version: str
    ) -> None:
        """Binds an instance to a new component and/or version. It is not possible to switch to a different instance template - a template of the same name (i.e.: type) must exist within the definition of the target component.

        Parameters:
            agent_name: The name of a node agent.
            instance_name: The name of an instance.
            component_name: The name of a component.
            component_version: The version of the component.
        """

    @api("GET/deployable_files/{file_id}")
    def get_file_content(self, *, file_id: str) -> Union[str, bytes]:
        """Gets the content of a file to deploy.

        Parameters:
            file_id: The file id.
        """

    @api("GET/deployable_files")
    def get_files_to_deploy(self) -> List[FileToDeploy]:
        """Gets the list of files to deploy."""

    @api("POST/deployable_files")
    def add_file_to_deploy(self, *, file_id: str, contents: Union[str, bytes]) -> FileToDeploy:
        """Registers a file on the manager.

        Parameters:
            file_id: Unique file id.
            contents: The content of the file.
        """

    @api("PUT/deployable_files/{file_id}")
    def update_file_to_deploy(self, *, file_id: str, contents: Union[str, bytes]) -> FileToDeploy:
        """Updates a file on the manager and all instances it's deployed on.

        Parameters:
            file_id: The file id.
            contents: The new file contents.
        """

    @api("DELETE/deployable_files/{file_id}")
    def remove_file_to_deploy(self, *, file_id: str) -> FileToDeploy:
        """Removes a registered file from the manager.

        Parameters:
            file_id: The file id.
        """

    @api("POST/agents/{agent_name}/processes/{instance_name}/deployed_files")
    def add_file_to_instance(self, *, agent_name: str, instance_name: str, file_id: str, file_path: str) -> None:
        """Pushes a file to an instance.

        Parameters:
            agent_name: The name of a node agent.
            instance_name: The name of the instance.
            file_id: The id of the file to deploy.
            file_path: The path where the file will be stored, relative to the instance directory.
        """

    @api("DELETE/agents/{agent_name}/processes/{instance_name}/deployed_files/{file_id}")
    def remove_file_from_instance(self, *, agent_name: str, instance_name: str, file_id: str, file_path: str) -> None:
        """Removes a file from an instance.

        Parameters:
            agent_name: The name of a node agent.
            instance_name: The name of the instance.
            file_id: The id of the file to remove.
            file_path: The path where the file will be stored, relative to the instance directory.
        """

    @api("POST/agents/{agent_name}/processes?type=generic")
    def add_monitored_process(self, *, agent_name: str, process: MonitoredProcess) -> None:
        """Adds a generic monitored process to a node agent.

        Parameters:
            agent_name: The name of a node agent.
            process: A monitored process definition.
        """

    @api("DELETE/agents/{agent_name}/processes/{process_name}")
    def remove_process(self, *, agent_name: str, process_name: str) -> None:
        """Removes a generic monitored process from a node agent.

        Parameters:
            agent_name: The name of a node agent.
            process_name: The name of a monitored process.
        """

    @api("POST/agents/{agent_name}/processes/{process_name}/start")
    def start_process(self, *, agent_name: str, process_name: str) -> None:
        """Starts/launches an instance or monitored process.

        Parameters:
            agent_name: The name of a node agent.
            process_name: The name of a monitored process or instance.
        """

    @api("POST/agents/{agent_name}/processes/{process_name}/stop")
    def stop_process(self, *, agent_name: str, process_name: str) -> None:
        """Stops an instance or monitored process.

        Parameters:
            agent_name: The name of a node agent.
            process_name: The name of a monitored process or instance.
        """

    @api("POST/agents/{agent_name}/processes/{process_name}/stop?timeout={Timeout_s}", timeout_s="Timeout_s")
    def stop_process_ex(self, *, agent_name: str, process_name: str, timeout_s: int) -> None:
        """Stops the specified instance or monitored process. Overrides the shutdown timeout of the process.

        Parameters:
            agent_name: The name of a node agent.
            process_name: The name of a monitored process or instance.
            timeout_s: The maximum number of seconds before killing the process. Set to 0 to kill instantly.
        """

    @api("PUT/agents/{agent_name}/processes/{process_name}?type=generi}")
    def update_monitored_process(self, *, agent_name: str, process_name: str, config: MonitoredProcessConfig) -> None:
        """Sets/updates the configuration of a monitored process.

        Parameters:
            agent_name: The name of a node agent.
            process_name: The name of a monitored process.
            config: A monitored process configuration.
        """

    @api("GET/agents/{agent_name}/ports")
    def get_ports_in_use(self, *, agent_name: str) -> List[int]:
        """Gets the ports in use on the agent machine.

        Parameters:
            agent_name: The name of a node agent.
        """
