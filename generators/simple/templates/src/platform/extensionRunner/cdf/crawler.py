"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/Crawler.jid

"""

from attr import attrib, attrs
from datetime import datetime
from enum import auto
from typing import Dict, List, Optional as Opt
from .root import CASING, CoveoInterface, ExceptionBase, JidEnumFlag, JidType, api
from .document_definition import PermissionLevel
from .config_definition import DataFile, Parameter, ParameterGroupDefinition, SecurityProvider
from .document_config_definition import DocumentConfig
from .tracking import MetricEntry, StatusEntry


class AddressPatternType(JidEnumFlag):
    """Type of address pattern

    Attributes:
        Wildcard: Wildcard
        RegEx: Regular Expression
    """

    Wildcard: int = auto()
    RegEx: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class AddressPattern(JidType, hint="Coveo.CrawlerBlade.AddressPattern"):
    """An Address Pattern

    Attributes:
        expression: Pattern Value
        pattern_type: Pattern Type
        allowed: Whether an address matching this pattern is allowed
    """

    expression: Opt[str] = None
    pattern_type: AddressPatternType = AddressPatternType.Wildcard
    allowed: bool = True

    def __init__(
        self,
        *,
        expression: Opt[str] = None,
        pattern_type: AddressPatternType = AddressPatternType.Wildcard,
        allowed: bool = True,
    ) -> None:
        """

        Parameters:
            expression: Pattern Value
            pattern_type: Pattern Type
            allowed: Whether an address matching this pattern is allowed
        """


@attrs(kw_only=True, auto_attribs=True)
class SourceInformation(JidType, hint="Coveo.CrawlerBlade.SourceInformation"):
    """Source Information

    Attributes:
        source_id: Source Identifier
        source_name: Source Name
        collection_id: Collection Identifier
        collection_name: Collection Name
    """

    source_id: Opt[int] = None
    source_name: Opt[str] = None
    collection_id: Opt[int] = None
    collection_name: Opt[str] = None

    def __init__(
        self,
        *,
        source_id: Opt[int] = None,
        source_name: Opt[str] = None,
        collection_id: Opt[int] = None,
        collection_name: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            source_id: Source Identifier
            source_name: Source Name
            collection_id: Collection Identifier
            collection_name: Collection Name
        """


@attrs(kw_only=True, auto_attribs=True)
class UserIdentity(JidType, hint="Coveo.CrawlerBlade.UserIdentity"):
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


class SecurityOption(JidEnumFlag):
    """Security Indexing Option

    Attributes:
        Retrieve: Retrieve
        Specified: Specified by User
        Merge: Retrieve and Merge with Specified
    """

    Retrieve: int = auto()
    Specified: int = auto()
    Merge: int = auto()


class FormAuthenticationMethod(JidEnumFlag):
    """Form Authentication HTTP method

    Attributes:
        Post: POST
        Get: GET
    """

    Post: int = auto()
    Get: int = auto()


