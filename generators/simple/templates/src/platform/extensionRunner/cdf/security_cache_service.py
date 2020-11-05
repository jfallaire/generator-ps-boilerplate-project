"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/SecurityCacheService.jid

"""

from attr import attrs
from typing import List, Optional as Opt
from .root import CoveoInterface, JidType, api
from .security_provider import SID, SecurityProviderConfig
from .document_definition import PermissionIdentityType


@attrs(kw_only=True, auto_attribs=True)
class AdditionalInfo(JidType, hint="Coveo.SecurityCacheService.AdditionalInfo"):
    """The additional information of a security entity.

    Attributes:
        key: The additional information key.
        value: The additional information value.
    """

    key: Opt[str] = None
    value: Opt[str] = None

    def __init__(self, *, key: Opt[str] = None, value: Opt[str] = None) -> None:
        """

        Parameters:
            key: The additional information key.
            value: The additional information value.
        """


class ISecurityCacheService(CoveoInterface):
    @api(
        "GET/organizations/{organization_id}/securitycache/entities/{provider_name}",
        page="page",
        per_page="perPage",
        states="states",
    )
    def get_entities(
        self, *, organization_id: str, provider_name: str, page: int, per_page: int, states: List[str]
    ) -> List[SID]:
        """Gets a list of security entities for the specified organization, starting from the specified position for a specific provider.

        Parameters:
            organization_id: The id of the organization owning the security provider instance.
            provider_name: The security provider of the security entities to list.
            page: The position where to start the entities listing.
            per_page: The maximum number of security entities to list.
            states: The states of the entities to list.
        """

    @api("POST/organizations/{organization_id}/securitycache/refresh/entity", type_="Type")
    def refresh_entity(
        self,
        *,
        organization_id: str,
        provider: str,
        name: str,
        type_: PermissionIdentityType,
        infos: List[AdditionalInfo],
    ) -> None:
        """Refreshes a single entity in the security cache.

        Parameters:
            organization_id: The organization identifier of the security entity to refresh.
            provider: The security provider of the security entity to refresh.
            name: The security entity name.
            type_: The security entity type.
            infos: The security entity additional information.
        """

    @api("GET/organizations/{organization_id}/securityproviders/{provider_name}/config/decrypted")
    def get_config(self, *, organization_id: str, provider_name: str) -> SecurityProviderConfig:
        """Retrieves a decrypted security provider configuration.

        Parameters:
            organization_id: The organization identifier of the security provider.
            provider_name: The security provider identifier.
        """
