"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/CoveoSecurityProvider.jid

"""

from attr import attrib, attrs
from enum import auto
from typing import Dict, List, Optional as Opt, Union
from .root import CASING, CoveoInterface, ExceptionBase, JidEnumFlag, JidType, MultiOut, api
from .config_definition import DataFile, Parameter, ParameterGroupDefinition, SecurityProvider, UserIdentity
from .document_definition import PermissionIdentityType


@attrs(kw_only=True, auto_attribs=True)
class SecurityException(ExceptionBase, hint="Coveo.CSP.SecurityException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityCallNotSupportedException(SecurityException, hint="Coveo.CSP.SecurityCallNotSupportedException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityInvalidUserGroupException(SecurityException, hint="Coveo.CSP.SecurityInvalidUserGroupException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityEntityNotFoundException(SecurityException, hint="Coveo.CSP.SecurityEntityNotFoundException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityProviderNotReadyException(SecurityException, hint="Coveo.CSP.SecurityProviderNotReadyException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class FatalException(SecurityException, hint="Coveo.CSP.FatalException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class AccessDeniedException(FatalException, hint="Coveo.CSP.AccessDeniedException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidSIDException(SecurityException, hint="Coveo.CSP.InvalidSIDException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidSIDStringException(SecurityException, hint="Coveo.CSP.InvalidSIDStringException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityProvidersException(ExceptionBase, hint="Coveo.CSP.SecurityProvidersException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityProviderNotRegisteredException(
    SecurityProvidersException, hint="Coveo.CSP.SecurityProviderNotRegisteredException"
):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityProviderAlreadyRegisteredException(
    SecurityProvidersException, hint="Coveo.CSP.SecurityProviderAlreadyRegisteredException"
):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityProviderTimeOutException(SecurityProvidersException, hint="Coveo.CSP.SecurityProviderTimeOutException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityProviderUnreachableException(
    SecurityProvidersException, hint="Coveo.CSP.SecurityProviderUnreachableException"
):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityProviderUnexpectedException(
    SecurityProvidersException, hint="Coveo.CSP.SecurityProviderUnexpectedException"
):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SID(JidType, hint="Coveo.CSP.SID"):
    provider: Opt[str] = None
    data: Opt[Union[str, bytes]] = None

    def __init__(self, *, provider: Opt[str] = None, data: Opt[Union[str, bytes]] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityProviderDescription(JidType, hint="Coveo.CSP.SecurityProviderDescription"):
    """

    Attributes:
        name: Name of the Security Provider
        type_: Type of the Security Provider
    """

    name: Opt[str] = None
    type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"})

    def __init__(
        self, *, name: Opt[str] = None, type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"})
    ) -> None:
        """

        Parameters:
            name: Name of the Security Provider
            type_: Type of the Security Provider
        """


@attrs(kw_only=True, auto_attribs=True)
class SIDDeclarator(JidType, hint="Coveo.CSP.SIDDeclarator"):
    provider: Opt[str] = None
    declaration: Opt[str] = None

    def __init__(self, *, provider: Opt[str] = None, declaration: Opt[str] = None) -> None:
        ...


class Options(JidEnumFlag):
    UNKNOWN: int = auto()
    STRING_TO_SID: int = auto()
    SID_TO_STRING: int = auto()
    GET_MEMBERS_AND_MAPPINGS: int = auto()
    LOGIN: int = auto()
    AUTHORIZE: int = auto()
    GET_WELLKNOWNGROUPS: int = auto()
    REFRESH_CACHE: int = auto()
    LOGIN_EX: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class Information(JidType, hint="Coveo.CSP.Information"):
    name: Opt[str] = None
    type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"})
    capabilities: Opt[Options] = None
    is_case_sensitive: Opt[bool] = None
    is_thread_safe: Opt[bool] = None

    def __init__(
        self,
        *,
        name: Opt[str] = None,
        type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"}),
        capabilities: Opt[Options] = None,
        is_case_sensitive: Opt[bool] = None,
        is_thread_safe: Opt[bool] = None,
    ) -> None:
        ...


class ISecurityProvider(CoveoInterface):
    @api("GET/information")
    def get_information(self) -> Information:
        ...

    @api("POST/sid/from_string", string_="String")
    def string_to_sid(self, *, string_: str) -> SID:
        ...

    @api("POST/sid/to_string", sid="SID")
    def sidto_string(self, *, sid: SID) -> str:
        ...

    @api("POST/sid/members", sid="SID")
    def get_members_and_mappings(self, *, sid: SID) -> MultiOut:
        ...

    @api("POST/sid/well_knowns", sid="SID")
    def get_well_known_groups(self, *, sid: SID) -> List[SID]:
        ...

    @api("POST/session/login")
    def login(self, *, user_name: str, password: str) -> MultiOut:
        ...

    @api("POST/session/validate")
    def validate_session(self, *, session_data: Union[str, bytes]) -> bool:
        ...

    @api("POST/session/authorize", document_uris="DocumentURIs")
    def authorize(self, *, user_name: str, session_data: Union[str, bytes], document_uris: List[str]) -> List[bool]:
        ...

    @api("POST/refresh")
    def refresh_cache(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityProviderConfig(JidType, hint="Coveo.CSP.SecurityProviderConfig"):
    """Config for a security provider.

    Attributes:
        name: The name of the security provider.
        user_identities: User Identities.
        parameters: The init parameters.
        data_files: The data files.
        security_providers: The bounded security providers.
        index_identifier: The index identifier.
        db_connection_string: The database connection string.
        organization_id: The organization id.
    """

    name: Opt[str] = None
    user_identities: Opt[Dict[str, UserIdentity]] = None
    parameters: Opt[Dict[str, Parameter]] = None
    data_files: Opt[Dict[str, DataFile]] = None
    security_providers: Opt[Dict[str, SecurityProvider]] = None
    index_identifier: Opt[str] = None
    db_connection_string: Opt[str] = None
    organization_id: Opt[str] = None

    def __init__(
        self,
        *,
        name: Opt[str] = None,
        user_identities: Opt[Dict[str, UserIdentity]] = None,
        parameters: Opt[Dict[str, Parameter]] = None,
        data_files: Opt[Dict[str, DataFile]] = None,
        security_providers: Opt[Dict[str, SecurityProvider]] = None,
        index_identifier: Opt[str] = None,
        db_connection_string: Opt[str] = None,
        organization_id: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            name: The name of the security provider.
            user_identities: User Identities.
            parameters: The init parameters.
            data_files: The data files.
            security_providers: The bounded security providers.
            index_identifier: The index identifier.
            db_connection_string: The database connection string.
            organization_id: The organization id.
        """


