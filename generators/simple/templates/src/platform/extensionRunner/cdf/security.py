"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/CoveoSecurityCache.jid

"""

from attr import attrib, attrs
from datetime import datetime
from enum import auto
from typing import List, Optional as Opt, Union
from .root import CASING, CoveoInterface, ExceptionBase, JidEnumFlag, JidType, MultiOut, api
from .job_service import JobHandlerType
from .security_provider import Information, SID, SIDDeclarator, SecurityProviderConfig
from .document_definition import PermissionModel, PermissionSet, SecurityIdentity
from .tracking import MetricEntry, StatusEntry


@attrs(kw_only=True, auto_attribs=True)
class SecurityCacheException(ExceptionBase, hint="Coveo.SecurityCacheException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityCacheUninitializedException(SecurityCacheException, hint="Coveo.SecurityCacheUninitializedException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityCacheAlreadyInitializedException(
    SecurityCacheException, hint="Coveo.SecurityCacheAlreadyInitializedException"
):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityCacheNotStartedException(SecurityCacheException, hint="Coveo.SecurityCacheNotStartedException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityCacheAlreadyStartedException(SecurityCacheException, hint="Coveo.SecurityCacheAlreadyStartedException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityCacheShuttingDownException(SecurityCacheException, hint="Coveo.SecurityCacheShuttingDownException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityCacheConfigNotSetException(SecurityCacheException, hint="Coveo.SecurityCacheConfigNotSetException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityCacheUnavailableException(SecurityCacheException, hint="Coveo.SecurityCacheUnavailableException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityCacheInvalidConfigurationException(
    SecurityCacheException, hint="Coveo.SecurityCacheInvalidConfigurationException"
):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityCacheInvalidOperationException(
    SecurityCacheException, hint="Coveo.SecurityCacheInvalidOperationException"
):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityCacheInvalidPermissionModelException(
    SecurityCacheException, hint="Coveo.SecurityCacheInvalidPermissionModelException"
):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityCacheProviderInaccessibleException(
    SecurityCacheException, hint="Coveo.SecurityCacheProviderInaccessibleException"
):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityCacheInvalidListingOptionsException(
    SecurityCacheException, hint="Coveo.SecurityCacheInvalidListingOptionsException"
):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityCacheUnknownEntityException(SecurityCacheException, hint="Coveo.SecurityCacheUnknownEntityException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityProviderRegistryInfo(JidType, hint="Coveo.SecurityProviderRegistryInfo"):
    """

    Attributes:
        name: Name of the security provider
        uri: Uri of the security provider
        synchronized_expansion: Whether the security provider support synchronized expansion.
        is_case_sensitive: Whether the security provider is case sensitive.
        is_using_job_service: Whether the security provider should be used as a service.
        handler_type: The type of the job service handler for the security provider.
        organization_id: Usused. Deprecated by SecurityConfig.OrganizationClusterId
        provider_id: The security provider identifier.
        provider_type: The security provider type.
        max_batch_size: The maximum number of entities a JobService job can contain. 0 means no maximum value.
        max_batch_size_in_bytes: The maximum size of entities a JobService job can contain, in bytes. 0 means no maximum value.
        timeout_ms: Deprecated; Use GetParentEntityIDsTimeout_ms
        get_parent_entities_timeout_ms: Number of milliseconds to wait for results when contacting provider to retrieve parent entities.
        update_entities_timeout_ms: Number of milliseconds to wait for results when contacting provider to update entities (default: 12h).
        is_creating_jobs_for_not_updated_entities_enabled: Whether jobs should be created when the security cache finds a non updated entity.
        config: The security provider configuration.
    """

    name: Opt[str] = None
    uri: Opt[str] = None
    synchronized_expansion: bool = True
    is_case_sensitive: Opt[bool] = None
    is_using_job_service: Opt[bool] = None
    handler_type: Opt[JobHandlerType] = None
    organization_id: Opt[str] = None
    provider_id: Opt[str] = None
    provider_type: Opt[str] = None
    max_batch_size: int = 1000
    max_batch_size_in_bytes: Opt[int] = None
    timeout_ms: int = attrib(default=5000, metadata={CASING: "Timeout_ms"})
    get_parent_entities_timeout_ms: int = attrib(default=5000, metadata={CASING: "GetParentEntitiesTimeout_ms"})
    update_entities_timeout_ms: int = attrib(default=43200000, metadata={CASING: "UpdateEntitiesTimeout_ms"})
    is_creating_jobs_for_not_updated_entities_enabled: bool = True
    config: Opt[SecurityProviderConfig] = None

    def __init__(
        self,
        *,
        name: Opt[str] = None,
        uri: Opt[str] = None,
        synchronized_expansion: bool = True,
        is_case_sensitive: Opt[bool] = None,
        is_using_job_service: Opt[bool] = None,
        handler_type: Opt[JobHandlerType] = None,
        organization_id: Opt[str] = None,
        provider_id: Opt[str] = None,
        provider_type: Opt[str] = None,
        max_batch_size: int = 1000,
        max_batch_size_in_bytes: Opt[int] = None,
        timeout_ms: int = attrib(default=5000, metadata={CASING: "Timeout_ms"}),
        get_parent_entities_timeout_ms: int = attrib(default=5000, metadata={CASING: "GetParentEntitiesTimeout_ms"}),
        update_entities_timeout_ms: int = attrib(default=43200000, metadata={CASING: "UpdateEntitiesTimeout_ms"}),
        is_creating_jobs_for_not_updated_entities_enabled: bool = True,
        config: Opt[SecurityProviderConfig] = None,
    ) -> None:
        """

        Parameters:
            name: Name of the security provider
            uri: Uri of the security provider
            synchronized_expansion: Whether the security provider support synchronized expansion.
            is_case_sensitive: Whether the security provider is case sensitive.
            is_using_job_service: Whether the security provider should be used as a service.
            handler_type: The type of the job service handler for the security provider.
            organization_id: Usused. Deprecated by SecurityConfig.OrganizationClusterId
            provider_id: The security provider identifier.
            provider_type: The security provider type.
            max_batch_size: The maximum number of entities a JobService job can contain. 0 means no maximum value.
            max_batch_size_in_bytes: The maximum size of entities a JobService job can contain, in bytes. 0 means no maximum value.
            timeout_ms: Deprecated; Use GetParentEntityIDsTimeout_ms
            get_parent_entities_timeout_ms: Number of milliseconds to wait for results when contacting provider to retrieve parent entities.
            update_entities_timeout_ms: Number of milliseconds to wait for results when contacting provider to update entities (default: 12h).
            is_creating_jobs_for_not_updated_entities_enabled: Whether jobs should be created when the security cache finds a non updated entity.
            config: The security provider configuration.
        """


@attrs(kw_only=True, auto_attribs=True)
class CPUCoresUsageConfig(JidType, hint="Coveo.CPUCoresUsageConfig"):
    """Config specifying how many CPU cores to use for a process.

    Attributes:
        ratio: Ratio of the total number of cores to use. Must be 0 < value <= 1. 0 means unspecified.
        count: Fixed number of cores to use. Must be > 0. 0 means unspecified.
    """

    ratio: Opt[float] = None
    count: Opt[int] = None

    def __init__(self, *, ratio: Opt[float] = None, count: Opt[int] = None) -> None:
        """

        Parameters:
            ratio: Ratio of the total number of cores to use. Must be 0 < value <= 1. 0 means unspecified.
            count: Fixed number of cores to use. Must be > 0. 0 means unspecified.
        """


@attrs(kw_only=True, auto_attribs=True)
class SecurityConfig(JidType, hint="Coveo.SecurityConfig"):
    """Config for a security blade.

    Attributes:
        organization_id: The global organization Id.
        organization_cluster_id: The global organization cluster Id.
        is_job_processing_enabled: Whether job messages should be retrieved and processed.
        job_queue_uri: The Uri of the job queue, used to publish security blade jobs.
        job_service_uri: The Uri of the job service, used to publish security provider jobs.
        is_sync_processing_enabled: Whether sync messages should be retrieved and processed.
        sync_queue_uri: The Uri of the sync queue, used to publish syncs.
        permission_models_update_delay_ms: The delay, in milliseconds, used between update of permission models.
        permission_models_update_throttle_max_delay_s: The maximum allowed delay, in seconds, to throttle the update of permission models.
        permission_models_update_throttle_min_msg_count: The minimum number of sync messages to trigger a throttle of the update of permission models.
        permission_models_update_cpu_cores_usage: The config specifying how many CPU cores to use to update permission models.
        queue_stats_fetching_min_delay_s: The minimum allowed delay, in seconds, between each queue stats query call.
        commit_delay_s: The delay, in seconds, used between commits.
        commit_batch_limit: The maximum number of unacked messages to tolerate before committing.
        status_update_frequency_s: The delay, in seconds, used between information and operation statuses are generated.
        operation_expiration_delay_s: The delay, in seconds, before an operation stops to generate operation statuses after the last time it was updated.
        is_publishing_metrics: Whether the security cache should publish metrics.
        security_providers: The security providers
        security_providers_max_wait_delay_ms: The maximum delay, in milliseconds, before aborting a security provider call when a blade reboot or shutdown is required.
        job_processor_forwarder_lru_cache_max_size: The maximum number of mega bytes the JobProcessorForwarder entity LRU cache may use. Use '0' to disable this feature.
        security_store_service_uri: The Uri of the SecurityStoreService.
        is_not_updated_entities_notif_enabled: Whether NotUpdated entities notifications are sent.
        not_updated_entities_notif_ignore_delay_ms: The delay, in milliseconds, for which NotUpdated entities notifications are not sent after another one is sent.
        max_batch_size: The maximum number of entities a message can contain. 0 means no maximum value.
        max_batch_size_in_bytes: The maximum size of entities a message can contain, in bytes. 0 means no maximum value.
    """

    organization_id: Opt[str] = None
    organization_cluster_id: Opt[str] = None
    is_job_processing_enabled: bool = True
    job_queue_uri: Opt[str] = None
    job_service_uri: Opt[str] = None
    is_sync_processing_enabled: bool = True
    sync_queue_uri: Opt[str] = None
    permission_models_update_delay_ms: int = attrib(default=5000, metadata={CASING: "PermissionModelsUpdateDelay_ms"})
    permission_models_update_throttle_max_delay_s: int = attrib(
        default=600, metadata={CASING: "PermissionModelsUpdateThrottleMaxDelay_s"}
    )
    permission_models_update_throttle_min_msg_count: int = 100
    permission_models_update_cpu_cores_usage: Opt[CPUCoresUsageConfig] = attrib(
        default=None, metadata={CASING: "PermissionModelsUpdateCPUCoresUsage"}
    )
    queue_stats_fetching_min_delay_s: int = attrib(default=30, metadata={CASING: "QueueStatsFetchingMinDelay_s"})
    commit_delay_s: int = attrib(default=300, metadata={CASING: "CommitDelay_s"})
    commit_batch_limit: int = 10000
    status_update_frequency_s: int = attrib(default=5, metadata={CASING: "StatusUpdateFrequency_s"})
    operation_expiration_delay_s: int = attrib(default=3600, metadata={CASING: "OperationExpirationDelay_s"})
    is_publishing_metrics: Opt[bool] = None
    security_providers: Opt[List[SecurityProviderRegistryInfo]] = None
    security_providers_max_wait_delay_ms: int = attrib(
        default=5000, metadata={CASING: "SecurityProvidersMaxWaitDelay_ms"}
    )
    job_processor_forwarder_lru_cache_max_size: int = attrib(
        default=512, metadata={CASING: "JobProcessorForwarderLRUCacheMaxSize"}
    )
    security_store_service_uri: Opt[str] = None
    is_not_updated_entities_notif_enabled: bool = True
    not_updated_entities_notif_ignore_delay_ms: int = attrib(
        default=2000, metadata={CASING: "NotUpdatedEntitiesNotifIgnoreDelay_ms"}
    )
    max_batch_size: int = 1000
    max_batch_size_in_bytes: int = 1048576

    def __init__(
        self,
        *,
        organization_id: Opt[str] = None,
        organization_cluster_id: Opt[str] = None,
        is_job_processing_enabled: bool = True,
        job_queue_uri: Opt[str] = None,
        job_service_uri: Opt[str] = None,
        is_sync_processing_enabled: bool = True,
        sync_queue_uri: Opt[str] = None,
        permission_models_update_delay_ms: int = attrib(
            default=5000, metadata={CASING: "PermissionModelsUpdateDelay_ms"}
        ),
        permission_models_update_throttle_max_delay_s: int = attrib(
            default=600, metadata={CASING: "PermissionModelsUpdateThrottleMaxDelay_s"}
        ),
        permission_models_update_throttle_min_msg_count: int = 100,
        permission_models_update_cpu_cores_usage: Opt[CPUCoresUsageConfig] = attrib(
            default=None, metadata={CASING: "PermissionModelsUpdateCPUCoresUsage"}
        ),
        queue_stats_fetching_min_delay_s: int = attrib(default=30, metadata={CASING: "QueueStatsFetchingMinDelay_s"}),
        commit_delay_s: int = attrib(default=300, metadata={CASING: "CommitDelay_s"}),
        commit_batch_limit: int = 10000,
        status_update_frequency_s: int = attrib(default=5, metadata={CASING: "StatusUpdateFrequency_s"}),
        operation_expiration_delay_s: int = attrib(default=3600, metadata={CASING: "OperationExpirationDelay_s"}),
        is_publishing_metrics: Opt[bool] = None,
        security_providers: Opt[List[SecurityProviderRegistryInfo]] = None,
        security_providers_max_wait_delay_ms: int = attrib(
            default=5000, metadata={CASING: "SecurityProvidersMaxWaitDelay_ms"}
        ),
        job_processor_forwarder_lru_cache_max_size: int = attrib(
            default=512, metadata={CASING: "JobProcessorForwarderLRUCacheMaxSize"}
        ),
        security_store_service_uri: Opt[str] = None,
        is_not_updated_entities_notif_enabled: bool = True,
        not_updated_entities_notif_ignore_delay_ms: int = attrib(
            default=2000, metadata={CASING: "NotUpdatedEntitiesNotifIgnoreDelay_ms"}
        ),
        max_batch_size: int = 1000,
        max_batch_size_in_bytes: int = 1048576,
    ) -> None:
        """

        Parameters:
            organization_id: The global organization Id.
            organization_cluster_id: The global organization cluster Id.
            is_job_processing_enabled: Whether job messages should be retrieved and processed.
            job_queue_uri: The Uri of the job queue, used to publish security blade jobs.
            job_service_uri: The Uri of the job service, used to publish security provider jobs.
            is_sync_processing_enabled: Whether sync messages should be retrieved and processed.
            sync_queue_uri: The Uri of the sync queue, used to publish syncs.
            permission_models_update_delay_ms: The delay, in milliseconds, used between update of permission models.
            permission_models_update_throttle_max_delay_s: The maximum allowed delay, in seconds, to throttle the update of permission models.
            permission_models_update_throttle_min_msg_count: The minimum number of sync messages to trigger a throttle of the update of permission models.
            permission_models_update_cpu_cores_usage: The config specifying how many CPU cores to use to update permission models.
            queue_stats_fetching_min_delay_s: The minimum allowed delay, in seconds, between each queue stats query call.
            commit_delay_s: The delay, in seconds, used between commits.
            commit_batch_limit: The maximum number of unacked messages to tolerate before committing.
            status_update_frequency_s: The delay, in seconds, used between information and operation statuses are generated.
            operation_expiration_delay_s: The delay, in seconds, before an operation stops to generate operation statuses after the last time it was updated.
            is_publishing_metrics: Whether the security cache should publish metrics.
            security_providers: The security providers
            security_providers_max_wait_delay_ms: The maximum delay, in milliseconds, before aborting a security provider call when a blade reboot or shutdown is required.
            job_processor_forwarder_lru_cache_max_size: The maximum number of mega bytes the JobProcessorForwarder entity LRU cache may use. Use '0' to disable this feature.
            security_store_service_uri: The Uri of the SecurityStoreService.
            is_not_updated_entities_notif_enabled: Whether NotUpdated entities notifications are sent.
            not_updated_entities_notif_ignore_delay_ms: The delay, in milliseconds, for which NotUpdated entities notifications are not sent after another one is sent.
            max_batch_size: The maximum number of entities a message can contain. 0 means no maximum value.
            max_batch_size_in_bytes: The maximum size of entities a message can contain, in bytes. 0 means no maximum value.
        """


class ISecurityAdmin(CoveoInterface):
    """API is used to manage and configure the security blade"""

    @api("POST/providers")
    def add_provider(self, *, security_provider: SecurityProviderRegistryInfo) -> None:
        """Adds a security provider.

        Parameters:
            security_provider: A security provider configuration.
        """

    @api("DELETE/providers/{provider_name}")
    def remove_provider(self, *, provider_name: str) -> None:
        """Removes a security provider.

        Parameters:
            provider_name: The name of a security provider.
        """

    @api("GET/providers/{provider_name}")
    def get_provider_information(self, *, provider_name: str) -> Information:
        """Returns information about a security provider.

        Parameters:
            provider_name: The name of a security provider.
        """

    @api("POST/data_path")
    def set_data_path(self, *, data_path: str) -> None:
        ...

    @api("PUT/config")
    def set_config(self, *, config: SecurityConfig) -> None:
        """Sets the required configuration parameters.

        Parameters:
            config: The new configuration parameters to use.
        """

    @api("GET/config")
    def get_config(self) -> SecurityConfig:
        """Gets the current configuration parameters."""


class SecurityExpansionState(JidEnumFlag):
    NotStarted: int = auto()
    Starting: int = auto()
    WaitingForConfig: int = auto()
    Synchronizing: int = auto()
    Running: int = auto()
    InvalidConfig: int = auto()
    OutOfSync: int = auto()
    CriticalError: int = auto()
    ShuttingDown: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class EntityAndID(JidType, hint="Coveo.EntityAndID"):
    """Contains the number of security entities for a specific state.

    Attributes:
        entity: The security entity.
        id_: The unique security entity identifier.
    """

    entity: Opt[SID] = None
    id_: Opt[int] = attrib(default=None, metadata={CASING: "ID"})

    def __init__(
        self, *, entity: Opt[SID] = None, id_: Opt[int] = attrib(default=None, metadata={CASING: "ID"})
    ) -> None:
        """

        Parameters:
            entity: The security entity.
            id_: The unique security entity identifier.
        """


class EntityState(JidEnumFlag):
    Unknown: int = auto()
    UpToDate: int = auto()
    NotUpdated: int = auto()
    OutOfDate: int = auto()
    InError: int = auto()
    Disabled: int = auto()


class EntityUpdateResult(JidEnumFlag):
    None_: int = auto()
    Success: int = auto()
    AccessDenied: int = auto()
    TimedOut: int = auto()
    EntityIsInvalid: int = auto()
    EntityIsUnavailable: int = auto()
    SecurityProviderIsUnavailable: int = auto()
    SecurityProviderIsUnreachable: int = auto()
    SecurityProviderIsNotReady: int = auto()
    UnexpectedError: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class EntitiesCountForState(JidType, hint="Coveo.EntitiesCountForState"):
    """Contains the number of security entities for a specific state.

    Attributes:
        state: The security entity state.
        count: The number of security entities for the state.
    """

    state: Opt[EntityState] = None
    count: Opt[int] = None

    def __init__(self, *, state: Opt[EntityState] = None, count: Opt[int] = None) -> None:
        """

        Parameters:
            state: The security entity state.
            count: The number of security entities for the state.
        """


@attrs(kw_only=True, auto_attribs=True)
class EntitiesCountPerStateForProvider(JidType, hint="Coveo.EntitiesCountPerStateForProvider"):
    """Contains the number of security entities for a specific state for a specific provider.

    Attributes:
        provider_name: The name of the security provider.
        entities_count_per_state: The number of security entities per state for the security provider.
    """

    provider_name: Opt[str] = None
    entities_count_per_state: Opt[List[EntitiesCountForState]] = None

    def __init__(
        self, *, provider_name: Opt[str] = None, entities_count_per_state: Opt[List[EntitiesCountForState]] = None
    ) -> None:
        """

        Parameters:
            provider_name: The name of the security provider.
            entities_count_per_state: The number of security entities per state for the security provider.
        """


@attrs(kw_only=True, auto_attribs=True)
class EntityInformation(JidType, hint="Coveo.EntityInformation"):
    """Contains the information of a specific entity.

    Attributes:
        entity: The security entity.
        id_: The unique security entity identifier.
        identity: The identity (e.g. declarator) for the security entity.
        provider: The security provider of the security entity.
        declaration: The security entity string descriptor.
        state: The actual entity state.
        created_date: The date at which the entity was created.
        last_enabled_date: The date at which the entity was last enabled.
        last_update_date: The date at which the entity was last updated.
        last_successful_update_date: The date at which the entity was last successfully updated.
        last_stored_date: The date at which the entity information was stored.
        ordering_id: ID used to order entity updates.
        last_update_result: The result of the last update.
        last_update_error_detail: In the case of an unexpected error, contains some basic error details.
    """

    entity: Opt[SID] = None
    id_: Opt[int] = attrib(default=None, metadata={CASING: "ID"})
    identity: Opt[SecurityIdentity] = None
    provider: Opt[str] = None
    declaration: Opt[str] = None
    state: Opt[EntityState] = None
    created_date: Opt[datetime] = None
    last_enabled_date: Opt[datetime] = None
    last_update_date: Opt[datetime] = None
    last_successful_update_date: Opt[datetime] = None
    last_stored_date: Opt[datetime] = None
    ordering_id: Opt[int] = attrib(default=None, metadata={CASING: "OrderingID"})
    last_update_result: Opt[EntityUpdateResult] = None
    last_update_error_detail: Opt[str] = None

    def __init__(
        self,
        *,
        entity: Opt[SID] = None,
        id_: Opt[int] = attrib(default=None, metadata={CASING: "ID"}),
        identity: Opt[SecurityIdentity] = None,
        provider: Opt[str] = None,
        declaration: Opt[str] = None,
        state: Opt[EntityState] = None,
        created_date: Opt[datetime] = None,
        last_enabled_date: Opt[datetime] = None,
        last_update_date: Opt[datetime] = None,
        last_successful_update_date: Opt[datetime] = None,
        last_stored_date: Opt[datetime] = None,
        ordering_id: Opt[int] = attrib(default=None, metadata={CASING: "OrderingID"}),
        last_update_result: Opt[EntityUpdateResult] = None,
        last_update_error_detail: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            entity: The security entity.
            id_: The unique security entity identifier.
            identity: The identity (e.g. declarator) for the security entity.
            provider: The security provider of the security entity.
            declaration: The security entity string descriptor.
            state: The actual entity state.
            created_date: The date at which the entity was created.
            last_enabled_date: The date at which the entity was last enabled.
            last_update_date: The date at which the entity was last updated.
            last_successful_update_date: The date at which the entity was last successfully updated.
            last_stored_date: The date at which the entity information was stored.
            ordering_id: ID used to order entity updates.
            last_update_result: The result of the last update.
            last_update_error_detail: In the case of an unexpected error, contains some basic error details.
        """


