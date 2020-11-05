"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/CoveoSecurityStoreService.jid

"""

from attr import attrib, attrs
from datetime import datetime
from typing import List, Optional as Opt
from .root import CASING, CoveoInterface, ExceptionBase, JidType, MultiOut, api
from .security_provider import SID


@attrs(kw_only=True, auto_attribs=True)
class SecurityStoreServiceException(ExceptionBase, hint="Coveo.SecurityStoreServiceException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidStateException(SecurityStoreServiceException, hint="Coveo.InvalidStateException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class NotStartedException(InvalidStateException, hint="Coveo.NotStartedException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class IsShutdownException(InvalidStateException, hint="Coveo.IsShutdownException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidOrganizationIdException(SecurityStoreServiceException, hint="Coveo.InvalidOrganizationIdException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class UnknownOrganizationIdException(SecurityStoreServiceException, hint="Coveo.UnknownOrganizationIdException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class OrganizationIdAlreadyExistsException(
    SecurityStoreServiceException, hint="Coveo.OrganizationIdAlreadyExistsException"
):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidProviderNameException(SecurityStoreServiceException, hint="Coveo.InvalidProviderNameException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class UnknownProviderNameException(SecurityStoreServiceException, hint="Coveo.UnknownProviderNameException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ProviderNameAlreadyExistsException(
    SecurityStoreServiceException, hint="Coveo.ProviderNameAlreadyExistsException"
):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidIdentityException(SecurityStoreServiceException, hint="Coveo.InvalidIdentityException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidIdentityProviderNameException(InvalidIdentityException, hint="Coveo.InvalidIdentityProviderNameException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class UnknownIdentityProviderNameException(InvalidIdentityException, hint="Coveo.UnknownIdentityProviderNameException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class IdentityTooBigException(InvalidIdentityException, hint="Coveo.IdentityTooBigException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class IdentityIsNullException(InvalidIdentityException, hint="Coveo.IdentityIsNullException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class UnknownIdentityIdException(SecurityStoreServiceException, hint="Coveo.UnknownIdentityIdException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidNumberToReturnException(SecurityStoreServiceException, hint="Coveo.InvalidNumberToReturnException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ProviderInfo(JidType, hint="Coveo.ProviderInfo"):
    """Contains the information of a specific security provider.

    Attributes:
        name: The unique name of the security provider.
        number_of_identities: The number of identities of the provider.
        created_date: The date at which the security provider was created.
    """

    name: Opt[str] = None
    number_of_identities: Opt[int] = None
    created_date: Opt[datetime] = None

    def __init__(
        self, *, name: Opt[str] = None, number_of_identities: Opt[int] = None, created_date: Opt[datetime] = None
    ) -> None:
        """

        Parameters:
            name: The unique name of the security provider.
            number_of_identities: The number of identities of the provider.
            created_date: The date at which the security provider was created.
        """


@attrs(kw_only=True, auto_attribs=True)
class OrganizationInfo(JidType, hint="Coveo.OrganizationInfo"):
    """Contains the information of a specific organization.

    Attributes:
        id_: The unique id of the organization.
        created_date: The date at which the organization was created.
        number_of_identities: The number of identities of the organization.
        providers_info: All organization security providers information.
    """

    id_: Opt[str] = attrib(default=None, metadata={CASING: "Id"})
    created_date: Opt[datetime] = None
    number_of_identities: Opt[int] = None
    providers_info: Opt[List[ProviderInfo]] = None

    def __init__(
        self,
        *,
        id_: Opt[str] = attrib(default=None, metadata={CASING: "Id"}),
        created_date: Opt[datetime] = None,
        number_of_identities: Opt[int] = None,
        providers_info: Opt[List[ProviderInfo]] = None,
    ) -> None:
        """

        Parameters:
            id_: The unique id of the organization.
            created_date: The date at which the organization was created.
            number_of_identities: The number of identities of the organization.
            providers_info: All organization security providers information.
        """


@attrs(kw_only=True, auto_attribs=True)
class IdentityImportInfo(JidType, hint="Coveo.IdentityImportInfo"):
    """Contains the information of a specific security identity.

    Attributes:
        id_: The unique security identity id.
        sid: The security identity in binary format.
    """

    id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"})
    sid: Opt[SID] = attrib(default=None, metadata={CASING: "SID"})

    def __init__(
        self,
        *,
        id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"}),
        sid: Opt[SID] = attrib(default=None, metadata={CASING: "SID"}),
    ) -> None:
        """

        Parameters:
            id_: The unique security identity id.
            sid: The security identity in binary format.
        """


class ISecurityStoreServiceAdmin(CoveoInterface):
    """Security Store Service administrative interface"""

    @api("GET/binary_schema_version")
    def get_binary_schema_version(self) -> int:
        """Returns the binary schema version"""

    @api("GET/schema_version")
    def get_current_schema_version(self) -> int:
        """Returns the current schema version"""

    @api("GET/data_version")
    def get_current_data_version(self) -> int:
        """Returns the current data version"""

    @api("POST/perform_data_revise")
    def perform_data_revise(self, *, target_data_version: int, is_final: bool) -> None:
        """Starts a data revise to the specified target version"""

    @api("GET/organizations")
    def get_organization_ids(self) -> List[str]:
        """Returns all organization ids"""

    @api("POST/organizations")
    def add_organization(self, *, organization_id: str) -> None:
        """Adds a new organization

        Parameters:
            organization_id: The unique id of the organization
        """

    @api("GET/organizations/{organization_id}")
    def get_organization_info(self, *, organization_id: str) -> OrganizationInfo:
        """Get the organization information

        Parameters:
            organization_id: The unique id of the organization
        """

    @api("DELETE/organizations/{organization_id}")
    def remove_organization(self, *, organization_id: str) -> None:
        """Deletes the organization and all its security providers

        Parameters:
            organization_id: The unique id of the organization
        """

    @api("POST/organizations/{organization_id}/providers")
    def add_provider(self, *, organization_id: str, provider_name: str) -> None:
        """Adds a new provider to the organization

        Parameters:
            organization_id: The unique id of the organization
            provider_name: The unique name of the security provider
        """

    @api("GET/organizations/{organization_id}/providers/{provider_name}")
    def get_provider_info(self, *, organization_id: str, provider_name: str) -> ProviderInfo:
        """Get the security provider information

        Parameters:
            organization_id: The unique id of the organization
            provider_name: The unique name of the security provider
        """

    @api("DELETE/organizations/{organization_id}/providers/{provider_name}")
    def remove_provider(self, *, organization_id: str, provider_name: str) -> None:
        """Deletes the security provider

        Parameters:
            organization_id: The unique id of the organization
            provider_name: The unique name of the security provider
        """

    @api("POST/logging/{logger_name}/level/{level}")
    def set_logging_level(self, *, logger_name: str, level: int) -> None:
        """Set the logging level of a specific logger

        Parameters:
            logger_name: The name of the logger
            level: The new level for the logger
        """

    @api("GET/logging/{logger_name}/level")
    def get_logging_level(self, *, logger_name: str) -> int:
        """Get the logging level of a specific logger

        Parameters:
            logger_name: The name of the logger
        """

    @api("POST/organizations/{organization_id}/import_identities")
    def import_security_identities(
        self, *, organization_id: str, identities_import_info: List[IdentityImportInfo]
    ) -> None:
        """Used to import security identities into the store

        Parameters:
            organization_id: The unique id of the organization
            identities_import_info: The list of identities to import
        """


@attrs(kw_only=True, auto_attribs=True)
class IdentityInfo(JidType, hint="Coveo.IdentityInfo"):
    """Contains the information of a specific security identity.

    Attributes:
        id_: The unique security identity id.
        sid: The security identity in binary format.
        created_date: The date at which the security identity was created.
    """

    id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"})
    sid: Opt[SID] = attrib(default=None, metadata={CASING: "SID"})
    created_date: Opt[datetime] = None

    def __init__(
        self,
        *,
        id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"}),
        sid: Opt[SID] = attrib(default=None, metadata={CASING: "SID"}),
        created_date: Opt[datetime] = None,
    ) -> None:
        """

        Parameters:
            id_: The unique security identity id.
            sid: The security identity in binary format.
            created_date: The date at which the security identity was created.
        """


@attrs(kw_only=True, auto_attribs=True)
class IdentitiesListingOptions(JidType, hint="Coveo.IdentitiesListingOptions"):
    """Contains options used to list security identities.

    Attributes:
        include_internal_identities: Whether to include internal security identities in the security identities to list
        provider_names: The security provider names of the security identities to list, or empty to specify all security providers.
        min_created_date: The minimum date at which the security identities to list were last created. Default: Minimum date value.
        max_created_date: The maximum date at which the security identities to list were last created. Default: Maximum date value.
        starting_position: The position where to start the security identities listing.
        number_to_return: The maximum number of security identities to list.
    """

    include_internal_identities: Opt[bool] = None
    provider_names: Opt[List[str]] = None
    min_created_date: Opt[datetime] = None
    max_created_date: Opt[datetime] = None
    starting_position: Opt[int] = None
    number_to_return: int = 1000

    def __init__(
        self,
        *,
        include_internal_identities: Opt[bool] = None,
        provider_names: Opt[List[str]] = None,
        min_created_date: Opt[datetime] = None,
        max_created_date: Opt[datetime] = None,
        starting_position: Opt[int] = None,
        number_to_return: int = 1000,
    ) -> None:
        """

        Parameters:
            include_internal_identities: Whether to include internal security identities in the security identities to list
            provider_names: The security provider names of the security identities to list, or empty to specify all security providers.
            min_created_date: The minimum date at which the security identities to list were last created. Default: Minimum date value.
            max_created_date: The maximum date at which the security identities to list were last created. Default: Maximum date value.
            starting_position: The position where to start the security identities listing.
            number_to_return: The maximum number of security identities to list.
        """


class ISecurityStoreService(CoveoInterface):
    """Security Store Service interface"""

    @api("POST/organizations/{organization_id}/ids/sid", sid="SID")
    def get_identity_id_for_sid(self, *, organization_id: str, sid: SID, add_if_unknown: bool) -> int:
        """Retrieves the security identity Id for a SID

        Parameters:
            organization_id: The unique id of the organization
            sid: The identity in SID format
            add_if_unknown: Whether the identity should be added if it's unknown
        """

    @api("POST/organizations/{organization_id}/ids/sids", sids="SIDs")
    def get_identity_ids_for_sids(self, *, organization_id: str, sids: List[SID], add_if_unknown: bool) -> List[int]:
        """Retrieves the security identity Ids for many SIDs

        Parameters:
            organization_id: The unique id of the organization
            sids: The identities in SID format
            add_if_unknown: Whether the identities should be added if they are unknown
        """

    @api("GET/organizations/{organization_id}/ids/{identity_id}/info")
    def get_identity_info(self, *, organization_id: str, identity_id: int) -> IdentityInfo:
        """Retrieves the identity information for an Id.

        Parameters:
            organization_id: The unique id of the organization
            identity_id: The unique id of the security identity
        """

    @api("POST/organizations/{organization_id}/ids/info")
    def get_identities_info_for_ids(self, *, organization_id: str, identity_ids: List[int]) -> List[IdentityInfo]:
        """Retrieves the identity information for many Ids

        Parameters:
            organization_id: The unique id of the organization
            identity_ids: The unique ids of the security identities
        """

    @api("POST/organizations/{organization_id}/ids/info/filter")
    def get_identities_info(self, *, organization_id: str, listing_options: IdentitiesListingOptions) -> MultiOut:
        """Retrieves the identity information for the given listing options

        Parameters:
            organization_id: The unique id of the organization
            listing_options: The options to use to select which security identities to return.
        """