class FormAuthenticationInputType(JidEnumFlag):
    """Form Authentication input parameter type

    Attributes:
        Text: Text
        Password: Password
        Checkbox: Checkbox
        Radio: Radio button
        Submit: Submit
        Reset: Reset
        File: File
        Hidden: Hidden
        Image: Image
        Button: Button
    """

    Text: int = auto()
    Password: int = auto()
    Checkbox: int = auto()
    Radio: int = auto()
    Submit: int = auto()
    Reset: int = auto()
    File: int = auto()
    Hidden: int = auto()
    Image: int = auto()
    Button: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class FormAuthenticationInput(JidType, hint="Coveo.CrawlerBlade.FormAuthenticationInput"):
    """Form Authentication input parameter

    Attributes:
        type_: Parameter type
        name: Parameter name
        value: Parameter value
    """

    type_: Opt[FormAuthenticationInputType] = attrib(default=None, metadata={CASING: "Type"})
    name: Opt[str] = None
    value: Opt[str] = None

    def __init__(
        self,
        *,
        type_: Opt[FormAuthenticationInputType] = attrib(default=None, metadata={CASING: "Type"}),
        name: Opt[str] = None,
        value: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            type_: Parameter type
            name: Parameter name
            value: Parameter value
        """


@attrs(kw_only=True, auto_attribs=True)
class FormAuthentication(JidType, hint="Coveo.CrawlerBlade.FormAuthentication"):
    """Form Authentication parameters

    Attributes:
        secure_url: URL of the secure resources requiring Form Authentication
        form_url: URL of the Form
        action_url: URL of the Form Authentication request destination
        action_method: HTTP method of the Form Authentication request
        inputs: Form Authentication parameters
        reauthenticate: Authenticate every time a secure resource is accessed
    """

    secure_url: Opt[str] = attrib(default=None, metadata={CASING: "SecureURL"})
    form_url: Opt[str] = attrib(default=None, metadata={CASING: "FormURL"})
    action_url: Opt[str] = attrib(default=None, metadata={CASING: "ActionURL"})
    action_method: FormAuthenticationMethod = FormAuthenticationMethod.Post
    inputs: Opt[List[FormAuthenticationInput]] = None
    reauthenticate: Opt[bool] = None

    def __init__(
        self,
        *,
        secure_url: Opt[str] = attrib(default=None, metadata={CASING: "SecureURL"}),
        form_url: Opt[str] = attrib(default=None, metadata={CASING: "FormURL"}),
        action_url: Opt[str] = attrib(default=None, metadata={CASING: "ActionURL"}),
        action_method: FormAuthenticationMethod = FormAuthenticationMethod.Post,
        inputs: Opt[List[FormAuthenticationInput]] = None,
        reauthenticate: Opt[bool] = None,
    ) -> None:
        """

        Parameters:
            secure_url: URL of the secure resources requiring Form Authentication
            form_url: URL of the Form
            action_url: URL of the Form Authentication request destination
            action_method: HTTP method of the Form Authentication request
            inputs: Form Authentication parameters
            reauthenticate: Authenticate every time a secure resource is accessed
        """


@attrs(kw_only=True, auto_attribs=True)
class Config(JidType, hint="Coveo.CrawlerBlade.Config"):
    """Crawler Configuration

    Attributes:
        document_consumer_uri: The document consumer URI
        index_identifier: The index identifier
        db_connection_string: The database connection string
        reporting_service_uri: The reporting service URI
        source_information: Source and Collection Information
        source_security_option: Security Indexing Option
        starting_addresses: Starting Addresses for Indexing
        address_patterns: Starting Addresses Patterns
        permissions: User-specified Permissions
        parameters: Source Parameters
        security_providers: Security Providers
        user_identities: User Identities
        data_files: The data files
        case_sensitive_patterns: Whether the AddressPatterns are case sensitive or not.
        document_config: Config used for conversion
    """

    document_consumer_uri: Opt[str] = attrib(default=None, metadata={CASING: "DocumentConsumerURI"})
    index_identifier: Opt[str] = None
    db_connection_string: Opt[str] = None
    reporting_service_uri: Opt[str] = None
    source_information: Opt[SourceInformation] = None
    source_security_option: SecurityOption = SecurityOption.Retrieve
    starting_addresses: Opt[List[str]] = None
    address_patterns: Opt[List[AddressPattern]] = None
    permissions: Opt[List[PermissionLevel]] = None
    parameters: Opt[Dict[str, Parameter]] = None
    security_providers: Opt[Dict[str, SecurityProvider]] = None
    user_identities: Opt[Dict[str, UserIdentity]] = None
    data_files: Opt[Dict[str, DataFile]] = None
    case_sensitive_patterns: bool = True
    document_config: Opt[DocumentConfig] = None

    def __init__(
        self,
        *,
        document_consumer_uri: Opt[str] = attrib(default=None, metadata={CASING: "DocumentConsumerURI"}),
        index_identifier: Opt[str] = None,
        db_connection_string: Opt[str] = None,
        reporting_service_uri: Opt[str] = None,
        source_information: Opt[SourceInformation] = None,
        source_security_option: SecurityOption = SecurityOption.Retrieve,
        starting_addresses: Opt[List[str]] = None,
        address_patterns: Opt[List[AddressPattern]] = None,
        permissions: Opt[List[PermissionLevel]] = None,
        parameters: Opt[Dict[str, Parameter]] = None,
        security_providers: Opt[Dict[str, SecurityProvider]] = None,
        user_identities: Opt[Dict[str, UserIdentity]] = None,
        data_files: Opt[Dict[str, DataFile]] = None,
        case_sensitive_patterns: bool = True,
        document_config: Opt[DocumentConfig] = None,
    ) -> None:
        """

        Parameters:
            document_consumer_uri: The document consumer URI
            index_identifier: The index identifier
            db_connection_string: The database connection string
            reporting_service_uri: The reporting service URI
            source_information: Source and Collection Information
            source_security_option: Security Indexing Option
            starting_addresses: Starting Addresses for Indexing
            address_patterns: Starting Addresses Patterns
            permissions: User-specified Permissions
            parameters: Source Parameters
            security_providers: Security Providers
            user_identities: User Identities
            data_files: The data files
            case_sensitive_patterns: Whether the AddressPatterns are case sensitive or not.
            document_config: Config used for conversion
        """


@attrs(kw_only=True, auto_attribs=True)
class CrawlerException(ExceptionBase, hint="Coveo.CrawlerBlade.CrawlerException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SourceAlreadyRefreshingException(CrawlerException, hint="Coveo.CrawlerBlade.SourceAlreadyRefreshingException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class DataPathAlreadySetException(CrawlerException, hint="Coveo.CrawlerBlade.DataPathAlreadySetException"):
    def __init__(self) -> None:
        ...


class RefreshType(JidEnumFlag):
    Rebuild: int = auto()
    FullRefresh: int = auto()
    IncrementalRefresh: int = auto()


class SourceRefreshType(JidEnumFlag):
    None_: int = auto()
    Rebuild: int = auto()
    FullRefresh: int = auto()
    IncrementalRefresh: int = auto()
    RefreshUri: int = auto()


class RefreshStatusType(JidEnumFlag):
    NotStarted: int = auto()
    Refreshing: int = auto()
    Paused: int = auto()
    Interrupted: int = auto()
    Stopped: int = auto()
    Finished: int = auto()
    OnError: int = auto()
    PausedOnError: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class RefreshError(JidType, hint="Coveo.CrawlerBlade.RefreshError"):
    """

    Attributes:
        message: The error message
        code: The error code
    """

    message: Opt[str] = None
    code: Opt[str] = None

    def __init__(self, *, message: Opt[str] = None, code: Opt[str] = None) -> None:
        """

        Parameters:
            message: The error message
            code: The error code
        """


@attrs(kw_only=True, auto_attribs=True)
class RefreshStatus(StatusEntry, hint="Coveo.CrawlerBlade.RefreshStatus"):
    """A structure that represents a source refresh status.

    Attributes:
        source_id: Source Identifier
        collection_id: Collection Identifier
        operation_id: The operation id
        type_: Refresh type
        status: Refresh status
        start_date: Start of the refresh
        end_date: End of the refresh
        last_activity_date_utc: Last activity date in UTC
        added_count: Added documents count
        updated_count: Modified documents count
        removed_count: Deleted documents count
        unchanged_count: Unchanged documents count
        filtered_count: Filtered documents count
        ignored_uri_count: Ignored URI count
        total_size: Total size of indexed documents
        index_identifier: The index identifier
        error: The error that forced the refresh to be OnError
    """

    source_id: Opt[int] = None
    collection_id: Opt[int] = None
    operation_id: Opt[str] = None
    type_: Opt[SourceRefreshType] = attrib(default=None, metadata={CASING: "Type"})
    status: Opt[RefreshStatusType] = None
    start_date: Opt[datetime] = None
    end_date: Opt[datetime] = None
    last_activity_date_utc: Opt[datetime] = None
    added_count: Opt[int] = None
    updated_count: Opt[int] = None
    removed_count: Opt[int] = None
    unchanged_count: Opt[int] = None
    filtered_count: Opt[int] = None
    ignored_uri_count: Opt[int] = None
    total_size: Opt[int] = None
    index_identifier: Opt[str] = None
    error: Opt[RefreshError] = None

    def __init__(
        self,
        *,
        source_id: Opt[int] = None,
        collection_id: Opt[int] = None,
        operation_id: Opt[str] = None,
        type_: Opt[SourceRefreshType] = attrib(default=None, metadata={CASING: "Type"}),
        status: Opt[RefreshStatusType] = None,
        start_date: Opt[datetime] = None,
        end_date: Opt[datetime] = None,
        last_activity_date_utc: Opt[datetime] = None,
        added_count: Opt[int] = None,
        updated_count: Opt[int] = None,
        removed_count: Opt[int] = None,
        unchanged_count: Opt[int] = None,
        filtered_count: Opt[int] = None,
        ignored_uri_count: Opt[int] = None,
        total_size: Opt[int] = None,
        index_identifier: Opt[str] = None,
        error: Opt[RefreshError] = None,
    ) -> None:
        """

        Parameters:
            source_id: Source Identifier
            collection_id: Collection Identifier
            operation_id: The operation id
            type_: Refresh type
            status: Refresh status
            start_date: Start of the refresh
            end_date: End of the refresh
            last_activity_date_utc: Last activity date in UTC
            added_count: Added documents count
            updated_count: Modified documents count
            removed_count: Deleted documents count
            unchanged_count: Unchanged documents count
            filtered_count: Filtered documents count
            ignored_uri_count: Ignored URI count
            total_size: Total size of indexed documents
            index_identifier: The index identifier
            error: The error that forced the refresh to be OnError
        """


@attrs(kw_only=True, auto_attribs=True)
class CrawlerStatus(StatusEntry, hint="Coveo.CrawlerBlade.CrawlerStatus"):
    """A structure that represents a crawler status.

    Attributes:
        live_monitor_enabled: Whether or not live monitoring is enabled
        index_identifier: The index identifier
    """

    live_monitor_enabled: Opt[bool] = None
    index_identifier: Opt[str] = None

    def __init__(self, *, live_monitor_enabled: Opt[bool] = None, index_identifier: Opt[str] = None) -> None:
        """

        Parameters:
            live_monitor_enabled: Whether or not live monitoring is enabled
            index_identifier: The index identifier
        """


class OperationType(JidEnumFlag):
    Added: int = auto()
    Deleted: int = auto()
    Updated: int = auto()
    Unmodified: int = auto()
    IsAlias: int = auto()
    Unauthorized: int = auto()
    NotFound: int = auto()
    Filtered: int = auto()
    FilteredByDocumentType: int = auto()
    FilteredByRobots: int = auto()
    Warning: int = auto()
    Error: int = auto()


class ContextType(JidEnumFlag):
    Rebuild: int = auto()
    FullRefresh: int = auto()
    IncrementalRefresh: int = auto()
    LiveMonitoring: int = auto()
    RefreshDocument: int = auto()
    RebuildDocument: int = auto()
    RefreshFolder: int = auto()
    RebuildFolder: int = auto()
    DeleteDocument: int = auto()
    DeleteFolder: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class CrawlerMetric(MetricEntry, hint="Coveo.CrawlerBlade.CrawlerMetric"):
    """A structure that represents a crawler metric.

    Attributes:
        source_id: Source Identifier
        collection_id: Collection Identifier
        operation_id: The operation id
        operation: The operation
        context: The context
        value: The value
        error_code: Used when operation is an Error
    """

    source_id: Opt[int] = None
    collection_id: Opt[int] = None
    operation_id: Opt[str] = None
    operation: Opt[OperationType] = None
    context: Opt[ContextType] = None
    value: Opt[float] = None
    error_code: Opt[str] = None

    def __init__(
        self,
        *,
        source_id: Opt[int] = None,
        collection_id: Opt[int] = None,
        operation_id: Opt[str] = None,
        operation: Opt[OperationType] = None,
        context: Opt[ContextType] = None,
        value: Opt[float] = None,
        error_code: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            source_id: Source Identifier
            collection_id: Collection Identifier
            operation_id: The operation id
            operation: The operation
            context: The context
            value: The value
            error_code: Used when operation is an Error
        """


class ICrawler(CoveoInterface):
    @api("POST/data_path")
    def set_data_path(self, *, data_path: str) -> None:
        ...

    @api("GET/refreshstatus")
    def get_status(self) -> RefreshStatus:
        ...

    @api("GET/config")
    def get_config(self) -> Config:
        ...

    @api("PUT/config")
    def set_config(self, *, config: Config) -> None:
        ...

    @api("GET/parameters")
    def get_parameters(self) -> List[ParameterGroupDefinition]:
        ...

    @api("GET/capabilities")
    def get_capabilities(self) -> int:
        ...

    @api("PUT/live_monitoring")
    def set_live_monitoring(self, *, enabled: bool) -> None:
        ...

    @api("POST/refresh")
    def start_refresh(self, *, operation_id: str, refresh_type: RefreshType) -> None:
        ...

    @api("POST/refresh/pause")
    def pause_refresh(self) -> None:
        ...

    @api("POST/refresh/resume")
    def resume_refresh(self) -> None:
        ...

    @api("POST/refresh/stop")
    def stop_refresh(self) -> None:
        ...

    @api("POST/refresh/uri", uri="URI")
    def refresh_uri(
        self, *, operation_id: str, uri: str, recursive: bool, force_refresh: bool, high_priority: bool
    ) -> None:
        ...

    @api("DELETE/refresh/uri", uri="URI", printable_uri="PrintableURI")
    def delete_uri(self, *, operation_id: str, uri: str, recursive: bool, printable_uri: bool) -> bool:
        ...

    @api("DELETE/source/persistence")
    def delete_source(self) -> None:
        ...
