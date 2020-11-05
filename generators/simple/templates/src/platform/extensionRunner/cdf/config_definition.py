"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/CoveoConfigDefinition.jid

"""

from attr import attrib, attrs
from typing import Dict, List, Optional as Opt, Union
from .root import CASING, ExceptionBase, JidType


@attrs(kw_only=True, auto_attribs=True)
class ParameterDefinition(JidType, hint="Coveo.ParameterDefinition"):
    """Configuration parameter definition

    Attributes:
        name: Parameter name
        label: Display label
        description: Description
        hint_text: Hint text
        type_: Parameter value type
        hidden: This is an advanced parameter that should be hidden by default
        optional: Parameter is optional
        sensitive: Parameter contains sensitive data
        default_value: Default value
        predefined_values: Allowed values for a parameter with predefined values
        security_types: Allowed security types for a security provider parameter
    """

    name: Opt[str] = None
    label: Opt[str] = None
    description: Opt[str] = None
    hint_text: Opt[str] = None
    type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"})
    hidden: Opt[bool] = None
    optional: Opt[bool] = None
    sensitive: Opt[bool] = None
    default_value: Opt[str] = None
    predefined_values: Opt[Dict[str, str]] = None
    security_types: Opt[List[str]] = None

    def __init__(
        self,
        *,
        name: Opt[str] = None,
        label: Opt[str] = None,
        description: Opt[str] = None,
        hint_text: Opt[str] = None,
        type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"}),
        hidden: Opt[bool] = None,
        optional: Opt[bool] = None,
        sensitive: Opt[bool] = None,
        default_value: Opt[str] = None,
        predefined_values: Opt[Dict[str, str]] = None,
        security_types: Opt[List[str]] = None,
    ) -> None:
        """

        Parameters:
            name: Parameter name
            label: Display label
            description: Description
            hint_text: Hint text
            type_: Parameter value type
            hidden: This is an advanced parameter that should be hidden by default
            optional: Parameter is optional
            sensitive: Parameter contains sensitive data
            default_value: Default value
            predefined_values: Allowed values for a parameter with predefined values
            security_types: Allowed security types for a security provider parameter
        """


@attrs(kw_only=True, auto_attribs=True)
class ParameterGroupDefinition(JidType, hint="Coveo.ParameterGroupDefinition"):
    """Group of Configuration Parameter definitions

    Attributes:
        label: Group label
        parameters: Group parameters
    """

    label: Opt[str] = None
    parameters: Opt[List[ParameterDefinition]] = None

    def __init__(self, *, label: Opt[str] = None, parameters: Opt[List[ParameterDefinition]] = None) -> None:
        """

        Parameters:
            label: Group label
            parameters: Group parameters
        """


@attrs(kw_only=True, auto_attribs=True)
class DataFile(JidType, hint="Coveo.DataFile"):
    """Binary Data File

    Attributes:
        sensitive: Data is sensitive
        data: Binary data
    """

    sensitive: Opt[bool] = None
    data: Opt[Union[str, bytes]] = None

    def __init__(self, *, sensitive: Opt[bool] = None, data: Opt[Union[str, bytes]] = None) -> None:
        """

        Parameters:
            sensitive: Data is sensitive
            data: Binary data
        """


@attrs(kw_only=True, auto_attribs=True)
class Parameter(JidType, hint="Coveo.Parameter"):
    """Parameter

    Attributes:
        sensitive: Value is sensitive
        value: Parameter value
    """

    sensitive: Opt[bool] = None
    value: Opt[str] = None

    def __init__(self, *, sensitive: Opt[bool] = None, value: Opt[str] = None) -> None:
        """

        Parameters:
            sensitive: Value is sensitive
            value: Parameter value
        """


@attrs(kw_only=True, auto_attribs=True)
class UserIdentity(JidType, hint="Coveo.UserIdentity"):
    """User Identity

    Attributes:
        name: Identity Identifier
        user_name: Username
        password: Password
    """

    name: Opt[str] = None
    user_name: Opt[str] = None
    password: Opt[str] = None

    def __init__(self, *, name: Opt[str] = None, user_name: Opt[str] = None, password: Opt[str] = None) -> None:
        """

        Parameters:
            name: Identity Identifier
            user_name: Username
            password: Password
        """


@attrs(kw_only=True, auto_attribs=True)
class SecurityProvider(JidType, hint="Coveo.SecurityProvider"):
    """Resolves permissions of a specific type

    Attributes:
        name: Security Provider instance name
        type_name: Security Type
    """

    name: Opt[str] = None
    type_name: Opt[str] = None

    def __init__(self, *, name: Opt[str] = None, type_name: Opt[str] = None) -> None:
        """

        Parameters:
            name: Security Provider instance name
            type_name: Security Type
        """


@attrs(kw_only=True, auto_attribs=True)
class ConfigException(ExceptionBase, hint="Coveo.ConfigException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class MissingConfigException(ConfigException, hint="Coveo.MissingConfigException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidConfigException(ConfigException, hint="Coveo.InvalidConfigException"):
    def __init__(self) -> None:
        ...