class PermissionModelState(JidEnumFlag):
    Unknown: int = auto()
    Valid: int = auto()
    Pending: int = auto()
    Incomplete: int = auto()
    InError: int = auto()
    Disabled: int = auto()
    Warning: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class SIDPermissionSet(JidType, hint="Coveo.SIDPermissionSet"):
    """A structure that represents a collection of allowed and denied permissions as SIDs.

    Attributes:
        allow_anonymous: Indicates if anonymous users ere allowed.
        allowed_permissions: The list of allowed permissions.
        denied_permissions: The list of denied permissions.
        name: An optional permission set name.
    """

    allow_anonymous: Opt[bool] = None
    allowed_permissions: Opt[List[SID]] = None
    denied_permissions: Opt[List[SID]] = None
    name: Opt[str] = None

    def __init__(
        self,
        *,
        allow_anonymous: Opt[bool] = None,
        allowed_permissions: Opt[List[SID]] = None,
        denied_permissions: Opt[List[SID]] = None,
        name: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            allow_anonymous: Indicates if anonymous users ere allowed.
            allowed_permissions: The list of allowed permissions.
            denied_permissions: The list of denied permissions.
            name: An optional permission set name.
        """


@attrs(kw_only=True, auto_attribs=True)
class SIDPermissionLevel(JidType, hint="Coveo.SIDPermissionLevel"):
    """A structure that represents a level of permission where multiple permission sets as SIDs can be specified.

    Attributes:
        name: An optional permission level name.
    """

    permission_sets: Opt[List[SIDPermissionSet]] = None
    name: Opt[str] = None

    def __init__(self, *, permission_sets: Opt[List[SIDPermissionSet]] = None, name: Opt[str] = None) -> None:
        """

        Parameters:
            name: An optional permission level name.
        """


@attrs(kw_only=True, auto_attribs=True)
class SIDPermissionModel(JidType, hint="Coveo.SIDPermissionModel"):
    """A structure that represent a permissions model that contains one or many permission levels as SIDs."""

    permission_levels: Opt[List[SIDPermissionLevel]] = None

    def __init__(self, *, permission_levels: Opt[List[SIDPermissionLevel]] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class EntityInformationPermissionSet(JidType, hint="Coveo.EntityInformationPermissionSet"):
    """A structure that represents a collection of allowed and denied permissions as EntityInformation.

    Attributes:
        allow_anonymous: Indicates if anonymous users ere allowed.
        allowed_permissions: The list of allowed permissions.
        denied_permissions: The list of denied permissions.
        name: An optional permission set name.
    """

    allow_anonymous: Opt[bool] = None
    allowed_permissions: Opt[List[EntityInformation]] = None
    denied_permissions: Opt[List[EntityInformation]] = None
    name: Opt[str] = None

    def __init__(
        self,
        *,
        allow_anonymous: Opt[bool] = None,
        allowed_permissions: Opt[List[EntityInformation]] = None,
        denied_permissions: Opt[List[EntityInformation]] = None,
        name: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            allow_anonymous: Indicates if anonymous users ere allowed.
            allowed_permissions: The list of allowed permissions.
            denied_permissions: The list of denied permissions.
            name: An optional permission set name.
        """


@attrs(kw_only=True, auto_attribs=True)
class EntityInformationPermissionLevel(JidType, hint="Coveo.EntityInformationPermissionLevel"):
    """A structure that represents a level of permission where multiple permission sets as EntityInformation can be specified.

    Attributes:
        name: An optional permission level name.
    """

    permission_sets: Opt[List[EntityInformationPermissionSet]] = None
    name: Opt[str] = None

    def __init__(
        self, *, permission_sets: Opt[List[EntityInformationPermissionSet]] = None, name: Opt[str] = None
    ) -> None:
        """

        Parameters:
            name: An optional permission level name.
        """


@attrs(kw_only=True, auto_attribs=True)
class EntityInformationPermissionModel(JidType, hint="Coveo.EntityInformationPermissionModel"):
    """A structure that represent a permissions model that contains one or many permission levels as EntityInformation."""

    permission_levels: Opt[List[EntityInformationPermissionLevel]] = None

    def __init__(self, *, permission_levels: Opt[List[EntityInformationPermissionLevel]] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class PermissionModelsCountForState(JidType, hint="Coveo.PermissionModelsCountForState"):
    """Contains the number of permission models for a specific state.

    Attributes:
        state: The permission model state.
        count: The number of permission models for the state.
    """

    state: Opt[PermissionModelState] = None
    count: Opt[int] = None

    def __init__(self, *, state: Opt[PermissionModelState] = None, count: Opt[int] = None) -> None:
        """

        Parameters:
            state: The permission model state.
            count: The number of permission models for the state.
        """


@attrs(kw_only=True, auto_attribs=True)
class PermissionModelStateRootCause(JidType, hint="Coveo.PermissionModelStateRootCause"):
    """Contains information about the root cause of a permission model's non-valid state.

    Attributes:
        entity_id: The ID of the entity which caused the permission model's state.
        entity_state: The root cause's ID at the moment the permission model was updated.
    """

    entity_id: Opt[int] = attrib(default=None, metadata={CASING: "EntityID"})
    entity_state: Opt[EntityState] = None

    def __init__(
        self,
        *,
        entity_id: Opt[int] = attrib(default=None, metadata={CASING: "EntityID"}),
        entity_state: Opt[EntityState] = None,
    ) -> None:
        """

        Parameters:
            entity_id: The ID of the entity which caused the permission model's state.
            entity_state: The root cause's ID at the moment the permission model was updated.
        """


@attrs(kw_only=True, auto_attribs=True)
class PermissionModelInformation(JidType, hint="Coveo.PermissionModelInformation"):
    """Contains the information of a specific permission model.

    Attributes:
        state: The actual permission model state.
        created_date: The date at which the permission model was created.
        last_enabled_date: The date at which the permission model was last enabled.
        last_update_date: The date at which the effective permissions were last updated.
        is_out_of_date: Whether the permission model is currently queued to be updated.
        effective_permissions: Deprecated.
        original_permission_model: The original permission model that was added to the cache. May be empty if he permission model was optimized.
        id_: The unique permission model identifier.
        entities_info_permission_model: All permission model entities information.
        optimized_permission_models_info: The information of the permission models that were optimized.
        optimized_entities_info: The information of the entities that were optimized.
        state_root_cause: The root cause of the non-valid state (only set when State != Valid).
    """

    state: Opt[PermissionModelState] = None
    created_date: Opt[datetime] = None
    last_enabled_date: Opt[datetime] = None
    last_update_date: Opt[datetime] = None
    is_out_of_date: Opt[bool] = None
    effective_permissions: Opt[PermissionSet] = None
    original_permission_model: Opt[PermissionModel] = None
    id_: Opt[int] = attrib(default=None, metadata={CASING: "ID"})
    entities_info_permission_model: Opt[EntityInformationPermissionModel] = None
    optimized_permission_models_info: "Opt[List[PermissionModelInformation]]" = None
    optimized_entities_info: Opt[EntityInformationPermissionSet] = None
    state_root_cause: Opt[PermissionModelStateRootCause] = None

    def __init__(
        self,
        *,
        state: Opt[PermissionModelState] = None,
        created_date: Opt[datetime] = None,
        last_enabled_date: Opt[datetime] = None,
        last_update_date: Opt[datetime] = None,
        is_out_of_date: Opt[bool] = None,
        effective_permissions: Opt[PermissionSet] = None,
        original_permission_model: Opt[PermissionModel] = None,
        id_: Opt[int] = attrib(default=None, metadata={CASING: "ID"}),
        entities_info_permission_model: Opt[EntityInformationPermissionModel] = None,
        optimized_permission_models_info: "Opt[List[PermissionModelInformation]]" = None,
        optimized_entities_info: Opt[EntityInformationPermissionSet] = None,
        state_root_cause: Opt[PermissionModelStateRootCause] = None,
    ) -> None:
        """

        Parameters:
            state: The actual permission model state.
            created_date: The date at which the permission model was created.
            last_enabled_date: The date at which the permission model was last enabled.
            last_update_date: The date at which the effective permissions were last updated.
            is_out_of_date: Whether the permission model is currently queued to be updated.
            effective_permissions: Deprecated.
            original_permission_model: The original permission model that was added to the cache. May be empty if he permission model was optimized.
            id_: The unique permission model identifier.
            entities_info_permission_model: All permission model entities information.
            optimized_permission_models_info: The information of the permission models that were optimized.
            optimized_entities_info: The information of the entities that were optimized.
            state_root_cause: The root cause of the non-valid state (only set when State != Valid).
        """


@attrs(kw_only=True, auto_attribs=True)
class PermissionModelAddResult(JidType, hint="Coveo.PermissionModelAddResult"):
    """Contains the result of a single added permission model.

    Attributes:
        allowed_entity_ids: Contains all permission model allowed entity IDs.
        denied_entity_ids: Contains all permission model denied entity IDs.
        error: Contains an error that prevent the permission model to be correctly processed.
    """

    allowed_entity_ids: Opt[List[int]] = None
    denied_entity_ids: Opt[List[int]] = None
    error: Opt[str] = None

    def __init__(
        self,
        *,
        allowed_entity_ids: Opt[List[int]] = None,
        denied_entity_ids: Opt[List[int]] = None,
        error: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            allowed_entity_ids: Contains all permission model allowed entity IDs.
            denied_entity_ids: Contains all permission model denied entity IDs.
            error: Contains an error that prevent the permission model to be correctly processed.
        """


@attrs(kw_only=True, auto_attribs=True)
class SecurityCacheInformationStatus(StatusEntry, hint="Coveo.SecurityCacheInformationStatus"):
    """Contains information details about the Security Cache and all its providers.

    Attributes:
        entities_count: The total number of security entities.
        entities_in_error_count: The total number of security entities that are out-of-date or in-error, but aren't disabled.
        entities_count_per_state_per_provider: The total number of security entities per provider per state.
        permission_models_count: The total number of permission models.
        permission_models_count_per_state: The total number of permission models per state.
    """

    entities_count: Opt[int] = None
    entities_in_error_count: Opt[int] = None
    entities_count_per_state_per_provider: Opt[List[EntitiesCountPerStateForProvider]] = None
    permission_models_count: Opt[int] = None
    permission_models_count_per_state: Opt[List[PermissionModelsCountForState]] = None

    def __init__(
        self,
        *,
        entities_count: Opt[int] = None,
        entities_in_error_count: Opt[int] = None,
        entities_count_per_state_per_provider: Opt[List[EntitiesCountPerStateForProvider]] = None,
        permission_models_count: Opt[int] = None,
        permission_models_count_per_state: Opt[List[PermissionModelsCountForState]] = None,
    ) -> None:
        """

        Parameters:
            entities_count: The total number of security entities.
            entities_in_error_count: The total number of security entities that are out-of-date or in-error, but aren't disabled.
            entities_count_per_state_per_provider: The total number of security entities per provider per state.
            permission_models_count: The total number of permission models.
            permission_models_count_per_state: The total number of permission models per state.
        """


@attrs(kw_only=True, auto_attribs=True)
class SecurityCacheOperationStatus(StatusEntry, hint="Coveo.SecurityCacheOperationStatus"):
    """A structure that represents a security cache operation status.

    Attributes:
        operation_id: The operation id.
        number_of_created_jobs: The number of UpdateEntity jobs that were created by this blade instance for this operation Id.
        number_of_successful_jobs: The number of UpdateEntity jobs that were completed with success by this blade instance for this operation Id.
        number_of_failed_jobs: The number of UpdateEntity jobs that were completed with error by this blade instance for this operation Id.
        number_of_skipped_jobs: The number of UpdateEntity jobs that were skipped by this blade instance for this operation Id.
        number_of_processed_jobs: The number of UpdateEntity jobs that were processed (completed + skipped) by this blade instance for this operation.
        number_of_created_syncs: The number of UpdateEntity job results that were created by this blade instance for this operation Id.
        number_of_processed_syncs: The number of UpdateEntity job results that were processed by this blade instance for this operation Id.
    """

    operation_id: Opt[str] = None
    number_of_created_jobs: Opt[int] = None
    number_of_successful_jobs: Opt[int] = None
    number_of_failed_jobs: Opt[int] = None
    number_of_skipped_jobs: Opt[int] = None
    number_of_processed_jobs: Opt[int] = None
    number_of_created_syncs: Opt[int] = None
    number_of_processed_syncs: Opt[int] = None

    def __init__(
        self,
        *,
        operation_id: Opt[str] = None,
        number_of_created_jobs: Opt[int] = None,
        number_of_successful_jobs: Opt[int] = None,
        number_of_failed_jobs: Opt[int] = None,
        number_of_skipped_jobs: Opt[int] = None,
        number_of_processed_jobs: Opt[int] = None,
        number_of_created_syncs: Opt[int] = None,
        number_of_processed_syncs: Opt[int] = None,
    ) -> None:
        """

        Parameters:
            operation_id: The operation id.
            number_of_created_jobs: The number of UpdateEntity jobs that were created by this blade instance for this operation Id.
            number_of_successful_jobs: The number of UpdateEntity jobs that were completed with success by this blade instance for this operation Id.
            number_of_failed_jobs: The number of UpdateEntity jobs that were completed with error by this blade instance for this operation Id.
            number_of_skipped_jobs: The number of UpdateEntity jobs that were skipped by this blade instance for this operation Id.
            number_of_processed_jobs: The number of UpdateEntity jobs that were processed (completed + skipped) by this blade instance for this operation.
            number_of_created_syncs: The number of UpdateEntity job results that were created by this blade instance for this operation Id.
            number_of_processed_syncs: The number of UpdateEntity job results that were processed by this blade instance for this operation Id.
        """


@attrs(kw_only=True, auto_attribs=True)
class EntitiesListingOptions(JidType, hint="Coveo.EntitiesListingOptions"):
    """Contains options used to list entities.

    Attributes:
        recursive: Deprecated
        provider_name: Deprecated, use ProviderNames
        include_internal_entities: Whether to include internal entities in the entities to list
        provider_names: The security provider names of the security entities to list, or empty to specify all security providers.
        states: The states of the entities to list, or empty to specify all states.
        update_results: The update results of the entities to list, or empty to specify all update results.
        min_created_date: The minimum date at which the entities to list were created. Default: Minimum date value.
        max_created_date: The maximum date at which the entities to list were created. Default: Maximum date value.
        min_last_enabled_date: The minimum date at which the entities to list were last enabled. Default: Minimum date value.
        max_last_enabled_date: The maximum date at which the entities to list were last enabled. Default: Maximum date value.
        min_last_update_date: The minimum date at which the entities to list were last updated. Default: Minimum date value.
        max_last_update_date: The maximum date at which the entities to list were last updated. Default: Maximum date value.
        min_last_successful_update_date: The minimum date at which the entities to list were last successfully updated. Default: Minimum date value.
        max_last_successful_update_date: The maximum date at which the entities to list were last successfully updated. Default: Maximum date value.
        min_ordering_id: The minimum ordering ID of entities to list. Default: minimum ordering ID value.
        max_ordering_id: The maximum ordering ID of entities to list. Default: maximum ordering ID value.
        min_entity_id: The minimum ID of entities to list. Default: first ID (0).
        max_entity_id: The maximum ID of entities to list. Default: last possible ID.
        starting_position: The position where to start the entities listing.
        page_size: The maximum number of security entities to list.
    """

    recursive: bool = True
    provider_name: Opt[str] = None
    include_internal_entities: Opt[bool] = None
    provider_names: Opt[List[str]] = None
    states: Opt[List[EntityState]] = None
    update_results: Opt[List[EntityUpdateResult]] = None
    min_created_date: Opt[datetime] = None
    max_created_date: Opt[datetime] = None
    min_last_enabled_date: Opt[datetime] = None
    max_last_enabled_date: Opt[datetime] = None
    min_last_update_date: Opt[datetime] = None
    max_last_update_date: Opt[datetime] = None
    min_last_successful_update_date: Opt[datetime] = None
    max_last_successful_update_date: Opt[datetime] = None
    min_ordering_id: Opt[int] = attrib(default=None, metadata={CASING: "MinOrderingID"})
    max_ordering_id: Opt[int] = attrib(default=None, metadata={CASING: "MaxOrderingID"})
    min_entity_id: Opt[int] = attrib(default=None, metadata={CASING: "MinEntityID"})
    max_entity_id: Opt[int] = attrib(default=None, metadata={CASING: "MaxEntityID"})
    starting_position: Opt[int] = None
    page_size: int = 1000

    def __init__(
        self,
        *,
        recursive: bool = True,
        provider_name: Opt[str] = None,
        include_internal_entities: Opt[bool] = None,
        provider_names: Opt[List[str]] = None,
        states: Opt[List[EntityState]] = None,
        update_results: Opt[List[EntityUpdateResult]] = None,
        min_created_date: Opt[datetime] = None,
        max_created_date: Opt[datetime] = None,
        min_last_enabled_date: Opt[datetime] = None,
        max_last_enabled_date: Opt[datetime] = None,
        min_last_update_date: Opt[datetime] = None,
        max_last_update_date: Opt[datetime] = None,
        min_last_successful_update_date: Opt[datetime] = None,
        max_last_successful_update_date: Opt[datetime] = None,
        min_ordering_id: Opt[int] = attrib(default=None, metadata={CASING: "MinOrderingID"}),
        max_ordering_id: Opt[int] = attrib(default=None, metadata={CASING: "MaxOrderingID"}),
        min_entity_id: Opt[int] = attrib(default=None, metadata={CASING: "MinEntityID"}),
        max_entity_id: Opt[int] = attrib(default=None, metadata={CASING: "MaxEntityID"}),
        starting_position: Opt[int] = None,
        page_size: int = 1000,
    ) -> None:
        """

        Parameters:
            recursive: Deprecated
            provider_name: Deprecated, use ProviderNames
            include_internal_entities: Whether to include internal entities in the entities to list
            provider_names: The security provider names of the security entities to list, or empty to specify all security providers.
            states: The states of the entities to list, or empty to specify all states.
            update_results: The update results of the entities to list, or empty to specify all update results.
            min_created_date: The minimum date at which the entities to list were created. Default: Minimum date value.
            max_created_date: The maximum date at which the entities to list were created. Default: Maximum date value.
            min_last_enabled_date: The minimum date at which the entities to list were last enabled. Default: Minimum date value.
            max_last_enabled_date: The maximum date at which the entities to list were last enabled. Default: Maximum date value.
            min_last_update_date: The minimum date at which the entities to list were last updated. Default: Minimum date value.
            max_last_update_date: The maximum date at which the entities to list were last updated. Default: Maximum date value.
            min_last_successful_update_date: The minimum date at which the entities to list were last successfully updated. Default: Minimum date value.
            max_last_successful_update_date: The maximum date at which the entities to list were last successfully updated. Default: Maximum date value.
            min_ordering_id: The minimum ordering ID of entities to list. Default: minimum ordering ID value.
            max_ordering_id: The maximum ordering ID of entities to list. Default: maximum ordering ID value.
            min_entity_id: The minimum ID of entities to list. Default: first ID (0).
            max_entity_id: The maximum ID of entities to list. Default: last possible ID.
            starting_position: The position where to start the entities listing.
            page_size: The maximum number of security entities to list.
        """


@attrs(kw_only=True, auto_attribs=True)
class EffectivePermissionsListingOptions(EntitiesListingOptions, hint="Coveo.EffectivePermissionsListingOptions"):
    """Contains options used to list effective permissions

    Attributes:
        beautify_effective_permissions: Whether or not to filter out the redundant allowed entities from the effective permissions.
        return_allowed_entities: Whether allowed entities should be listed.
        return_denied_entities: Whether denied entities should be listed.
    """

    beautify_effective_permissions: bool = True
    return_allowed_entities: bool = True
    return_denied_entities: bool = True

    def __init__(
        self,
        *,
        beautify_effective_permissions: bool = True,
        return_allowed_entities: bool = True,
        return_denied_entities: bool = True,
    ) -> None:
        """

        Parameters:
            beautify_effective_permissions: Whether or not to filter out the redundant allowed entities from the effective permissions.
            return_allowed_entities: Whether allowed entities should be listed.
            return_denied_entities: Whether denied entities should be listed.
        """


@attrs(kw_only=True, auto_attribs=True)
class PermissionModelsListingOptions(JidType, hint="Coveo.PermissionModelsListingOptions"):
    """Contains options used to list permission models.

    Attributes:
        states: The states of the permission models to list, or empty to specify all states.
        min_last_update_date: The minimum date at which the permission models to list were last updated. Default: Minimum date value.
        max_last_update_date: The maximum date at which the permission models to list were last updated. Default: Maximum date value.
        min_created_date: The minimum date at which the permission models to list were created. Default: Minimum date value.
        max_created_date: The maximum date at which the permission models to list were created. Default: Maximum date value.
        min_last_enabled_date: The minimum date at which the permission models to list were last enabled. Default: Minimum date value.
        max_last_enabled_date: The maximum date at which the permission models to list were last enabled. Default: Maximum date value.
        starting_position: The position where to start the permission models listing.
        page_size: The maximum number of permission models to list.
    """

    states: Opt[List[PermissionModelState]] = None
    min_last_update_date: Opt[datetime] = None
    max_last_update_date: Opt[datetime] = None
    min_created_date: Opt[datetime] = None
    max_created_date: Opt[datetime] = None
    min_last_enabled_date: Opt[datetime] = None
    max_last_enabled_date: Opt[datetime] = None
    starting_position: Opt[int] = None
    page_size: int = 1000

    def __init__(
        self,
        *,
        states: Opt[List[PermissionModelState]] = None,
        min_last_update_date: Opt[datetime] = None,
        max_last_update_date: Opt[datetime] = None,
        min_created_date: Opt[datetime] = None,
        max_created_date: Opt[datetime] = None,
        min_last_enabled_date: Opt[datetime] = None,
        max_last_enabled_date: Opt[datetime] = None,
        starting_position: Opt[int] = None,
        page_size: int = 1000,
    ) -> None:
        """

        Parameters:
            states: The states of the permission models to list, or empty to specify all states.
            min_last_update_date: The minimum date at which the permission models to list were last updated. Default: Minimum date value.
            max_last_update_date: The maximum date at which the permission models to list were last updated. Default: Maximum date value.
            min_created_date: The minimum date at which the permission models to list were created. Default: Minimum date value.
            max_created_date: The maximum date at which the permission models to list were created. Default: Maximum date value.
            min_last_enabled_date: The minimum date at which the permission models to list were last enabled. Default: Minimum date value.
            max_last_enabled_date: The maximum date at which the permission models to list were last enabled. Default: Maximum date value.
            starting_position: The position where to start the permission models listing.
            page_size: The maximum number of permission models to list.
        """


class FailedDeclaratorReason(JidEnumFlag):
    Unknown: int = auto()
    NoWellknownSupport: int = auto()
    NoSynchronizedExpansion: int = auto()
    Timeout: int = auto()
    JobException: int = auto()
    ProviderException: int = auto()
    UnknownProvider: int = auto()
    InvalidDeclarator: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class FailedDeclarator(JidType, hint="Coveo.FailedDeclarator"):
    """Information about a declarator for which we failed to fetch parents.

    Attributes:
        declarator: Declarator for which we failed to fetch parents.
        reason: Reason we failed to fetch parents for declarator.
        message: Optional message with further details about the reason we failed.
    """

    declarator: Opt[SIDDeclarator] = None
    reason: Opt[FailedDeclaratorReason] = None
    message: Opt[str] = None

    def __init__(
        self,
        *,
        declarator: Opt[SIDDeclarator] = None,
        reason: Opt[FailedDeclaratorReason] = None,
        message: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            declarator: Declarator for which we failed to fetch parents.
            reason: Reason we failed to fetch parents for declarator.
            message: Optional message with further details about the reason we failed.
        """


@attrs(kw_only=True, auto_attribs=True)
class ParentEntitiesResponse(JidType, hint="Coveo.ParentEntitiesResponse"):
    """Information returned from GetParentEntities calls.

    Attributes:
        entities: Parent entities.
        failed_declarators: Declarators for which we could not fetch parent entities.
    """

    entities: Opt[List[SID]] = None
    failed_declarators: Opt[List[FailedDeclarator]] = None

    def __init__(
        self, *, entities: Opt[List[SID]] = None, failed_declarators: Opt[List[FailedDeclarator]] = None
    ) -> None:
        """

        Parameters:
            entities: Parent entities.
            failed_declarators: Declarators for which we could not fetch parent entities.
        """


@attrs(kw_only=True, auto_attribs=True)
class ParentEntityIDsResponse(JidType, hint="Coveo.ParentEntityIDsResponse"):
    """Information returned from GetParentEntityIDs calls.

    Attributes:
        entity_ids: ID of parent entities.
        failed_declarators: Declarators for which we could not fetch parent entity IDs.
    """

    entity_ids: Opt[List[int]] = attrib(default=None, metadata={CASING: "EntityIDs"})
    failed_declarators: Opt[List[FailedDeclarator]] = None

    def __init__(
        self,
        *,
        entity_ids: Opt[List[int]] = attrib(default=None, metadata={CASING: "EntityIDs"}),
        failed_declarators: Opt[List[FailedDeclarator]] = None,
    ) -> None:
        """

        Parameters:
            entity_ids: ID of parent entities.
            failed_declarators: Declarators for which we could not fetch parent entity IDs.
        """


@attrs(kw_only=True, auto_attribs=True)
class MismatchEntityId(JidType, hint="Coveo.MismatchEntityId"):
    """Information returned from ValidateSecurityStoreEntityIDs calls.

    Attributes:
        security_cache_entity_id: The Security Cache id.
        security_store_entity_id: The Security Store id.
    """

    security_cache_entity_id: Opt[int] = None
    security_store_entity_id: Opt[int] = None

    def __init__(self, *, security_cache_entity_id: Opt[int] = None, security_store_entity_id: Opt[int] = None) -> None:
        """

        Parameters:
            security_cache_entity_id: The Security Cache id.
            security_store_entity_id: The Security Store id.
        """


@attrs(kw_only=True, auto_attribs=True)
class SecurityEntityIDsValidationResult(JidType, hint="Coveo.SecurityEntityIDsValidationResult"):
    """Information returned from ValidateSecurityStoreEntityIDs calls.

    Attributes:
        result: If any mismatch ids
        mismatch_entity_ids: List of mismatch ids
    """

    result: Opt[bool] = None
    mismatch_entity_ids: Opt[List[MismatchEntityId]] = None

    def __init__(self, *, result: Opt[bool] = None, mismatch_entity_ids: Opt[List[MismatchEntityId]] = None) -> None:
        """

        Parameters:
            result: If any mismatch ids
            mismatch_entity_ids: List of mismatch ids
        """


class ISecurityExpansion(CoveoInterface):
    """The security expansion API provides various functionality tied to security."""

    @api("POST/sids/normalize", sid_declarator="SIDDeclarator")
    def normalize(self, *, sid_declarator: SIDDeclarator) -> SID:
        """Transforms a SIDDeclarator to its normalized form (SID).

        Parameters:
            sid_declarator: The SIDDeclarator to normalize.
        """

    @api("POST/sids/normalize_batch", sid_declarators="SIDDeclarators")
    def normalize_batch(self, *, sid_declarators: List[SIDDeclarator]) -> List[SID]:
        """Transforms many SIDDeclarators to their normalized form (SID).

        Parameters:
            sid_declarators: The SIDDeclarators to normalize.
        """

    @api("POST/sids/convert", sid="SID")
    def convert_to_string(self, *, sid: SID) -> str:
        """Converts a SID to a readable form.

        Parameters:
            sid: The SID to convert.
        """

    @api("POST/sids/convert_batch", sids="SIDs")
    def convert_to_string_batch(self, *, sids: List[SID]) -> List[str]:
        """Converts many SIDs to a readable form.

        Parameters:
            sids: The SIDs to convert.
        """

    @api("POST/providers/{provider_name}/login")
    def login(self, *, provider_name: str, user_name: str, password: str) -> MultiOut:
        """Attempts to login a user to an external system.

        Parameters:
            provider_name: The name of the security provider used to perform the login.
            user_name: The user name.
            password: The password.
        """

    @api("POST/providers/{provider_name}/authorize", document_uris="DocumentURIs")
    def authorize(
        self, *, provider_name: str, user_name: str, session_data: Union[str, bytes], document_uris: List[str]
    ) -> List[bool]:
        """Authorizes a user to a security provider.

        Parameters:
            provider_name: The name of the security provider to authorize to.
            user_name: The user name.
            session_data: The session data.
            document_uris: Document URIs to do the authorization for.
        """

    @api("POST/providers/{provider_name}/validate_session")
    def validate_session(self, *, provider_name: str, session_data: Union[str, bytes]) -> bool:
        """Validates a session to a security provider.

        Parameters:
            provider_name: The name of the security provider to validate the session for.
            session_data: The session data.
        """

    @api("POST/providers/{provider_name}/refresh_cache")
    def refresh_security_provider_cache(self, *, provider_name: str) -> None:
        """Refreshes the cache of a security provider.

        Parameters:
            provider_name: The name of a security provider.
        """

    @api("GET/expansion_status")
    def get_security_expansion_state(self) -> SecurityExpansionState:
        """Gets current state of the SecurityExpansion service."""

    @api("GET/runtime_instance_unique_identifier")
    def get_runtime_instance_unique_identifier(self) -> str:
        """Gets a unique identifier that is recreated every time the service is initialized."""

    @api("GET/information_status")
    def get_information_status(self) -> SecurityCacheInformationStatus:
        ...

    @api("GET/operation_statuses")
    def get_all_operation_statuses(self) -> List[SecurityCacheOperationStatus]:
        """Gets all current operation statuses for the blade."""

    @api("GET/operation_statuses/{operation_id}")
    def get_operation_status(self, *, operation_id: str) -> SecurityCacheOperationStatus:
        """Gets the operation status for the provided operation Id for the blade.

        Parameters:
            operation_id: The identifier that uniquely represents the operation to retrieve.
        """

    @api("POST/perform_data_integrity_check")
    def perform_data_integrity_check(self, *, perform_quick_checks_only: bool = True) -> bool:
        """Performs a manual data integrity check.

        Parameters:
            perform_quick_checks_only: Whether to only perform quick data integrity checks.
        """

    @api("POST/permission_models")
    def add_permission_model(self, *, permission_model: PermissionModel) -> MultiOut:
        """Adds the specified permission model and returns the unique security entities that represent this permission model.

        Parameters:
            permission_model: The permission model to add.
        """

    @api("POST/permission_models/add_and_optimize")
    def add_and_optimize_permission_model(self, *, permission_model: PermissionModel) -> MultiOut:
        """Adds the specified permission model and returns the unique security entities that represent this permission model.

        Parameters:
            permission_model: The permission model to add and optimize.
        """

    @api("POST/permission_models/add_batch")
    def add_permission_models_batch(
        self, *, permission_models: List[PermissionModel]
    ) -> List[PermissionModelAddResult]:
        """Adds all permission models returns the security entities that represent each of those permission models.

        Parameters:
            permission_models: The list of permission models to add.
        """

    @api("POST/permission_models/get_info")
    def get_permission_model_information(
        self, *, permission_model_effective_allowed_entity: SID, filter_effective_permissions_duplicates: bool
    ) -> PermissionModelInformation:
        """Gets the information about a given permission model.

        Parameters:
            permission_model_effective_allowed_entity: The entity that represents the permission model effective allowed entities.
            filter_effective_permissions_duplicates: Deprecated
        """

    @api("POST/permission_models/get_info_optimized")
    def get_optimized_permission_model_information(
        self,
        *,
        permission_model_allowed_entities: List[SID],
        permission_model_denied_entities: List[SID],
        permission_model: PermissionModel,
    ) -> PermissionModelInformation:
        """Gets the information about optimized and non-optimized permission models.

        Parameters:
            permission_model_allowed_entities: Contains the entities that represents the permission model allowed entities (may not be empty).
            permission_model_denied_entities: Contains the entities that represents the permission model denied entities (may be empty).
            permission_model: The original permission model that was previously added. May be left null
        """

    @api("GET/permission_models/get_count")
    def get_permission_models_count(self) -> int:
        """Gets the total number of permission models."""

    @api("GET/permission_models/get_count_per_state")
    def get_permission_models_count_per_state(self) -> List[PermissionModelsCountForState]:
        """Gets the total number of permission models per state."""

    @api("POST/permission_models/get_all")
    def get_permission_models(
        self, *, listing_options: PermissionModelsListingOptions, starting_position: int, page_size: int = 1000
    ) -> MultiOut:
        """Gets a list of permission models, starting from the specified position.

        Parameters:
            listing_options: The options used to select permission models (filtering, pagination, etc.)
            starting_position: Deprecated, use ListingOptions.StartingPosition
            page_size: Deprecated, use ListingOptions.PageSize
        """

    @api("POST/permission_models/get_all_infos")
    def get_permission_model_informations(self, *, listing_options: PermissionModelsListingOptions) -> MultiOut:
        """Gets the information about a list of permission models that match the given listing options.

        Parameters:
            listing_options: The options used to select permission models (filtering, pagination, etc.)
        """

    @api("GET/permission_models/has_pending_updates")
    def has_permission_models_to_update(self) -> bool:
        """Checks whether the blade has permission models to update."""

    @api("GET/permission_models/is_permission_models_update_throttled")
    def is_permission_models_update_throttled(self) -> bool:
        """Checks whether the permission models update is currently throttled."""

    @api("POST/permission_models/update")
    def update_permission_model(self, *, permission_model_effective_allowed_entity: SID) -> None:
        """Triggers an update of the effective permissions of a specific model.

        Parameters:
            permission_model_effective_allowed_entity: The entity that represents the permission model effective allowed entities to update.
        """

    @api("POST/permission_models/update_all")
    def update_all_permission_models(self) -> None:
        """Triggers an update of the effective permissions of all permission models."""

    @api("POST/permission_models/beautify_effective_permissions")
    def beautify_effective_permissions(
        self, *, allowed_entities: List[SID], denied_entities: List[SID]
    ) -> PermissionSet:
        """Depredated.

        Parameters:
            allowed_entities: Depredated.
            denied_entities: Depredated.
        """

    @api("POST/permission_models/effective_permissions")
    def get_permission_model_effective_permissions(
        self,
        *,
        permission_model_allowed_entities: List[SID],
        permission_model_denied_entities: List[SID],
        listing_options: EffectivePermissionsListingOptions,
    ) -> MultiOut:
        """Returns the effective permissions of the given permission model entities.

        Parameters:
            permission_model_allowed_entities: The list of effective permissions allowed entities.
            permission_model_denied_entities: The list of effective permissions denied entities.
            listing_options: Entities listing options to use.
        """

    @api("POST/entities/get_info_by_id", id_="ID")
    def get_entity_information_by_id(self, *, id_: int) -> EntityInformation:
        """Gets basic information of a specific entity using its unique identifier.

        Parameters:
            id_: The entity unique identifier to look for.
        """

    @api("POST/entities/get_info")
    def get_entity_information(self, *, entity: SID) -> EntityInformation:
        """Gets basic information of a specific entity.

        Parameters:
            entity: The entity to look for.
        """

    @api("GET/entities/get_count?include_internal_entities={IncludeInternalEntities}")
    def get_entities_count(self, *, include_internal_entities: bool = False) -> int:
        """Gets the total number of security entities.

        Parameters:
            include_internal_entities: Whether to include internal entities in the total (permission models entities).
        """

    @api("POST/entities/get_count_per_state_per_provider")
    def get_entities_count_per_state_per_provider(
        self, *, provider_name: str
    ) -> List[EntitiesCountPerStateForProvider]:
        """Gets the total number of security entities per provider per state.

        Parameters:
            provider_name: The security provider of the security entities to count, or empty to specify all security providers.
        """

    @api("POST/entities/get_all")
    def get_entities(self, *, provider_name: str, starting_position: int, page_size: int = 1000) -> List[EntityAndID]:
        """Gets a list of security entities, starting from the specified position.

        Parameters:
            provider_name: The security provider of the security entities to list, or empty to specify all security providers.
            starting_position: The position where to start the entities listing.
            page_size: The maximum number of security entities to list.
        """

    @api("POST/entities/get_all_and_ids")
    def get_entities_and_ids(self, *, starting_position: int, page_size: int) -> MultiOut:
        """Gets a list of security entities and their IDs, including internal entities, starting from the specified position.

        Parameters:
            starting_position: The position where to start the entities listing.
            page_size: The maximum number of security entities to list.
        """

    @api("POST/entities/get_all_info_for_states")
    def get_entities_information_for_states(
        self, *, provider_name: str, states: List[EntityState], starting_position: int, page_size: int = 1000
    ) -> List[EntityInformation]:
        """Deprecated; use GetEntitiesInformation instead.

        Parameters:
            provider_name: The security provider of the security entities to list, or empty to specify all security providers.
            states: The states of the security entities to list, or empty to specify all states.
            starting_position: The position where to start the entities listing.
            page_size: The maximum number of security entities to list.
        """

    @api("POST/entities/get_all_infos")
    def get_entities_information(self, *, listing_options: EntitiesListingOptions) -> MultiOut:
        """Gets a list of security entities information for the given states, starting from the specified position.

        Parameters:
            listing_options: The options to use to select entities (states, pagination, etc.)
        """

    @api("POST/entities/get_by_ids", entity_ids="EntityIDs")
    def get_entities_by_ids(self, *, entity_ids: List[int]) -> List[EntityAndID]:
        """Gets a list of the requested security entities.

        Parameters:
            entity_ids: The unique identifiers of the security entities to retrieve.
        """

    @api("POST/entities/get_parents")
    def get_parent_entities(
        self, *, entity: SID, recursive: bool, include_anonymous_entity: bool, create_entity_if_unknown: bool
    ) -> List[EntityAndID]:
        """Gets the list of all parent entities of a specific security entity.

        Parameters:
            entity: The entity to retrieve its parent entities.
            recursive: Whether parent entities should be listed recursively.
            include_anonymous_entity: Whether to include the anonymous entity and its parent entities in the list of parent entities.
            create_entity_if_unknown: If the entity is not known, a new UpdateEntity job will be published.
        """

    @api("POST/entities/get_parents_info")
    def get_parent_entities_information(
        self, *, entity: SID, recursive: bool, listing_options: EntitiesListingOptions
    ) -> MultiOut:
        """Gets the list of all parent entities of a specific security entity.

        Parameters:
            entity: The entity to retrieve its parent entities.
            recursive: Whether parent entities should be listed recursively.
            listing_options: The options to use to select entities (states, pagination, etc.)
        """

    @api("POST/entities/get_parents_from_declarator")
    def get_parent_entities_from_declarator(
        self, *, entity: SIDDeclarator, recursive: bool, include_anonymous_entity: bool, create_entity_if_unknown: bool
    ) -> List[SID]:
        """Gets the list of all parent security entities of a specific entity (combines Normalize and GetParentEntities)

        Parameters:
            entity: The entity to retrieve its parent entities.
            recursive: Whether parent entities should be listed recursively.
            include_anonymous_entity: Whether to return all parent entities of the anonymous entity (including all permission models)..
            create_entity_if_unknown: If the entity is not known, a new UpdateEntity job will be published.
        """

    @api("POST/entities/get_parents_from_declarators")
    def get_parent_entities_from_declarators(
        self,
        *,
        entities: List[SIDDeclarator],
        recursive: bool,
        include_anonymous_entity: bool,
        create_entity_if_unknown: bool,
    ) -> List[SID]:
        """Gets the list of all parent security entities of specific entities

        Parameters:
            entities: The entity to retrieve its parent entities.
            recursive: Whether parent entities should be listed recursively.
            include_anonymous_entity: Whether to return all parent entities of the anonymous entity (including all permission models)..
            create_entity_if_unknown: If the entity is not known, a new UpdateEntity job will be published.
        """

    @api("POST/entities/get_parents_from_declarators_2")
    def get_parent_entities_from_declarators2(
        self,
        *,
        entities: List[SIDDeclarator],
        recursive: bool,
        include_anonymous_entity: bool,
        create_entity_if_unknown: bool,
    ) -> ParentEntitiesResponse:
        """Gets the list of all parent security entities of specific entities

        Parameters:
            entities: The entities to retrieve parent entities for.
            recursive: Whether parent entities should be listed recursively.
            include_anonymous_entity: Whether to return all parent entities of the anonymous entity (including all permission models).
            create_entity_if_unknown: If the entity is not known, a new UpdateEntity job will be published.
        """

    @api("POST/entities/get_parent_entity_ids_from_declarators")
    def get_parent_entity_ids_from_declarators(
        self,
        *,
        entities: List[SIDDeclarator],
        recursive: bool,
        include_anonymous_entity: bool,
        create_entity_if_unknown: bool,
    ) -> List[int]:
        """Gets the list of all parent security entity IDs of specific entities.

        Parameters:
            entities: The entity IDs for which to retrieve their parent entities.
            recursive: Whether parent entities should be listed recursively.
            include_anonymous_entity: Whether to return all parent entities of the anonymous entity (including all permission models)..
            create_entity_if_unknown: If the entity is not known, a new UpdateEntity job will be published.
        """

    @api("POST/entities/get_parent_entity_ids_from_declarators_2")
    def get_parent_entity_ids_from_declarators2(
        self,
        *,
        entities: List[SIDDeclarator],
        recursive: bool,
        include_anonymous_entity: bool,
        create_entity_if_unknown: bool,
    ) -> ParentEntityIDsResponse:
        """Gets the list of all parent security entity IDs of specific entities.

        Parameters:
            entities: The entity IDs for which to retrieve their parent entities.
            recursive: Whether parent entities should be listed recursively.
            include_anonymous_entity: Whether to return all parent entities of the anonymous entity (including all permission models.
            create_entity_if_unknown: If the entity is not known, a new UpdateEntity job will be published.
        """

    @api("POST/entities/get_children")
    def get_child_entities(self, *, entity: SID, recursive: bool) -> List[EntityAndID]:
        """Gets the child entities (members) of a specific security entity.

        Parameters:
            entity: The entity to retrieve its child entities
            recursive: Whether children entities should be listed recursively.
        """

    @api("POST/entities/get_children_info")
    def get_child_entities_information(
        self, *, entity: SID, recursive: bool, listing_options: EntitiesListingOptions
    ) -> MultiOut:
        """Gets the list of all children entities of a specific security entity.

        Parameters:
            entity: The entity to retrieve its children entities.
            recursive: Whether children entities should be listed recursively.
            listing_options: The options to use to select entities (states, pagination, etc.)
        """

    @api("POST/entities/update")
    def update_entity(self, *, entity: SID, operation_id: str) -> None:
        """Triggers an update of the relationship of a specific security entity.

        Parameters:
            entity: The security entity to update.
            operation_id: An optional identifier that uniquely represents the current operation.
        """

    @api("POST/entities/update_all")
    def update_all_entities(self, *, provider_name: str, operation_id: str) -> None:
        """Triggers an update of the relationships of all security entities that aren't disabled.

        Parameters:
            provider_name: The security provider of the security entities to update, or empty to specify all security providers.
            operation_id: An optional identifier that uniquely represents the current operation.
        """

    @api("POST/entities/update_all_in_error")
    def update_all_entities_in_error(
        self, *, provider_name: str, operation_id: str, minimum_stored_date: datetime
    ) -> None:
        """Triggers an update of the relationships of all security entities that are out-of-date or in-error, but aren't disabled.

        Parameters:
            provider_name: The security provider of the security entities to update, or empty to specify all security providers.
            operation_id: An optional identifier that uniquely represents the current operation.
            minimum_stored_date: If specified, only entities updated after that date are considered.
        """

    @api("POST/entities/update_matching")
    def update_entities_matching(self, *, listing_options: EntitiesListingOptions, operation_id: str) -> None:
        """Triggers an update of the relationships of all security entities that match the given listing options.

        Parameters:
            listing_options: The options to use to select entities to update.
            operation_id: An optional identifier that uniquely represents the current operation.
        """

    @api("POST/entities/enable_all")
    def enable_all_disabled_entities(self, *, provider_name: str, operation_id: str) -> None:
        """Enables all disabled security entities.

        Parameters:
            provider_name: The security provider of the security entities to enable, or empty to specify all security providers.
            operation_id: An optional identifier that uniquely represents the current operation.
        """

    @api("POST/entities/enable")
    def enable_entities(
        self,
        *,
        listing_options: EntitiesListingOptions,
        specific_entities: List[SID],
        specific_declarator_entities: List[SIDDeclarator],
    ) -> None:
        """Enables all disabled security entities that match the given filter(s).

        Parameters:
            listing_options: The options to use to select entities to enable.
            specific_entities: The specific security entities to enable, if in SID format.
            specific_declarator_entities: The specific security entities to enable, if in declarator format.
        """

    @api("POST/entities/disable", ordering_id="OrderingID")
    def disable_entities(
        self,
        *,
        listing_options: EntitiesListingOptions,
        specific_entities: List[SID],
        specific_declarator_entities: List[SIDDeclarator],
        ordering_id: int,
    ) -> None:
        """Disables all security entities that match the given filter(s).

        Parameters:
            listing_options: The options to use to select entities to disable.
            specific_entities: The specific security entities to disable, if in SID format.
            specific_declarator_entities: The specific security entities to disable, if in declarator format.
            ordering_id: An optional ID that orders entity updates.
        """

    @api("GET/validate_security_store_entity_ids")
    def validate_security_store_entity_ids(self) -> SecurityEntityIDsValidationResult:
        """Performs a validation of security identities in the security store."""


class IJobProcessor(CoveoInterface):
    """Allows to push job commands to the security blade (internal use only)"""


@attrs(kw_only=True, auto_attribs=True)
class RelatedEntities(JidType, hint="Coveo.RelatedEntities"):
    """Container of related entities. Used for a specific type of relationship.

    Attributes:
        is_specified: Whether the related entities are specified. If not, the relationship should be ignored.
        entities: Related entities, in SID format.
        declarator_entities: Related entities, in declarator format.
    """

    is_specified: bool = True
    entities: Opt[List[SID]] = None
    declarator_entities: Opt[List[SIDDeclarator]] = None

    def __init__(
        self,
        *,
        is_specified: bool = True,
        entities: Opt[List[SID]] = None,
        declarator_entities: Opt[List[SIDDeclarator]] = None,
    ) -> None:
        """

        Parameters:
            is_specified: Whether the related entities are specified. If not, the relationship should be ignored.
            entities: Related entities, in SID format.
            declarator_entities: Related entities, in declarator format.
        """


@attrs(kw_only=True, auto_attribs=True)
class EntityRelationships(JidType, hint="Coveo.EntityRelationships"):
    """The complete relationships of an entity.

    Attributes:
        parents: Parents of the entity.
        children: Children of the entity.
    """

    parents: Opt[RelatedEntities] = None
    children: Opt[RelatedEntities] = None

    def __init__(self, *, parents: Opt[RelatedEntities] = None, children: Opt[RelatedEntities] = None) -> None:
        """

        Parameters:
            parents: Parents of the entity.
            children: Children of the entity.
        """


@attrs(kw_only=True, auto_attribs=True)
class EntityUpdateInformation(JidType, hint="Coveo.EntityUpdateInformation"):
    """The complete entity update information.

    Attributes:
        entity: The security entity that was updated, if in SID format.
        declarator_entity: The security entity that was updated, if in declarator format.
        date: The date at which the entity was updated.
        result: The result of the update.
        relationships: The updated relationships of the entity.
        error_detail: In the case of an unexpected error, contains some basic error details.
    """

    entity: Opt[SID] = None
    declarator_entity: Opt[SIDDeclarator] = None
    date: Opt[datetime] = None
    result: Opt[EntityUpdateResult] = None
    relationships: Opt[EntityRelationships] = None
    error_detail: Opt[str] = None

    def __init__(
        self,
        *,
        entity: Opt[SID] = None,
        declarator_entity: Opt[SIDDeclarator] = None,
        date: Opt[datetime] = None,
        result: Opt[EntityUpdateResult] = None,
        relationships: Opt[EntityRelationships] = None,
        error_detail: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            entity: The security entity that was updated, if in SID format.
            declarator_entity: The security entity that was updated, if in declarator format.
            date: The date at which the entity was updated.
            result: The result of the update.
            relationships: The updated relationships of the entity.
            error_detail: In the case of an unexpected error, contains some basic error details.
        """


class ISyncProcessor(CoveoInterface):
    """Allows to push synchronization commands to the security blade (internal use only)"""

    @api("POST/sync/entities/relationships", ordering_id="OrderingID")
    def process_sync_entity_relationships_updated(
        self,
        *,
        entity: SID,
        declarator_entity: SIDDeclarator,
        date: datetime,
        result: EntityUpdateResult,
        relationships: EntityRelationships,
        error_detail: str,
        operation_id: str,
        ordering_id: int,
    ) -> None:
        """Deprecated, use ProcessSync_EntitiesUpdated.

        Parameters:
            entity: The security entity that was updated, if in SID format.
            declarator_entity: The security entity that was updated, if in declarator format.
            date: The date at which the entity was updated.
            result: The result of the update.
            relationships: The updated relationships of the entity.
            error_detail: In the case of an unexpected error, contains some basic error details.
            operation_id: An optional identifier that uniquely represents the current operation.
            ordering_id: An optional id that orders entity updates.
        """

    @api("POST/sync/entities/relationships/batch", ordering_id="OrderingID")
    def process_sync_entities_updated(
        self, *, entities_update_information: List[EntityUpdateInformation], operation_id: str, ordering_id: int
    ) -> None:
        """Apply the relationship updates of a specific security entities.

        Parameters:
            entities_update_information: Contains the entities ralationships to update.
            operation_id: An optional identifier that uniquely represents the current operation.
            ordering_id: An optional id that orders entity updates.
        """

    @api("POST/sync/entities/enable")
    def process_sync_entities_enable_requested(
        self,
        *,
        listing_options: EntitiesListingOptions,
        specific_entities: List[SID],
        specific_declarator_entities: List[SIDDeclarator],
    ) -> None:
        """Enables all disabled security entities that match the given filter(s).

        Parameters:
            listing_options: The options to use to select entities to enable.
            specific_entities: The specific security entities to enable, if in SID format.
            specific_declarator_entities: The specific security entities to enable, if in declarator format.
        """

    @api("POST/sync/entities/disable", ordering_id="OrderingID")
    def process_sync_entities_disable_requested(
        self,
        *,
        listing_options: EntitiesListingOptions,
        specific_entities: List[SID],
        specific_declarator_entities: List[SIDDeclarator],
        ordering_id: int,
    ) -> None:
        """Disables all security entities that match the given filter(s).

        Parameters:
            listing_options: The options to use to select entities to disable.
            specific_entities: The specific security entities to disable, if in SID format.
            specific_declarator_entities: The specific security entities to disable, if in declarator format.
            ordering_id: An optional ID that orders entity updates.
        """


class SecurityCacheOperationType(JidEnumFlag):
    UpdateEntity: int = auto()
    UpdateAllEntities: int = auto()
    UpdateAllEntitiesInError: int = auto()
    UpdateEntitiesMatching: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class SecurityCacheMetric(MetricEntry, hint="Coveo.SecurityCacheMetric"):
    """A structure that represents a security cache metric.

    Attributes:
        operation_type: The operation type.
        operation_id: The operation id (may be empty).
        value: The value.
        success: Whether the operation completed with success.
    """

    operation_type: Opt[SecurityCacheOperationType] = None
    operation_id: Opt[str] = None
    value: Opt[float] = None
    success: Opt[bool] = None

    def __init__(
        self,
        *,
        operation_type: Opt[SecurityCacheOperationType] = None,
        operation_id: Opt[str] = None,
        value: Opt[float] = None,
        success: Opt[bool] = None,
    ) -> None:
        """

        Parameters:
            operation_type: The operation type.
            operation_id: The operation id (may be empty).
            value: The value.
            success: Whether the operation completed with success.
        """
