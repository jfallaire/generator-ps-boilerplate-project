"""
    - THIS FILE IS GENERATED -

dependencies/CDF/CDFComponentDefinition.jid

"""

from attr import attrs
from typing import Dict, List, Optional as Opt
from .root import JidType


@attrs(kw_only=True, auto_attribs=True)
class Parameter(JidType, hint="Coveo.Cdf.Component.Parameter"):
    """A structure that represents a configuration parameter.

    Attributes:
        name: The name of the parameter, for display.
        default_value: The default value of the parameter.
        tag: The tag used to identify the parameter within the files. In the files, each tag must be enclosed in double-percent signs (e.g.: %%myTag%%).
    """

    name: Opt[str] = None
    default_value: Opt[str] = None
    tag: Opt[str] = None

    def __init__(self, *, name: Opt[str] = None, default_value: Opt[str] = None, tag: Opt[str] = None) -> None:
        """

        Parameters:
            name: The name of the parameter, for display.
            default_value: The default value of the parameter.
            tag: The tag used to identify the parameter within the files. In the files, each tag must be enclosed in double-percent signs (e.g.: %%myTag%%).
        """


@attrs(kw_only=True, auto_attribs=True)
class ParametersDefinition(JidType, hint="Coveo.Cdf.Component.ParametersDefinition"):
    """A structure that represents configuration parameters and the text files in which they appear.

    Attributes:
        files: A list of text files to search for parameter tags.
        parameters: The list of configuration parameters to apply.
    """

    files: Opt[List[str]] = None
    parameters: Opt[List[Parameter]] = None

    def __init__(self, *, files: Opt[List[str]] = None, parameters: Opt[List[Parameter]] = None) -> None:
        """

        Parameters:
            files: A list of text files to search for parameter tags.
            parameters: The list of configuration parameters to apply.
        """


@attrs(kw_only=True, auto_attribs=True)
class InstanceDefinition(JidType, hint="Coveo.Cdf.Component.InstanceDefinition"):
    """A structure that represents an instance template.

    Attributes:
        type_name: The name of the instance template. Used as Id, unique per component.
        description: The description of the instance template.
        package_file_name: The filename of the instance package to use within the component package.
        install_command: A command to execute each time an instance of this type is created on an agent.
        uninstall_command: A command to execute each time an instance of this type is removed from an agent.
        parameters_definition: A list of configuration parameters.
        executable_path: The command to execute. Path must be relative to the root of the archive.
        command_parameters: The command line parameters to use when launching the executable.
        is_node_process: Indicates if the instance is a 'Node Process'.
    """

    type_name: Opt[str] = None
    description: Opt[str] = None
    package_file_name: Opt[str] = None
    install_command: Opt[str] = None
    uninstall_command: Opt[str] = None
    parameters_definition: Opt[ParametersDefinition] = None
    executable_path: Opt[str] = None
    command_parameters: Opt[str] = None
    is_node_process: Opt[bool] = None

    def __init__(
        self,
        *,
        type_name: Opt[str] = None,
        description: Opt[str] = None,
        package_file_name: Opt[str] = None,
        install_command: Opt[str] = None,
        uninstall_command: Opt[str] = None,
        parameters_definition: Opt[ParametersDefinition] = None,
        executable_path: Opt[str] = None,
        command_parameters: Opt[str] = None,
        is_node_process: Opt[bool] = None,
    ) -> None:
        """

        Parameters:
            type_name: The name of the instance template. Used as Id, unique per component.
            description: The description of the instance template.
            package_file_name: The filename of the instance package to use within the component package.
            install_command: A command to execute each time an instance of this type is created on an agent.
            uninstall_command: A command to execute each time an instance of this type is removed from an agent.
            parameters_definition: A list of configuration parameters.
            executable_path: The command to execute. Path must be relative to the root of the archive.
            command_parameters: The command line parameters to use when launching the executable.
            is_node_process: Indicates if the instance is a 'Node Process'.
        """


@attrs(kw_only=True, auto_attribs=True)
class ComponentDefinition(JidType, hint="Coveo.Cdf.Component.ComponentDefinition"):
    """A structure that represents a component package.

    Attributes:
        name: The name of the component. Components of the same name can coexist if their versions differ.
        version: The version of the component. Used as Id, unique per component. Used in conjunction with the component name, the Id becomes unique per node manager and/or agent.
        platform: The platform on wich the component can be deployed.
        target: The target of the package's binaries.
        description: The description of the component.
        location: The path to locate the component package.
        install_command: A command to execute each time the component package is deployed to an agent.
        uninstall_command: A command to execute each time the component package is removed from an agent.
        environment: A list of environment variables set specifically for the component.
        parameters_definition: A list of configuration parameters.
        instances: The list of instance templates defined by this component package.
    """

    name: Opt[str] = None
    version: Opt[str] = None
    platform: Opt[str] = None
    target: Opt[str] = None
    description: Opt[str] = None
    location: Opt[str] = None
    install_command: Opt[str] = None
    uninstall_command: Opt[str] = None
    environment: Opt[Dict[str, str]] = None
    parameters_definition: Opt[ParametersDefinition] = None
    instances: Opt[List[InstanceDefinition]] = None

    def __init__(
        self,
        *,
        name: Opt[str] = None,
        version: Opt[str] = None,
        platform: Opt[str] = None,
        target: Opt[str] = None,
        description: Opt[str] = None,
        location: Opt[str] = None,
        install_command: Opt[str] = None,
        uninstall_command: Opt[str] = None,
        environment: Opt[Dict[str, str]] = None,
        parameters_definition: Opt[ParametersDefinition] = None,
        instances: Opt[List[InstanceDefinition]] = None,
    ) -> None:
        """

        Parameters:
            name: The name of the component. Components of the same name can coexist if their versions differ.
            version: The version of the component. Used as Id, unique per component. Used in conjunction with the component name, the Id becomes unique per node manager and/or agent.
            platform: The platform on wich the component can be deployed.
            target: The target of the package's binaries.
            description: The description of the component.
            location: The path to locate the component package.
            install_command: A command to execute each time the component package is deployed to an agent.
            uninstall_command: A command to execute each time the component package is removed from an agent.
            environment: A list of environment variables set specifically for the component.
            parameters_definition: A list of configuration parameters.
            instances: The list of instance templates defined by this component package.
        """
