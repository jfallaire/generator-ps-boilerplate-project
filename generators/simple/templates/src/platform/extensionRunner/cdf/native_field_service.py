"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/NativeFieldService.jid

"""

from attr import attrs
from typing import List
from .root import CoveoInterface, ExceptionBase, api
from .indexer_config import Field


@attrs(kw_only=True, auto_attribs=True)
class ServiceException(ExceptionBase, hint="Coveo.NativeFieldService.ServiceException"):
    def __init__(self) -> None:
        ...


class INativeFieldService(CoveoInterface):
    """Interface used to retrieve the fields of an organization"""

    @api("GET/internal/organizations/{organization_id}/native/fields", organization_id="organizationId")
    def get_fields(self, *, organization_id: str) -> List[Field]:
        """Get all the fields for an organization.

        Parameters:
            organization_id: The id of the organization.
        """
