"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/SourceService.jid

"""

from typing import List
from .root import CoveoInterface, api
from .crawler import Config
from .document_config_definition import DocumentConfig


class ISourceService(CoveoInterface):
    """Interface used to retrieve the crawler config of an organization and source"""

    @api("GET/internal/organizations/{organization_id}/sources/{source_id}/crawlerconfig")
    def get_crawler_source_config(self, *, organization_id: str, source_id: str) -> Config:
        """Get the config for a crawler inside an organization

        Parameters:
            organization_id: The id of the organization.
            source_id: The id of the source.
        """

    @api("GET/internal/organizations/{organization_id}/crawlerconfigs")
    def get_crawler_sources_config(self, *, organization_id: str) -> List[Config]:
        """Get the configs for all crawlers inside an organization

        Parameters:
            organization_id: The id of the organization.
        """

    @api("GET/internal/organizations/{organization_id}/sources/{source_id}/crawlerdocumentconfig")
    def get_crawler_source_document_config(self, *, organization_id: str, source_id: str) -> DocumentConfig:
        """Get the document config for a crawler inside an organization

        Parameters:
            organization_id: The id of the organization.
            source_id: The id of the source.
        """
