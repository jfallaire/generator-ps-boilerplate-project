"""
    - THIS FILE IS GENERATED -

dependencies/CMF.Net/Cmf/CmfAdminService/CoveoCmfAdminService.jid

"""

from attr import attrib, attrs
from datetime import datetime
from enum import auto
from typing import Dict, List, Optional as Opt
from .root import CASING, CoveoInterface, ExceptionBase, JidEnumFlag, JidType, api
from .tracking import CallProgress, TrackingException
from .parameter_store import Credential


@attrs(kw_only=True, auto_attribs=True)
class InvalidCallIdException(TrackingException, hint="Coveo.CmfAdmin.InvalidCallIdException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class CallCancelledException(ExceptionBase, hint="Coveo.CmfAdmin.CallCancelledException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class StopConsumingFromQueueException(ExceptionBase, hint="Coveo.CmfAdmin.StopConsumingFromQueueException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class NeverRetryException(ExceptionBase, hint="Coveo.CmfAdmin.NeverRetryException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ServantInfo(JidType, hint="Coveo.CmfAdmin.ServantInfo"):
    """A structure that describes a communication servant/handler.

    Attributes:
        name: The name of the servant.
        ifaces: The list of interfaces served by the servant.
        strategies: The optional strategies incoming messages go through.
    """

    name: Opt[str] = None
    ifaces: Opt[List[str]] = None
    strategies: Opt[str] = None

    def __init__(self, *, name: Opt[str] = None, ifaces: Opt[List[str]] = None, strategies: Opt[str] = None) -> None:
        """

        Parameters:
            name: The name of the servant.
            ifaces: The list of interfaces served by the servant.
            strategies: The optional strategies incoming messages go through.
        """


@attrs(kw_only=True, auto_attribs=True)
class ServerInfo(JidType, hint="Coveo.CmfAdmin.ServerInfo"):
    """A structure that represents a communication server.

    Attributes:
        server_uri: The normalized uri of the server.
        full_uri: The full uri of the server.
        is_started: Indicates if the server is started.
        servants: The list of servants hosted by the server.
        strategies: The optional strategies attached to this server.
        rest_urls: All the REST urls supported by this server, if web.
    """

    server_uri: Opt[str] = None
    full_uri: Opt[str] = None
    is_started: Opt[bool] = None
    servants: Opt[List[ServantInfo]] = None
    strategies: Opt[str] = None
    rest_urls: Opt[List[str]] = None

    def __init__(
        self,
        *,
        server_uri: Opt[str] = None,
        full_uri: Opt[str] = None,
        is_started: Opt[bool] = None,
        servants: Opt[List[ServantInfo]] = None,
        strategies: Opt[str] = None,
        rest_urls: Opt[List[str]] = None,
    ) -> None:
        """

        Parameters:
            server_uri: The normalized uri of the server.
            full_uri: The full uri of the server.
            is_started: Indicates if the server is started.
            servants: The list of servants hosted by the server.
            strategies: The optional strategies attached to this server.
            rest_urls: All the REST urls supported by this server, if web.
        """


@attrs(kw_only=True, auto_attribs=True)
class ProxyInfo(JidType, hint="Coveo.CmfAdmin.ProxyInfo"):
    """A structure that represents a communication proxy.

    Attributes:
        server_uri: The normalized uri targeted by the proxy.
        full_uri: The full Uri targeted by the proxy.
        servant: The servant targeted by the proxy.
        iface: The iface targeted by the proxy.
        strategies: The optional strategies outgoing messages go through.
    """

    server_uri: Opt[str] = None
    full_uri: Opt[str] = None
    servant: Opt[str] = None
    iface: Opt[str] = None
    strategies: Opt[str] = None

    def __init__(
        self,
        *,
        server_uri: Opt[str] = None,
        full_uri: Opt[str] = None,
        servant: Opt[str] = None,
        iface: Opt[str] = None,
        strategies: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            server_uri: The normalized uri targeted by the proxy.
            full_uri: The full Uri targeted by the proxy.
            servant: The servant targeted by the proxy.
            iface: The iface targeted by the proxy.
            strategies: The optional strategies outgoing messages go through.
        """


@attrs(kw_only=True, auto_attribs=True)
class ChannelInfo(JidType, hint="Coveo.CmfAdmin.ChannelInfo"):
    """A structure that represents a pre-Cmf channel.

    Attributes:
        name: The channel name.
        is_ssl: Does the channel use SSL ?
        request_categories: The request categories served by this channel.
    """

    name: Opt[str] = None
    is_ssl: Opt[bool] = None
    request_categories: Opt[List[int]] = None

    def __init__(
        self, *, name: Opt[str] = None, is_ssl: Opt[bool] = None, request_categories: Opt[List[int]] = None
    ) -> None:
        """

        Parameters:
            name: The channel name.
            is_ssl: Does the channel use SSL ?
            request_categories: The request categories served by this channel.
        """


@attrs(kw_only=True, auto_attribs=True)
class StrategyType(JidType, hint="Coveo.CmfAdmin.StrategyType"):
    """A structure that represents a strategy type.

    Attributes:
        name: The strategy name.
        parameters: The available parameters.
    """

    name: Opt[str] = None
    parameters: Opt[List[str]] = None

    def __init__(self, *, name: Opt[str] = None, parameters: Opt[List[str]] = None) -> None:
        """

        Parameters:
            name: The strategy name.
            parameters: The available parameters.
        """


@attrs(kw_only=True, auto_attribs=True)
class UriAlias(JidType, hint="Coveo.CmfAdmin.UriAlias"):
    """A structure that represents an URI alias.

    Attributes:
        name: The name of the alias.
        uri: The replacement uri.
    """

    name: Opt[str] = None
    uri: Opt[str] = None

    def __init__(self, *, name: Opt[str] = None, uri: Opt[str] = None) -> None:
        """

        Parameters:
            name: The name of the alias.
            uri: The replacement uri.
        """


@attrs(kw_only=True, auto_attribs=True)
class UriMatcher(JidType, hint="Coveo.CmfAdmin.UriMatcher"):
    """A structure that represents an uri matcher. Used to know what strategies apply to an uri. The primary key is IsProxy+Uri+Servant.

    Attributes:
        name: The name of the UriMatcher. Optional; if not specified, will be composed of its PK.
        is_proxy: If specified (only needed if can't be deduced from strategies), tells if this matches proxies.
        uri: The server to match.
        servant: The optional servant name.
        strategies: If the uri matches a server, apply these strategies.
        strategy_list: If the uri matches a server, apply this list of strategies. Exclusive with 'Strategies'.
    """

    name: Opt[str] = None
    is_proxy: Opt[bool] = None
    uri: Opt[str] = None
    servant: Opt[str] = None
    strategies: Opt[List[str]] = None
    strategy_list: Opt[str] = None

    def __init__(
        self,
        *,
        name: Opt[str] = None,
        is_proxy: Opt[bool] = None,
        uri: Opt[str] = None,
        servant: Opt[str] = None,
        strategies: Opt[List[str]] = None,
        strategy_list: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            name: The name of the UriMatcher. Optional; if not specified, will be composed of its PK.
            is_proxy: If specified (only needed if can't be deduced from strategies), tells if this matches proxies.
            uri: The server to match.
            servant: The optional servant name.
            strategies: If the uri matches a server, apply these strategies.
            strategy_list: If the uri matches a server, apply this list of strategies. Exclusive with 'Strategies'.
        """


@attrs(kw_only=True, auto_attribs=True)
class StrategyList(JidType, hint="Coveo.CmfAdmin.StrategyList"):
    """A structure that represents the strategies to apply to an uri (it can be an alias too).

    Attributes:
        name: The name of the list.
        strategies: The strategy names to apply.
    """

    name: Opt[str] = None
    strategies: Opt[List[str]] = None

    def __init__(self, *, name: Opt[str] = None, strategies: Opt[List[str]] = None) -> None:
        """

        Parameters:
            name: The name of the list.
            strategies: The strategy names to apply.
        """


@attrs(kw_only=True, auto_attribs=True)
class BaseStrategy(JidType, hint="Coveo.CmfAdmin.BaseStrategy"):
    """A structure that represents a communication strategy.

    Attributes:
        name: The name of the strategy.
        type_: The type of the strategy. This will also dictate if the strategy is proxy and/or server-side.
        parameters: Additional parameters.
        disabled: Is this strategy  disabled ?
    """

    name: Opt[str] = None
    type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"})
    parameters: Opt[Dict[str, str]] = None
    disabled: Opt[bool] = None

    def __init__(
        self,
        *,
        name: Opt[str] = None,
        type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"}),
        parameters: Opt[Dict[str, str]] = None,
        disabled: Opt[bool] = None,
    ) -> None:
        """

        Parameters:
            name: The name of the strategy.
            type_: The type of the strategy. This will also dictate if the strategy is proxy and/or server-side.
            parameters: Additional parameters.
            disabled: Is this strategy  disabled ?
        """


@attrs(kw_only=True, auto_attribs=True)
class QueueStrategy(BaseStrategy, hint="Coveo.CmfAdmin.QueueStrategy"):
    """A structure that represents a communication queue strategy.

    Attributes:
        host: The queue server default host.
        port: The queue server default port.
        user: The queue server default user.
        password: The queue server default password.
        certificate: The certificate. Either in base64 form, or a filename.
        certificate_format: The certificate format.
        key: The private key. Either in base64 form, or a filename
        key_format: The private key format.
        trusted_cas: The trusted CAs. Either in base64 form, or a filename.
    """

    host: Opt[str] = None
    port: Opt[int] = None
    user: Opt[str] = None
    password: Opt[str] = None
    certificate: Opt[str] = None
    certificate_format: Opt[str] = None
    key: Opt[str] = None
    key_format: Opt[str] = None
    trusted_cas: Opt[str] = attrib(default=None, metadata={CASING: "TrustedCAs"})

    def __init__(
        self,
        *,
        host: Opt[str] = None,
        port: Opt[int] = None,
        user: Opt[str] = None,
        password: Opt[str] = None,
        certificate: Opt[str] = None,
        certificate_format: Opt[str] = None,
        key: Opt[str] = None,
        key_format: Opt[str] = None,
        trusted_cas: Opt[str] = attrib(default=None, metadata={CASING: "TrustedCAs"}),
    ) -> None:
        """

        Parameters:
            host: The queue server default host.
            port: The queue server default port.
            user: The queue server default user.
            password: The queue server default password.
            certificate: The certificate. Either in base64 form, or a filename.
            certificate_format: The certificate format.
            key: The private key. Either in base64 form, or a filename
            key_format: The private key format.
            trusted_cas: The trusted CAs. Either in base64 form, or a filename.
        """


@attrs(kw_only=True, auto_attribs=True)
class MultiQueueParameters(JidType, hint="Coveo.CmfAdmin.MultiQueueParameters"):
    """Parameters on how with consume from multiple queue

    Attributes:
        duration: Time in seconds allowed to consume messages before going to the next queue
        use_secure_admin: Whether or not to use SSL when talking to the queue admin
        throttling_service_uri: The uri of the throttling service.
        max_service_backoff_seconds: The maximum polling wait period when the throttling service has no job.
        use_basic_get: Whether to use BasicGet instead of BasicConsume to read from queues.
        queue_type: The type of random queue to get from the service ex: dpm
    """

    duration: Opt[int] = None
    use_secure_admin: Opt[str] = None
    throttling_service_uri: Opt[str] = attrib(default=None, metadata={CASING: "ThrottlingServiceURI"})
    max_service_backoff_seconds: int = 30
    use_basic_get: Opt[bool] = None
    queue_type: Opt[str] = None

    def __init__(
        self,
        *,
        duration: Opt[int] = None,
        use_secure_admin: Opt[str] = None,
        throttling_service_uri: Opt[str] = attrib(default=None, metadata={CASING: "ThrottlingServiceURI"}),
        max_service_backoff_seconds: int = 30,
        use_basic_get: Opt[bool] = None,
        queue_type: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            duration: Time in seconds allowed to consume messages before going to the next queue
            use_secure_admin: Whether or not to use SSL when talking to the queue admin
            throttling_service_uri: The uri of the throttling service.
            max_service_backoff_seconds: The maximum polling wait period when the throttling service has no job.
            use_basic_get: Whether to use BasicGet instead of BasicConsume to read from queues.
            queue_type: The type of random queue to get from the service ex: dpm
        """


@attrs(kw_only=True, auto_attribs=True)
class MultiQueueStrategy(BaseStrategy, hint="Coveo.CmfAdmin.MultiQueueStrategy"):
    """Will consume from multiple queue

    Attributes:
        params: Parameters for the strategy
    """

    params: Opt[MultiQueueParameters] = None

    def __init__(self, *, params: Opt[MultiQueueParameters] = None) -> None:
        """

        Parameters:
            params: Parameters for the strategy
        """


@attrs(kw_only=True, auto_attribs=True)
class AuthPrivilege(JidType, hint="Coveo.CmfAdmin.AuthPrivilege"):
    """Privilege that can be requested to the authorization server.

    Attributes:
        organization_id: The organization id, needed for org-bound privileges.
        target_id: The target id, needed for granular access to single resources.
        target_domain: The target domain, designates the permission that we want (e.g. NODE_ADMINISTRATION).
        owner: The owner of the privilege, generally PLATFORM or BACKEND, depends on your use case.
        level: The level of the privilege, generally NORMAL, INTERNAL or GLOBAL.
        type_: The type of the privilege, generally VIEW or EDIT, depends on your use case.
    """

    organization_id: Opt[str] = None
    target_id: Opt[str] = None
    target_domain: Opt[str] = None
    owner: Opt[str] = None
    level: Opt[str] = None
    type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"})

    def __init__(
        self,
        *,
        organization_id: Opt[str] = None,
        target_id: Opt[str] = None,
        target_domain: Opt[str] = None,
        owner: Opt[str] = None,
        level: Opt[str] = None,
        type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"}),
    ) -> None:
        """

        Parameters:
            organization_id: The organization id, needed for org-bound privileges.
            target_id: The target id, needed for granular access to single resources.
            target_domain: The target domain, designates the permission that we want (e.g. NODE_ADMINISTRATION).
            owner: The owner of the privilege, generally PLATFORM or BACKEND, depends on your use case.
            level: The level of the privilege, generally NORMAL, INTERNAL or GLOBAL.
            type_: The type of the privilege, generally VIEW or EDIT, depends on your use case.
        """


@attrs(kw_only=True, auto_attribs=True)
class OauthTokenValidatorStrategy(BaseStrategy, hint="Coveo.CmfAdmin.OauthTokenValidatorStrategy"):
    """Will validate the authority of the caller before letting call through

    Attributes:
        auth_server_uri: Uri of the authorization server used to validate the token
        required_authority: Required authority for the caller
        user_privilege: User privilege that will also grant access.
        user_read_privilege: User privilege that will be applied to GET requests. Use if you want different check for GET.
        throw_if_disabled: Whether to throw when invoked and the strategy is disabled
        throw_if_incomplete: Whether to throw when invoked and the strategy is incompletely parameterized
    """

    auth_server_uri: Opt[str] = None
    required_authority: Opt[str] = None
    user_privilege: Opt[AuthPrivilege] = None
    user_read_privilege: Opt[AuthPrivilege] = None
    throw_if_disabled: Opt[bool] = None
    throw_if_incomplete: Opt[bool] = None

    def __init__(
        self,
        *,
        auth_server_uri: Opt[str] = None,
        required_authority: Opt[str] = None,
        user_privilege: Opt[AuthPrivilege] = None,
        user_read_privilege: Opt[AuthPrivilege] = None,
        throw_if_disabled: Opt[bool] = None,
        throw_if_incomplete: Opt[bool] = None,
    ) -> None:
        """

        Parameters:
            auth_server_uri: Uri of the authorization server used to validate the token
            required_authority: Required authority for the caller
            user_privilege: User privilege that will also grant access.
            user_read_privilege: User privilege that will be applied to GET requests. Use if you want different check for GET.
            throw_if_disabled: Whether to throw when invoked and the strategy is disabled
            throw_if_incomplete: Whether to throw when invoked and the strategy is incompletely parameterized
        """


@attrs(kw_only=True, auto_attribs=True)
class ProxyStrategy(BaseStrategy, hint="Coveo.CmfAdmin.ProxyStrategy"):
    """A structure that represents a communication proxy strategy."""

    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ProxySslStrategy(ProxyStrategy, hint="Coveo.CmfAdmin.ProxySslStrategy"):
    """A structure that represents a communication proxy SSL strategy.

    Attributes:
        certificate: The certificate. Either in base64 form, or a filename.
        certificate_format: The certificate format.
        key: The private key. Either in base64 form, or a filename
        key_format: The private key format.
        trusted_cas: The trusted CAs. Either in base64 form, or a filename.
    """

    certificate: Opt[str] = None
    certificate_format: Opt[str] = None
    key: Opt[str] = None
    key_format: Opt[str] = None
    trusted_cas: Opt[str] = attrib(default=None, metadata={CASING: "TrustedCAs"})

    def __init__(
        self,
        *,
        certificate: Opt[str] = None,
        certificate_format: Opt[str] = None,
        key: Opt[str] = None,
        key_format: Opt[str] = None,
        trusted_cas: Opt[str] = attrib(default=None, metadata={CASING: "TrustedCAs"}),
    ) -> None:
        """

        Parameters:
            certificate: The certificate. Either in base64 form, or a filename.
            certificate_format: The certificate format.
            key: The private key. Either in base64 form, or a filename
            key_format: The private key format.
            trusted_cas: The trusted CAs. Either in base64 form, or a filename.
        """


class CommunicationErrorType(JidEnumFlag):
    None_: int = auto()
    IgnoreUnknownQueue: int = auto()
    All: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class WaitOnException(JidType, hint="Coveo.CmfAdmin.WaitOnException"):
    """

    Attributes:
        maximum_retry_count: Maximum number times to retry. 0 means retry for ever
        maximum_retry_time: Maximum number of seconds to retry. 0 means retry for ever.
        time_before_retry_ms: Number of milliseconds to sleep before retrying
        exponential_backoff_maximum: Maximum wait time in seconds for exponential backoff, 0 to disable exponential backoff.
        report_error_frequency: Will report an error once in X seconds. 0 to report everytime.
        exceptions_to_retry: Fully qualified exception names to retry on ex: Coveo.ThrottlingException
        exceptions_to_ignore: Fully qualified exception names that we won't retry, let's say we want to retry on a specific base class but not on a derived class
        communication_error: Whether to retry on communication errors (rabbit, network, 400 etc)
        http_status_code_to_retry: List of http status to retry.
    """

    maximum_retry_count: Opt[int] = None
    maximum_retry_time: Opt[int] = None
    time_before_retry_ms: int = attrib(default=1000, metadata={CASING: "TimeBeforeRetry_ms"})
    exponential_backoff_maximum: Opt[int] = None
    report_error_frequency: int = 30
    exceptions_to_retry: Opt[List[str]] = None
    exceptions_to_ignore: Opt[List[str]] = None
    communication_error: Opt[CommunicationErrorType] = None
    http_status_code_to_retry: Opt[List[int]] = None

    def __init__(
        self,
        *,
        maximum_retry_count: Opt[int] = None,
        maximum_retry_time: Opt[int] = None,
        time_before_retry_ms: int = attrib(default=1000, metadata={CASING: "TimeBeforeRetry_ms"}),
        exponential_backoff_maximum: Opt[int] = None,
        report_error_frequency: int = 30,
        exceptions_to_retry: Opt[List[str]] = None,
        exceptions_to_ignore: Opt[List[str]] = None,
        communication_error: Opt[CommunicationErrorType] = None,
        http_status_code_to_retry: Opt[List[int]] = None,
    ) -> None:
        """

        Parameters:
            maximum_retry_count: Maximum number times to retry. 0 means retry for ever
            maximum_retry_time: Maximum number of seconds to retry. 0 means retry for ever.
            time_before_retry_ms: Number of milliseconds to sleep before retrying
            exponential_backoff_maximum: Maximum wait time in seconds for exponential backoff, 0 to disable exponential backoff.
            report_error_frequency: Will report an error once in X seconds. 0 to report everytime.
            exceptions_to_retry: Fully qualified exception names to retry on ex: Coveo.ThrottlingException
            exceptions_to_ignore: Fully qualified exception names that we won't retry, let's say we want to retry on a specific base class but not on a derived class
            communication_error: Whether to retry on communication errors (rabbit, network, 400 etc)
            http_status_code_to_retry: List of http status to retry.
        """


@attrs(kw_only=True, auto_attribs=True)
class ProxyRetryStrategy(ProxyStrategy, hint="Coveo.CmfAdmin.ProxyRetryStrategy"):
    """A structure that represents a communication proxy retry strategy.

    Attributes:
        wait_on_exceptions: The exceptions that the strategy will wait on
        do_not_quit: Will keep retrying even if the quit event is posted
        time_before_retry_ms: After a failed connection attempt, wait that many milliseconds before attempting to connect again.
        max_nb_tries: After this many failed connection attemps, let the communication exception bubble up.
    """

    wait_on_exceptions: Opt[List[WaitOnException]] = None
    do_not_quit: Opt[bool] = None
    time_before_retry_ms: Opt[int] = attrib(default=None, metadata={CASING: "TimeBeforeRetry_ms"})
    max_nb_tries: Opt[int] = None

    def __init__(
        self,
        *,
        wait_on_exceptions: Opt[List[WaitOnException]] = None,
        do_not_quit: Opt[bool] = None,
        time_before_retry_ms: Opt[int] = attrib(default=None, metadata={CASING: "TimeBeforeRetry_ms"}),
        max_nb_tries: Opt[int] = None,
    ) -> None:
        """

        Parameters:
            wait_on_exceptions: The exceptions that the strategy will wait on
            do_not_quit: Will keep retrying even if the quit event is posted
            time_before_retry_ms: After a failed connection attempt, wait that many milliseconds before attempting to connect again.
            max_nb_tries: After this many failed connection attemps, let the communication exception bubble up.
        """


@attrs(kw_only=True, auto_attribs=True)
class NoRetryJsonSelector(JidType, hint="Coveo.CmfAdmin.NoRetryJsonSelector"):
    """

    Attributes:
        lookup_field: The field in the json structure to lookup
        expected_value: The value for which this selector will trigger
    """

    lookup_field: Opt[str] = None
    expected_value: Opt[str] = None

    def __init__(self, *, lookup_field: Opt[str] = None, expected_value: Opt[str] = None) -> None:
        """

        Parameters:
            lookup_field: The field in the json structure to lookup
            expected_value: The value for which this selector will trigger
        """


@attrs(kw_only=True, auto_attribs=True)
class ProxyAbortFromJsonStrategy(ProxyStrategy, hint="Coveo.CmfAdmin.ProxyAbortFromJsonStrategy"):
    """A structure that represents a communication proxy abort strategy.

    Attributes:
        no_retry_json_selectors: The json selector that the strategy will abort on without retrying.
    """

    no_retry_json_selectors: Opt[List[NoRetryJsonSelector]] = None

    def __init__(self, *, no_retry_json_selectors: Opt[List[NoRetryJsonSelector]] = None) -> None:
        """

        Parameters:
            no_retry_json_selectors: The json selector that the strategy will abort on without retrying.
        """


@attrs(kw_only=True, auto_attribs=True)
class ProxyFailoverStrategy(ProxyStrategy, hint="Coveo.CmfAdmin.ProxyFailoverStrategy"):
    """A structure that represents a communication proxy failover strategy.

    Attributes:
        alternate_uris: Round-robin through these servers upon a failed connection.
        max_nb_tries: After this many failed connection attemps, let the communication exception bubble up.
    """

    alternate_uris: Opt[List[str]] = None
    max_nb_tries: Opt[int] = None

    def __init__(self, *, alternate_uris: Opt[List[str]] = None, max_nb_tries: Opt[int] = None) -> None:
        """

        Parameters:
            alternate_uris: Round-robin through these servers upon a failed connection.
            max_nb_tries: After this many failed connection attemps, let the communication exception bubble up.
        """


@attrs(kw_only=True, auto_attribs=True)
class ServerStrategy(BaseStrategy, hint="Coveo.CmfAdmin.ServerStrategy"):
    """A structure that represents a communication server strategy."""

    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ServerSslStrategy(ServerStrategy, hint="Coveo.CmfAdmin.ServerSslStrategy"):
    """A structure that represents a communication server SSL strategy.

    Attributes:
        certificate: The certificate. Either in base64 form, or a filename.
        certificate_private_key: The certificate private key. Either in base64 form, or a filename.
        certificate_chain: The certificate chain. Either in base64 form, or a filename.
        trusted_cas: The trusted CAs. Either in base64 form, or a filename.
        ca_certificate_private_key: The CA certificate private key. Either in base64 form, or a filename.
        cipher: The cipher name.
    """

    certificate: Opt[str] = None
    certificate_private_key: Opt[str] = None
    certificate_chain: Opt[str] = None
    trusted_cas: Opt[str] = attrib(default=None, metadata={CASING: "TrustedCAs"})
    ca_certificate_private_key: Opt[str] = attrib(default=None, metadata={CASING: "CACertificatePrivateKey"})
    cipher: Opt[str] = None

    def __init__(
        self,
        *,
        certificate: Opt[str] = None,
        certificate_private_key: Opt[str] = None,
        certificate_chain: Opt[str] = None,
        trusted_cas: Opt[str] = attrib(default=None, metadata={CASING: "TrustedCAs"}),
        ca_certificate_private_key: Opt[str] = attrib(default=None, metadata={CASING: "CACertificatePrivateKey"}),
        cipher: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            certificate: The certificate. Either in base64 form, or a filename.
            certificate_private_key: The certificate private key. Either in base64 form, or a filename.
            certificate_chain: The certificate chain. Either in base64 form, or a filename.
            trusted_cas: The trusted CAs. Either in base64 form, or a filename.
            ca_certificate_private_key: The CA certificate private key. Either in base64 form, or a filename.
            cipher: The cipher name.
        """


@attrs(kw_only=True, auto_attribs=True)
class QueueThrottlingStrategy(BaseStrategy, hint="Coveo.CmfAdmin.QueueThrottlingStrategy"):
    """A structure that represents a communication queue throttling strategy.

    Attributes:
        fetch_stats_every_s: How many seconds before we refresh queue stats.
        fetch_bindings_every_s: How many seconds to refresh the bindings if we throttle on an exchange.
        max_size: The targeted max queue size.
        use_total_message_count: If true checks total message count instead of ready message count in rabbit.
        start_throttling_at_percent: At what % of MaxSize do we start throttling.
        max_sleep_time_ms: Sleep at most that many milliseconds, even when MaxSize has been reached.
        alternate_queue_uri: The alternate queue to use instead of the one from the current proxy.
        use_secure_admin: Whether or not to use SSL when talking to the queue admin
    """

    fetch_stats_every_s: int = attrib(default=5, metadata={CASING: "FetchStatsEvery_s"})
    fetch_bindings_every_s: int = attrib(default=30, metadata={CASING: "FetchBindingsEvery_s"})
    max_size: Opt[int] = None
    use_total_message_count: Opt[bool] = None
    start_throttling_at_percent: int = 100
    max_sleep_time_ms: Opt[int] = attrib(default=None, metadata={CASING: "MaxSleepTime_ms"})
    alternate_queue_uri: Opt[str] = attrib(default=None, metadata={CASING: "AlternateQueueURI"})
    use_secure_admin: Opt[str] = None

    def __init__(
        self,
        *,
        fetch_stats_every_s: int = attrib(default=5, metadata={CASING: "FetchStatsEvery_s"}),
        fetch_bindings_every_s: int = attrib(default=30, metadata={CASING: "FetchBindingsEvery_s"}),
        max_size: Opt[int] = None,
        use_total_message_count: Opt[bool] = None,
        start_throttling_at_percent: int = 100,
        max_sleep_time_ms: Opt[int] = attrib(default=None, metadata={CASING: "MaxSleepTime_ms"}),
        alternate_queue_uri: Opt[str] = attrib(default=None, metadata={CASING: "AlternateQueueURI"}),
        use_secure_admin: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            fetch_stats_every_s: How many seconds before we refresh queue stats.
            fetch_bindings_every_s: How many seconds to refresh the bindings if we throttle on an exchange.
            max_size: The targeted max queue size.
            use_total_message_count: If true checks total message count instead of ready message count in rabbit.
            start_throttling_at_percent: At what % of MaxSize do we start throttling.
            max_sleep_time_ms: Sleep at most that many milliseconds, even when MaxSize has been reached.
            alternate_queue_uri: The alternate queue to use instead of the one from the current proxy.
            use_secure_admin: Whether or not to use SSL when talking to the queue admin
        """


@attrs(kw_only=True, auto_attribs=True)
class ConsumerRetryStrategy(ServerStrategy, hint="Coveo.CmfAdmin.ConsumerRetryStrategy"):
    """A structure that represents a communication consumer retry strategy.

    Attributes:
        time_before_retry_ms: After a failed connection attempt, wait that many milliseconds before attempting to connect again.
    """

    time_before_retry_ms: Opt[int] = attrib(default=None, metadata={CASING: "TimeBeforeRetry_ms"})

    def __init__(
        self, *, time_before_retry_ms: Opt[int] = attrib(default=None, metadata={CASING: "TimeBeforeRetry_ms"})
    ) -> None:
        """

        Parameters:
            time_before_retry_ms: After a failed connection attempt, wait that many milliseconds before attempting to connect again.
        """


@attrs(kw_only=True, auto_attribs=True)
class OauthHeaderInjectorStrategy(ProxyStrategy, hint="Coveo.CmfAdmin.OauthHeaderInjectorStrategy"):
    """A structure that represents an oauth header injector proxy strategy.

    Attributes:
        auth_server_endpoint: Where to ask a token from.
        auth_server_client_id: Client id to use when asking for a token.
        auth_server_client_secret: Client secret to use when asking for a token.
        header: The header where the token is injected.
    """

    auth_server_endpoint: Opt[str] = None
    auth_server_client_id: Opt[str] = None
    auth_server_client_secret: Opt[str] = None
    header: str = "Authorization"

    def __init__(
        self,
        *,
        auth_server_endpoint: Opt[str] = None,
        auth_server_client_id: Opt[str] = None,
        auth_server_client_secret: Opt[str] = None,
        header: str = "Authorization",
    ) -> None:
        """

        Parameters:
            auth_server_endpoint: Where to ask a token from.
            auth_server_client_id: Client id to use when asking for a token.
            auth_server_client_secret: Client secret to use when asking for a token.
            header: The header where the token is injected.
        """


@attrs(kw_only=True, auto_attribs=True)
class SqsParameters(JidType, hint="Coveo.CmfAdmin.SqsParameters"):
    """The parameters needed to handle a SQS queue proxy/server.

    Attributes:
        bucket_name: The S3 bucket name to use for big SQS payloads. Ex: 'coveo-ndev-customerdata'.
        bucket_key_prefix: The S3 bucket key prefix (before the generated guid). Ex: 'develop/blobstore/0000-sqs-'.
        always_use_s3: Should we unconditionally write SQS payloads to S3 ? Default is only if size > 250K.
    """

    bucket_name: Opt[str] = None
    bucket_key_prefix: Opt[str] = None
    always_use_s3: Opt[bool] = None

    def __init__(
        self, *, bucket_name: Opt[str] = None, bucket_key_prefix: Opt[str] = None, always_use_s3: Opt[bool] = None
    ) -> None:
        """

        Parameters:
            bucket_name: The S3 bucket name to use for big SQS payloads. Ex: 'coveo-ndev-customerdata'.
            bucket_key_prefix: The S3 bucket key prefix (before the generated guid). Ex: 'develop/blobstore/0000-sqs-'.
            always_use_s3: Should we unconditionally write SQS payloads to S3 ? Default is only if size > 250K.
        """


@attrs(kw_only=True, auto_attribs=True)
class CmfConfig(JidType, hint="Coveo.CmfAdmin.CmfConfig"):
    """A structure that represents a Cmf configuration.

    Attributes:
        call_tracker_retention_period: Retention period in minutes when a call is done.
        graphite_url: Ex.1: tcp://localhost:2003, Ex.2: https://www.hostedgraphite.com/api/v1/sink
        graphite_api_key: Only needed for HostedGraphite.
        graphite_prefix: All metrics will be prefixed by this.
        graphite_blacklist_regex: Metrics matching this regex will be filtered out.
        credentials: User & pwd for various servers
        message_routing_service_uri: The message routing service uri
        sqs_parameters: The optional SQS parameters.
        swagger_authorization_uri: The uri to use for oauth authorization from swagger.
    """

    uri_matchers: Opt[List[UriMatcher]] = None
    strategies: Opt[List[BaseStrategy]] = None
    uri_aliases: Opt[List[UriAlias]] = None
    strategy_lists: Opt[List[StrategyList]] = None
    status_tracker_uri: Opt[str] = None
    metric_aggregator_uri: Opt[str] = None
    redis_uri: Opt[str] = None
    call_tracker_uri: Opt[str] = None
    call_tracker_retention_period: int = 60
    graphite_url: Opt[str] = None
    graphite_api_key: Opt[str] = None
    graphite_prefix: Opt[str] = None
    graphite_blacklist_regex: Opt[str] = None
    credentials: Opt[Dict[str, Credential]] = None
    message_routing_service_uri: Opt[str] = None
    sqs_parameters: Opt[SqsParameters] = None
    swagger_authorization_uri: Opt[str] = None

    def __init__(
        self,
        *,
        uri_matchers: Opt[List[UriMatcher]] = None,
        strategies: Opt[List[BaseStrategy]] = None,
        uri_aliases: Opt[List[UriAlias]] = None,
        strategy_lists: Opt[List[StrategyList]] = None,
        status_tracker_uri: Opt[str] = None,
        metric_aggregator_uri: Opt[str] = None,
        redis_uri: Opt[str] = None,
        call_tracker_uri: Opt[str] = None,
        call_tracker_retention_period: int = 60,
        graphite_url: Opt[str] = None,
        graphite_api_key: Opt[str] = None,
        graphite_prefix: Opt[str] = None,
        graphite_blacklist_regex: Opt[str] = None,
        credentials: Opt[Dict[str, Credential]] = None,
        message_routing_service_uri: Opt[str] = None,
        sqs_parameters: Opt[SqsParameters] = None,
        swagger_authorization_uri: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            call_tracker_retention_period: Retention period in minutes when a call is done.
            graphite_url: Ex.1: tcp://localhost:2003, Ex.2: https://www.hostedgraphite.com/api/v1/sink
            graphite_api_key: Only needed for HostedGraphite.
            graphite_prefix: All metrics will be prefixed by this.
            graphite_blacklist_regex: Metrics matching this regex will be filtered out.
            credentials: User & pwd for various servers
            message_routing_service_uri: The message routing service uri
            sqs_parameters: The optional SQS parameters.
            swagger_authorization_uri: The uri to use for oauth authorization from swagger.
        """


@attrs(kw_only=True, auto_attribs=True)
class ProcessInfo(JidType, hint="Coveo.CmfAdmin.ProcessInfo"):
    """A structure that represents information about the process hosting the target Cmf admin server."""

    machine: Opt[str] = None
    pid: Opt[int] = None
    command_line: Opt[str] = None
    name: Opt[str] = None
    better_name: Opt[str] = None
    args: Opt[List[str]] = None
    user: Opt[str] = None
    working_dir: Opt[str] = None
    build_date: Opt[str] = None
    file_version: Opt[str] = None
    now: Opt[datetime] = None

    def __init__(
        self,
        *,
        machine: Opt[str] = None,
        pid: Opt[int] = None,
        command_line: Opt[str] = None,
        name: Opt[str] = None,
        better_name: Opt[str] = None,
        args: Opt[List[str]] = None,
        user: Opt[str] = None,
        working_dir: Opt[str] = None,
        build_date: Opt[str] = None,
        file_version: Opt[str] = None,
        now: Opt[datetime] = None,
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ServedCall(JidType, hint="Coveo.CmfAdmin.ServedCall"):
    """A structure that describes a call being served.

    Attributes:
        servant: The name of the servant.
        time_started: The time the call was dispatched.
        method: The method name (because the arguments don't contain the _type).
        arguments: The whole call arguments as Json.
    """

    servant: Opt[str] = None
    time_started: Opt[datetime] = None
    method: Opt[str] = None
    arguments: Opt[str] = None

    def __init__(
        self,
        *,
        servant: Opt[str] = None,
        time_started: Opt[datetime] = None,
        method: Opt[str] = None,
        arguments: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            servant: The name of the servant.
            time_started: The time the call was dispatched.
            method: The method name (because the arguments don't contain the _type).
            arguments: The whole call arguments as Json.
        """


@attrs(kw_only=True, auto_attribs=True)
class ProxiedCall(JidType, hint="Coveo.CmfAdmin.ProxiedCall"):
    """A structure that describes a call being proxied.

    Attributes:
        uri: The target uri.
        time_started: The time the call was dispatched.
        method: The method name (because the arguments don't contain the _type).
        arguments: The whole call arguments as Json.
    """

    uri: Opt[str] = None
    time_started: Opt[datetime] = None
    method: Opt[str] = None
    arguments: Opt[str] = None

    def __init__(
        self,
        *,
        uri: Opt[str] = None,
        time_started: Opt[datetime] = None,
        method: Opt[str] = None,
        arguments: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            uri: The target uri.
            time_started: The time the call was dispatched.
            method: The method name (because the arguments don't contain the _type).
            arguments: The whole call arguments as Json.
        """


class ICmfServer(CoveoInterface):
    """The ICmfServer interface exposes methods to retrieve information about the status and capabilities of communication servers."""

    @api("GET/ping")
    def ping(self) -> None:
        """Pings the server. The call only returns if the ping is acknowledged."""

    @api("GET/process_info")
    def get_process_info(self) -> ProcessInfo:
        """Returns information on the process hosting this CmfAdminServer."""

    @api("GET/servers")
    def get_servers(self) -> List[ServerInfo]:
        """Returns the list of communication servers."""

    @api("GET/proxies")
    def get_proxies(self) -> List[ProxyInfo]:
        """Returns the list of communication proxies."""

    @api("GET/channels")
    def get_channels(self) -> List[ChannelInfo]:
        """Returns the list of ChannelManager channels (pre-Cmf)."""

    @api("GET/strategy_types")
    def get_strategy_types(self) -> List[StrategyType]:
        """Returns the list of available strategy types."""

    @api("GET/configuration")
    def get_config(self) -> CmfConfig:
        """Returns the CmfConfig."""

    @api("PUT/configuration")
    def set_config(self, *, config: CmfConfig, str_config: str) -> None:
        """Sets the uri aliases, matchers and strategies all at once."""

    @api("POST/load_metamodule")
    def load_meta_module(self, *, dll_path: str) -> str:
        """Load a meta-module to the process, allowing de/encoding of sub-classes."""

    @api("POST/set_nb_consuming_threads")
    def set_nb_consuming_threads(self, *, server_uri: str, servant_name: str, nb_threads: int) -> None:
        """Sets the number of threads consuming from a queue."""

    @api("GET/served_calls")
    def get_served_calls(self) -> List[ServedCall]:
        """Gets the list of active calls in all servants."""

    @api("GET/proxied_calls")
    def get_proxied_calls(self) -> List[ProxiedCall]:
        """Gets the list of active calls in all messengers."""

    @api("GET/tracked_calls")
    def get_tracked_calls(self) -> List[CallProgress]:
        """Returns a CallProgress for all tracked calls with up-to-date progress information."""

    @api("GET/tracked_calls/{call_id}")
    def get_tracked_call(self, *, call_id: str) -> CallProgress:
        """Returns a CallProgress with up-to-date progress information for the given call.

        Parameters:
            call_id: The Id of a call.
        """

    @api("POST/tracked_calls/{call_id}/cancel")
    def cancel_tracked_call(self, *, call_id: str) -> None:
        """Cancel a tracked call.

        Parameters:
            call_id: The Id of a tracked call.
        """

    @api("POST/tracked_calls/{call_id}/suspend")
    def suspend_tracked_call(self, *, call_id: str) -> None:
        """Suspend a tracked call.

        Parameters:
            call_id: The Id of a tracked call.
        """

    @api("POST/tracked_calls/{call_id}/resume")
    def resume_tracked_call(self, *, call_id: str) -> None:
        """Resume a tracked call.

        Parameters:
            call_id: The Id of an async call.
        """

    @api("PUT/call_tracker_uri")
    def set_call_tracker_uri(self, *, call_tracker_uri: str) -> None:
        """Sets the call tracker uri where detailed call sending/handling will be sent. Null or empty to stop sending data."""

    @api("GET/nb_long_calls")
    def get_nb_long_calls(self, *, threshold: int = 3600) -> int:
        """Gets the number of calls (served and proxied) started for more than Threshold seconds."""


@attrs(kw_only=True, auto_attribs=True)
class LoggerInfo(JidType, hint="Coveo.CmfAdmin.LoggerInfo"):
    logger_name: Opt[str] = None
    logger_level: Opt[str] = None
    appenders: Opt[List[str]] = None

    def __init__(
        self, *, logger_name: Opt[str] = None, logger_level: Opt[str] = None, appenders: Opt[List[str]] = None
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidAppenderNameException(ExceptionBase, hint="Coveo.CmfAdmin.InvalidAppenderNameException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class EmptyAppenderNameException(InvalidAppenderNameException, hint="Coveo.CmfAdmin.EmptyAppenderNameException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidLoggingLevelException(ExceptionBase, hint="Coveo.CmfAdmin.InvalidLoggingLevelException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidLoggerNameException(ExceptionBase, hint="Coveo.CmfAdmin.InvalidLoggerNameException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidLoggingConfigException(ExceptionBase, hint="Coveo.CmfAdmin.InvalidLoggingConfigException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class CannotOpenConfigFileExeption(ExceptionBase, hint="Coveo.CmfAdmin.CannotOpenConfigFileExeption"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class EmptyLoggingConfigException(InvalidLoggingConfigException, hint="Coveo.CmfAdmin.EmptyLoggingConfigException"):
    def __init__(self) -> None:
        ...


class ILogManager(CoveoInterface):
    """The ILogManager interface is used to manage the logging"""

    @api("GET/log_manager/loggers")
    def get_all_loggers_info(self) -> List[LoggerInfo]:
        ...

    @api("GET/log_manager/loggers/{logger_name}")
    def get_logger_info(self, *, logger_name: str) -> LoggerInfo:
        ...

    @api("POST/log_manager/loggers/{logger_name}", logging_duration_s="LoggingDuration_s")
    def set_logging_level(self, *, logger_name: str, logging_level: str, logging_duration_s: int = 300) -> None:
        ...

    @api("GET/log_manager/appenders")
    def get_all_appenders(self) -> List[str]:
        ...

    @api("POST/log_manager/loggers/{logger_name}/appenders")
    def add_logger_appender(self, *, logger_name: str, appender_name: str) -> None:
        ...

    @api("DELETE/log_manager/loggers/{logger_name}/appenders/{appender_name}")
    def remove_logger_appender(self, *, logger_name: str, appender_name: str) -> None:
        ...

    @api("DELETE/log_manager/loggers/{logger_name}/appenders")
    def remove_all_logger_appenders(self, *, logger_name: str) -> None:
        ...

    @api("POST/log_manager/disable_all_loggers")
    def disable_all_loggers(self) -> None:
        ...

    @api("POST/log_manager/restore_loggers_default")
    def restore_default(self) -> None:
        ...

    @api("PUT/log_manager/config/file")
    def set_file_configuration(self, *, configuration: str) -> None:
        ...

    @api("GET/log_manager/config/file")
    def get_file_configuration(self) -> str:
        ...