class ISecurityProviderAdmin(CoveoInterface):
    @api("GET/config")
    def get_config(self) -> SecurityProviderConfig:
        ...

    @api("PUT/config")
    def set_config(self, *, config: SecurityProviderConfig) -> None:
        ...

    @api("GET/parameters")
    def get_parameters(self) -> List[ParameterGroupDefinition]:
        ...


@attrs(kw_only=True, auto_attribs=True)
class Identity(JidType, hint="Coveo.CSP.Identity"):
    """

    Attributes:
        name: The name of the identity.
        type_: The type of the identity.
        provider: The name of the security provider this identity belongs to.
        additional_info: The identity additional info.
    """

    name: Opt[str] = None
    type_: Opt[PermissionIdentityType] = attrib(default=None, metadata={CASING: "Type"})
    provider: Opt[str] = None
    additional_info: Opt[Dict[str, str]] = None

    def __init__(
        self,
        *,
        name: Opt[str] = None,
        type_: Opt[PermissionIdentityType] = attrib(default=None, metadata={CASING: "Type"}),
        provider: Opt[str] = None,
        additional_info: Opt[Dict[str, str]] = None,
    ) -> None:
        """

        Parameters:
            name: The name of the identity.
            type_: The type of the identity.
            provider: The name of the security provider this identity belongs to.
            additional_info: The identity additional info.
        """


@attrs(kw_only=True, auto_attribs=True)
class StoreMembersBatchItem(JidType, hint="Coveo.CSP.StoreMembersBatchItem"):
    """

    Attributes:
        identity: The identity.
        members: The identity members.
        well_knowns: The identity well knowns.
    """

    identity: Opt[Identity] = None
    members: Opt[List[Identity]] = None
    well_knowns: Opt[List[Identity]] = None

    def __init__(
        self,
        *,
        identity: Opt[Identity] = None,
        members: Opt[List[Identity]] = None,
        well_knowns: Opt[List[Identity]] = None,
    ) -> None:
        """

        Parameters:
            identity: The identity.
            members: The identity members.
            well_knowns: The identity well knowns.
        """


class IStoreExpandedPermissionProvider(CoveoInterface):
    @api("PUT/members/{organization_id}/{provider_id}")
    def store_members(
        self,
        *,
        organization_id: str,
        provider_id: str,
        identity: Identity,
        operation_id: int,
        members_security_provider: str,
        members: List[Identity],
        well_knowns: List[Identity],
    ) -> None:
        """

        Parameters:
            organization_id: The organization identifier.
            provider_id: The provider identifier.
            identity: The identity.
            operation_id: The operation identifier.
            members_security_provider: The security provider name of the members. This parameter is now obsolete, pass the provider name in the members identities.
            members: The identity members.
            well_knowns: The identity well knowns.
        """

    @api("DELETE/members/{organization_id}/{provider_id}")
    def delete_member(self, *, organization_id: str, provider_id: str, identity: Identity) -> None:
        """

        Parameters:
            organization_id: The organization identifier.
            provider_id: The provider identifier.
            identity: The identity to delete.
        """

    @api("DELETE/members/{organization_id}/{provider_id}/olderThan")
    def delete_members_older_than(self, *, organization_id: str, provider_id: str, operation_id: int) -> None:
        """

        Parameters:
            organization_id: The organization identifier.
            provider_id: The provider identifier.
            operation_id: The operation identifier.
        """

    @api("PUT/members/{organization_id}/{provider_id}/batch")
    def process_batch(
        self,
        *,
        organization_id: str,
        provider_id: str,
        operation_id: int,
        identites_to_store: List[StoreMembersBatchItem],
        identites_to_delete: List[Identity],
    ) -> None:
        """

        Parameters:
            organization_id: The organization identifier.
            provider_id: The provider identifier.
            operation_id: The batch operation identifier.
            identites_to_store: The identities to store.
            identites_to_delete: The identities to delete.
        """
