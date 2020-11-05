"""
    - THIS FILE IS GENERATED -

dependencies/CDF/CoveoDistributionFramework.jid

"""

from attr import attrib, attrs
from enum import auto
from typing import Dict, List, Optional as Opt, Union
from .root import CASING, CoveoInterface, ExceptionBase, JidEnumFlag, JidType, api
from .data import DbRow
from .logger import SeverityType


@attrs(kw_only=True, auto_attribs=True)
class CDFException(ExceptionBase, hint="Coveo.Cdf.CDFException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class CDFInternalException(CDFException, hint="Coveo.Cdf.CDFInternalException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidConfigurationException(CDFException, hint="Coveo.Cdf.InvalidConfigurationException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class BladeTypeNotFoundException(CDFException, hint="Coveo.Cdf.BladeTypeNotFoundException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class CannotLoadBladeDllException(CDFException, hint="Coveo.Cdf.CannotLoadBladeDllException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class FactoryNotFoundException(CDFException, hint="Coveo.Cdf.FactoryNotFoundException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ParameterNotFoundException(CDFException, hint="Coveo.Cdf.ParameterNotFoundException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidParameterException(CDFException, hint="Coveo.Cdf.InvalidParameterException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class BladeNotReady(CDFException, hint="Coveo.Cdf.BladeNotReady"):
    def __init__(self) -> None:
        ...


class ContentType(JidEnumFlag):
    """Defines the content types that can be used for communication.

    Attributes:
        Xml: Xml content type.
        Json: Json content type.
        Binary: Binary content type.
    """

    Xml: int = auto()
    Json: int = auto()
    Binary: int = auto()


class EncodingType(JidEnumFlag):
    """Defines the encoding types used to encode messages.

    Attributes:
        None_: No encoding is used.
    """

    None_: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class Parameter(JidType, hint="Coveo.Cdf.Parameter"):
    """A structure that represents a blade parameter.

    Attributes:
        name: The name of the parameter. Used as Id.
        display_name: The name of the parameter, for display.
        type_: The value type of the parameter.
        default_value: The default value of the parameter.
        is_required: Indicates if the parameter is required.
        description: The description of the parameter.
    """

    name: Opt[str] = None
    display_name: Opt[str] = None
    type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"})
    default_value: Opt[str] = None
    is_required: Opt[bool] = None
    description: Opt[str] = None

    def __init__(
        self,
        *,
        name: Opt[str] = None,
        display_name: Opt[str] = None,
        type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"}),
        default_value: Opt[str] = None,
        is_required: Opt[bool] = None,
        description: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            name: The name of the parameter. Used as Id.
            display_name: The name of the parameter, for display.
            type_: The value type of the parameter.
            default_value: The default value of the parameter.
            is_required: Indicates if the parameter is required.
            description: The description of the parameter.
        """


@attrs(kw_only=True, auto_attribs=True)
class BladeProxy(JidType, hint="Coveo.Cdf.BladeProxy"):
    """A structure that contains information to interact with a blade.

    Attributes:
        interface: The name of the interface served by the blade proxy.
        is_optional: Indicates if this interface can be ignored.
        can_have_many: Indicates if this proxy can communicate with several blades.
        relation_name: An optional disambiguator used when matching 'ProxyInterfaceDefinitions'.
    """

    interface: Opt[str] = None
    is_optional: Opt[bool] = None
    can_have_many: Opt[bool] = None
    relation_name: Opt[str] = None

    def __init__(
        self,
        *,
        interface: Opt[str] = None,
        is_optional: Opt[bool] = None,
        can_have_many: Opt[bool] = None,
        relation_name: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            interface: The name of the interface served by the blade proxy.
            is_optional: Indicates if this interface can be ignored.
            can_have_many: Indicates if this proxy can communicate with several blades.
            relation_name: An optional disambiguator used when matching 'ProxyInterfaceDefinitions'.
        """


@attrs(kw_only=True, auto_attribs=True)
class BladeDescription(JidType, hint="Coveo.Cdf.BladeDescription"):
    """A structure that describes a blade.

    Attributes:
        type_: The type of blade to locate.
        name: The name used to identify the blade.
        description: An optional human readable description of the blade.
        parameters: The collection of parameters that can be configured when the blade is initialized.
        interfaces: The collection of all interface types served by the blade.
        proxies: The collection of all interface proxies that can be consumed by the blade.
    """

    type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"})
    name: Opt[str] = None
    description: Opt[str] = None
    parameters: Opt[List[Parameter]] = None
    interfaces: Opt[List[str]] = None
    proxies: Opt[List[BladeProxy]] = None

    def __init__(
        self,
        *,
        type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"}),
        name: Opt[str] = None,
        description: Opt[str] = None,
        parameters: Opt[List[Parameter]] = None,
        interfaces: Opt[List[str]] = None,
        proxies: Opt[List[BladeProxy]] = None,
    ) -> None:
        """

        Parameters:
            type_: The type of blade to locate.
            name: The name used to identify the blade.
            description: An optional human readable description of the blade.
            parameters: The collection of parameters that can be configured when the blade is initialized.
            interfaces: The collection of all interface types served by the blade.
            proxies: The collection of all interface proxies that can be consumed by the blade.
        """


@attrs(kw_only=True, auto_attribs=True)
class BaseConfig(DbRow, hint="Coveo.Cdf.BaseConfig"):
    """The base class used by all configuration objects."""

    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class BladeDefinitionConfig(BaseConfig, hint="Coveo.Cdf.BladeDefinitionConfig"):
    """A structure that defines the configuration of a blade.

    Attributes:
        node_id: The Id of the node hosting this blade.
        name: The name of the blade. Used as Id, unique per node.
        description: The human-readable description of the blade.
        dll_path: The path to the Dll that contains the blade. Can be relative to the node's working path.
        type_: The class type of the blade.
        init_parameters: An optional collection of parameters to use when the blade is initialized.
        is_logging_blade: Whether or not the blade is a logging blade
    """

    node_id: Opt[int] = None
    name: Opt[str] = None
    description: Opt[str] = None
    dll_path: Opt[str] = None
    type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"})
    init_parameters: Opt[Dict[str, str]] = None
    is_logging_blade: Opt[bool] = None

    def __init__(
        self,
        *,
        node_id: Opt[int] = None,
        name: Opt[str] = None,
        description: Opt[str] = None,
        dll_path: Opt[str] = None,
        type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"}),
        init_parameters: Opt[Dict[str, str]] = None,
        is_logging_blade: Opt[bool] = None,
    ) -> None:
        """

        Parameters:
            node_id: The Id of the node hosting this blade.
            name: The name of the blade. Used as Id, unique per node.
            description: The human-readable description of the blade.
            dll_path: The path to the Dll that contains the blade. Can be relative to the node's working path.
            type_: The class type of the blade.
            init_parameters: An optional collection of parameters to use when the blade is initialized.
            is_logging_blade: Whether or not the blade is a logging blade
        """


@attrs(kw_only=True, auto_attribs=True)
class NodeDefinitionConfig(DbRow, hint="Coveo.Cdf.NodeDefinitionConfig"):
    """A structure that represents a node.

    Attributes:
        name: The name of the node. Used as Id, must be unique.
        description: An optional human-readable description of the node.
        host: The hostname of the server on which this node is located.
        node_monitor_uri: The Uri of the interface that is monitoring this node.
        path: The working path of this node instance.
        server_id: The Id of the server that is publishing this interface.
        server_uri: An alternate way of specifying the server that is publishing this interface.
        force_load_dlls: An optional list of DLL paths to load before loading the blades. This can be necessary to populate the meta for interface lookup.
    """

    name: Opt[str] = None
    description: Opt[str] = None
    host: str = "localhost"
    node_monitor_uri: Opt[str] = None
    path: Opt[str] = None
    server_id: Opt[int] = None
    server_uri: Opt[str] = None
    force_load_dlls: Opt[List[str]] = None

    def __init__(
        self,
        *,
        name: Opt[str] = None,
        description: Opt[str] = None,
        host: str = "localhost",
        node_monitor_uri: Opt[str] = None,
        path: Opt[str] = None,
        server_id: Opt[int] = None,
        server_uri: Opt[str] = None,
        force_load_dlls: Opt[List[str]] = None,
    ) -> None:
        """

        Parameters:
            name: The name of the node. Used as Id, must be unique.
            description: An optional human-readable description of the node.
            host: The hostname of the server on which this node is located.
            node_monitor_uri: The Uri of the interface that is monitoring this node.
            path: The working path of this node instance.
            server_id: The Id of the server that is publishing this interface.
            server_uri: An alternate way of specifying the server that is publishing this interface.
            force_load_dlls: An optional list of DLL paths to load before loading the blades. This can be necessary to populate the meta for interface lookup.
        """


@attrs(kw_only=True, auto_attribs=True)
class NextInterceptorConfig(DbRow, hint="Coveo.Cdf.NextInterceptorConfig"):
    """A structure that represents an interceptor link. An interceptor can be used for both client and server sides and can be chained; the last interceptor would either be the message sender (client-side) or the message handler (server-side).

    Attributes:
        blade_id: The Id of the 'Interceptor' blade.
        next_interceptor_id: The Id of the next interceptor in the chain, if applicable.
    """

    blade_id: Opt[int] = None
    next_interceptor_id: Opt[int] = None

    def __init__(self, *, blade_id: Opt[int] = None, next_interceptor_id: Opt[int] = None) -> None:
        """

        Parameters:
            blade_id: The Id of the 'Interceptor' blade.
            next_interceptor_id: The Id of the next interceptor in the chain, if applicable.
        """


@attrs(kw_only=True, auto_attribs=True)
class PublicInterfaceDefinition(DbRow, hint="Coveo.Cdf.PublicInterfaceDefinition"):
    """A structure that represents the public interface of a blade.

    Attributes:
        blade_id: The Id of the blade using the interface.
        servant_name: The name of the servant.
        published_interface: The name of the interface.
        server_id: The Id of the server that is publishing the interface.
        server_uri: An alternate way of specifying the server that is publishing the interface. This Uri includes servants and served interfaces.
        server_interceptor_id: The Id of a server-side interceptor. Optional.
    """

    blade_id: Opt[int] = None
    servant_name: Opt[str] = None
    published_interface: Opt[str] = None
    server_id: Opt[int] = None
    server_uri: Opt[str] = None
    server_interceptor_id: Opt[int] = None

    def __init__(
        self,
        *,
        blade_id: Opt[int] = None,
        servant_name: Opt[str] = None,
        published_interface: Opt[str] = None,
        server_id: Opt[int] = None,
        server_uri: Opt[str] = None,
        server_interceptor_id: Opt[int] = None,
    ) -> None:
        """

        Parameters:
            blade_id: The Id of the blade using the interface.
            servant_name: The name of the servant.
            published_interface: The name of the interface.
            server_id: The Id of the server that is publishing the interface.
            server_uri: An alternate way of specifying the server that is publishing the interface. This Uri includes servants and served interfaces.
            server_interceptor_id: The Id of a server-side interceptor. Optional.
        """


@attrs(kw_only=True, auto_attribs=True)
class ProxyInterfaceDefinition(DbRow, hint="Coveo.Cdf.ProxyInterfaceDefinition"):
    """A structure that represents a proxy to the public interface of a blade.

    Attributes:
        blade_id: The Id of the blade using the proxy.
        public_interface_id: The Id of the public interface used by the proxy.
        relation_name: An optional named relation that can be used by a 'BladeProxy' to distinguish 'ProxyInterfaceDefinitions'.
        client_id: The Id of a configuration that specifies the base client arguments.
        server_uri: A Uri that specifies the server that is publishing the proxy interface. This Uri includes servants and served interfaces.
        client_interceptor_id: The Id of a client-side interceptor. Optional.
    """

    blade_id: Opt[int] = None
    public_interface_id: Opt[int] = None
    relation_name: Opt[str] = None
    client_id: Opt[int] = None
    server_uri: Opt[str] = None
    client_interceptor_id: Opt[int] = None

    def __init__(
        self,
        *,
        blade_id: Opt[int] = None,
        public_interface_id: Opt[int] = None,
        relation_name: Opt[str] = None,
        client_id: Opt[int] = None,
        server_uri: Opt[str] = None,
        client_interceptor_id: Opt[int] = None,
    ) -> None:
        """

        Parameters:
            blade_id: The Id of the blade using the proxy.
            public_interface_id: The Id of the public interface used by the proxy.
            relation_name: An optional named relation that can be used by a 'BladeProxy' to distinguish 'ProxyInterfaceDefinitions'.
            client_id: The Id of a configuration that specifies the base client arguments.
            server_uri: A Uri that specifies the server that is publishing the proxy interface. This Uri includes servants and served interfaces.
            client_interceptor_id: The Id of a client-side interceptor. Optional.
        """


class INode(CoveoInterface):
    """The INode API exposes methods to interact with a node."""

    @api("GET/is_started")
    def is_started(self) -> bool:
        """Returns whether or not this node is started."""

    @api("POST/start_all_blades")
    def start(self) -> None:
        """Starts all blades."""

    @api("POST/shutdown")
    def shutdown(self) -> None:
        """Shuts down this node completely. Remark: The INode interface will become unavailable until the node is started again on the target machine."""

    @api("POST/stop_all_blades")
    def stop(self) -> None:
        """Stops all blades."""

    @api("POST/configuration")
    def update_config(self, *, node_config: List[DbRow]) -> None:
        """Updates the configuration of this node.

        Parameters:
            node_config: The new or updated node configuration.
        """

    @api("GET/blades_description")
    def get_blades_descriptions_from_dll(self, *, dll_path: str) -> List[BladeDescription]:
        """Returns the the collection of blades contained within a Dll.

        Parameters:
            dll_path: The filename of the DLL to lookup.
        """

    @api("POST/files/{filename}")
    def notify_local_file_updated(self, *, filename: str) -> None:
        """Notifies the node that a local file has been updated.

        Parameters:
            filename: The name of the file that has been updated. The file might not exist, in the case it has been deleted as part of the update.
        """


class LogMessageSeverity(JidEnumFlag):
    """Defines all existing log entry severity types."""

    SeverityDetail: int = auto()
    SeverityNormal: int = auto()
    SeverityImportant: int = auto()
    SeverityWarning: int = auto()
    SeverityError: int = auto()
    SeverityFatal: int = auto()
    SeverityNotification: int = auto()


class CreationEventType(JidEnumFlag):
    """Defines the events that can occur on blades.

    Attributes:
        Created: A blade is created.
        Started: A blade is started.
        Stopped: A blade is stopped.
        Shutdown: A blade is shut down.
    """

    Created: int = auto()
    Started: int = auto()
    Stopped: int = auto()
    Shutdown: int = auto()


class INodeMonitor(CoveoInterface):
    """The INodeMonitor API provides methods to report node events."""

    @api("POST/blades/events")
    def report_blade_event(self, *, node_id: int, blade_id: int, event: CreationEventType) -> None:
        """Reports a blade event.

        Parameters:
            node_id: The Id of the node hosting the blade. Remark: Use 0 if unknown.
            blade_id: The Id of the blade that performed the event.
            event: The event to report.
        """

    @api("POST/nodes/events")
    def report_node_event(self, *, node_uri: str, node_id: int, event: CreationEventType) -> None:
        """Reports a node event.

        Parameters:
            node_uri: The uri of the INode interface.
            node_id: The Id of the node that performed this event. Remark: Use 0 if unknown.
            event: The event to report.
        """

    @api("POST/logs")
    def log_message(self, *, node_uri: str, node_id: int, message: str, severity: SeverityType) -> None:
        """Pushes a message to the logger.

        Parameters:
            node_uri: The uri of an INode interface.
            node_id: The Id of a node to link to this message. Remark: Use 0 if unknown.
            message: A message to push to the logger.
            severity: The severity of the log entry.
        """


class ISystemBlade(CoveoInterface):
    ...


class IServerBlade(CoveoInterface):
    ...


class IServerMessageHandler(CoveoInterface):
    ...


class IClientMessageHandler(CoveoInterface):
    ...


class IUpgradeableNode(CoveoInterface):
    """The IUpgradeableNode API exposes methods used to upgrade a node's binary files remotely."""

    @api("GET/version")
    def version(self) -> str:
        """Returns the current version of this node."""

    @api("PUT/binaries")
    def update(self, *, binaries: Union[str, bytes], command: str) -> None:
        """Updates a node with new binaries.

        Parameters:
            binaries: A zip file containing the updated binaries for this node.
            command: An optional command line to execute after deploying the binaries, but before launching the node again.
        """
