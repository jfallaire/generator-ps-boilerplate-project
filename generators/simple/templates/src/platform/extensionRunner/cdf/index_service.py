"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/IndexService.jid

"""

from attr import attrib, attrs
from datetime import datetime
from enum import auto
from typing import Dict, List, Optional as Opt
from .root import CASING, CoveoInterface, ExceptionBase, JidEnumFlag, JidType, MultiOut, api
from .indexer_config import (
    CollaborativeRanking,
    Collection,
    Field,
    HighlightTag,
    PhysicalIndex,
    QueryHighlighter,
    Ranking,
    ResultsPreviewer,
    SearchCertificate,
    Slice,
    Source,
    System,
    TagField,
)
from .index_tracking import IndexStatus
from .document_definition import PermissionModel, PermissionSet
from .security import EffectivePermissionsListingOptions, PermissionModelInformation
from .security_provider import SID


@attrs(kw_only=True, auto_attribs=True)
class IndexException(ExceptionBase, hint="Coveo.IndexService.IndexException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidBinaryVersionException(IndexException, hint="Coveo.IndexService.InvalidBinaryVersionException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class OutOfRangeException(ExceptionBase, hint="Coveo.IndexService.OutOfRangeException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidDocumentKeyException(IndexException, hint="Coveo.IndexService.InvalidDocumentKeyException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class DocumentNotFoundException(IndexException, hint="Coveo.IndexService.DocumentNotFoundException"):
    def __init__(self) -> None:
        ...


class BladeState(JidEnumFlag):
    Created: int = auto()
    Initialized: int = auto()
    Starting: int = auto()
    Running: int = auto()
    WaitingForConfig: int = auto()
    OutOfSync: int = auto()
    ShuttingDown: int = auto()
    Synchronizing: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class IndexerConfig(JidType, hint="Coveo.IndexService.IndexerConfig"):
    """Some global configuration for the indexer blade

    Attributes:
        tagging_manager_uri: The URI to the tagging manager
        security_server_uri: The security server URI
        mirror_name: The mirror name of this index
        index_path: The physical path for the index
        realtime_indexing_path: The physical path for the realtime indexing files.
        slice_paths: The physical paths for each slice.
        index_identifier: The index identifier.
        config_cache_page_size: The b-tree page size for the config cache.
        config_cache_size: The b-tree cache size for the config cache.
    """

    tagging_manager_uri: Opt[str] = attrib(default=None, metadata={CASING: "TaggingManagerURI"})
    security_server_uri: Opt[str] = attrib(default=None, metadata={CASING: "SecurityServerURI"})
    mirror_name: Opt[str] = None
    index_path: Opt[str] = None
    realtime_indexing_path: Opt[str] = None
    slice_paths: Opt[Dict[str, str]] = None
    index_identifier: Opt[str] = None
    config_cache_page_size: int = 1048576
    config_cache_size: int = 67108864

    def __init__(
        self,
        *,
        tagging_manager_uri: Opt[str] = attrib(default=None, metadata={CASING: "TaggingManagerURI"}),
        security_server_uri: Opt[str] = attrib(default=None, metadata={CASING: "SecurityServerURI"}),
        mirror_name: Opt[str] = None,
        index_path: Opt[str] = None,
        realtime_indexing_path: Opt[str] = None,
        slice_paths: Opt[Dict[str, str]] = None,
        index_identifier: Opt[str] = None,
        config_cache_page_size: int = 1048576,
        config_cache_size: int = 67108864,
    ) -> None:
        """

        Parameters:
            tagging_manager_uri: The URI to the tagging manager
            security_server_uri: The security server URI
            mirror_name: The mirror name of this index
            index_path: The physical path for the index
            realtime_indexing_path: The physical path for the realtime indexing files.
            slice_paths: The physical paths for each slice.
            index_identifier: The index identifier.
            config_cache_page_size: The b-tree page size for the config cache.
            config_cache_size: The b-tree cache size for the config cache.
        """


@attrs(kw_only=True, auto_attribs=True)
class ElasticSearchConnection(JidType, hint="Coveo.IndexService.ElasticSearchConnection"):
    """Elasticsearch connection.

    Attributes:
        host: The URI of th elasticsearch host (like 'host.adomain.com').
        port: The port to used (default is 9200).
        username: The user name for http_auth.
        password: The user's password for http_auth.
        url_prefix: The URL prefix.
        use_ssl: Whether we use SSL or not.
        verify_certs: Whether we check the certificates or not.
        ca_certs: Optional path to CA bundle on disk.
        client_cert: Path to the file containing the private key and the certificate, or cert only if using CientKey.
        client_key: Path to the file containing the private key if using separate cert and key files (client_cert will contain only the cert).
        aws_access_key: The AWS access key.
        aws_secret_key: The AWS secret key.
        aws_region: The AWS region.
        aws_service_name: The AWS service name.
    """

    host: Opt[str] = None
    port: int = 9200
    username: Opt[str] = None
    password: Opt[str] = None
    url_prefix: Opt[str] = attrib(default=None, metadata={CASING: "URLPrefix"})
    use_ssl: Opt[bool] = attrib(default=None, metadata={CASING: "UseSSL"})
    verify_certs: Opt[bool] = None
    ca_certs: Opt[str] = attrib(default=None, metadata={CASING: "CACerts"})
    client_cert: Opt[str] = None
    client_key: Opt[str] = None
    aws_access_key: Opt[str] = attrib(default=None, metadata={CASING: "AWSAccessKey"})
    aws_secret_key: Opt[str] = attrib(default=None, metadata={CASING: "AWSSecretKey"})
    aws_region: Opt[str] = attrib(default=None, metadata={CASING: "AWSRegion"})
    aws_service_name: Opt[str] = attrib(default=None, metadata={CASING: "AWSServiceName"})

    def __init__(
        self,
        *,
        host: Opt[str] = None,
        port: int = 9200,
        username: Opt[str] = None,
        password: Opt[str] = None,
        url_prefix: Opt[str] = attrib(default=None, metadata={CASING: "URLPrefix"}),
        use_ssl: Opt[bool] = attrib(default=None, metadata={CASING: "UseSSL"}),
        verify_certs: Opt[bool] = None,
        ca_certs: Opt[str] = attrib(default=None, metadata={CASING: "CACerts"}),
        client_cert: Opt[str] = None,
        client_key: Opt[str] = None,
        aws_access_key: Opt[str] = attrib(default=None, metadata={CASING: "AWSAccessKey"}),
        aws_secret_key: Opt[str] = attrib(default=None, metadata={CASING: "AWSSecretKey"}),
        aws_region: Opt[str] = attrib(default=None, metadata={CASING: "AWSRegion"}),
        aws_service_name: Opt[str] = attrib(default=None, metadata={CASING: "AWSServiceName"}),
    ) -> None:
        """

        Parameters:
            host: The URI of th elasticsearch host (like 'host.adomain.com').
            port: The port to used (default is 9200).
            username: The user name for http_auth.
            password: The user's password for http_auth.
            url_prefix: The URL prefix.
            use_ssl: Whether we use SSL or not.
            verify_certs: Whether we check the certificates or not.
            ca_certs: Optional path to CA bundle on disk.
            client_cert: Path to the file containing the private key and the certificate, or cert only if using CientKey.
            client_key: Path to the file containing the private key if using separate cert and key files (client_cert will contain only the cert).
            aws_access_key: The AWS access key.
            aws_secret_key: The AWS secret key.
            aws_region: The AWS region.
            aws_service_name: The AWS service name.
        """


@attrs(kw_only=True, auto_attribs=True)
class ElasticSearchBladeConfig(JidType, hint="Coveo.IndexService.ElasticSearchBladeConfig"):
    """Some global configuration for the elasticsearch indexer blade

    Attributes:
        message_store: Optional folder where to keep a copy of the add_document messages.
        logger_config: Optional logger configuration. Format to be defined.
    """

    message_store: Opt[str] = None
    logger_config: Opt[str] = None

    def __init__(self, *, message_store: Opt[str] = None, logger_config: Opt[str] = None) -> None:
        """

        Parameters:
            message_store: Optional folder where to keep a copy of the add_document messages.
            logger_config: Optional logger configuration. Format to be defined.
        """


@attrs(kw_only=True, auto_attribs=True)
class ElasticSearchConfig(JidType, hint="Coveo.IndexService.ElasticSearchConfig"):
    """Some global configuration for the elasticsearch indexer blade and search API.

    Attributes:
        connection_v: List of elasticsearch connections.
        indexer_config: Indexer blade config.
    """

    connection_v: Opt[List[ElasticSearchConnection]] = None
    indexer_config: Opt[ElasticSearchBladeConfig] = None

    def __init__(
        self,
        *,
        connection_v: Opt[List[ElasticSearchConnection]] = None,
        indexer_config: Opt[ElasticSearchBladeConfig] = None,
    ) -> None:
        """

        Parameters:
            connection_v: List of elasticsearch connections.
            indexer_config: Indexer blade config.
        """


@attrs(kw_only=True, auto_attribs=True)
class IndexState(JidType, hint="Coveo.IndexService.IndexState"):
    """Internal state for the index.

    Attributes:
        inconsistent_index: Whether the index is in an inconsistent state.
        inconsistent_config: Whether the index config is in an inconsistent state.
    """

    inconsistent_index: Opt[bool] = None
    inconsistent_config: Opt[bool] = None

    def __init__(self, *, inconsistent_index: Opt[bool] = None, inconsistent_config: Opt[bool] = None) -> None:
        """

        Parameters:
            inconsistent_index: Whether the index is in an inconsistent state.
            inconsistent_config: Whether the index config is in an inconsistent state.
        """


class IIndexAdmin(CoveoInterface):
    """Main interface used to control an index node."""

    @api("GET/ranking")
    def get_ranking(self) -> Ranking:
        """Get ranking configuration for the index."""

    @api("PUT/ranking")
    def update_ranking(self, *, ranking: Ranking) -> None:
        """Update ranking configuration in the index.

        Parameters:
            ranking: The updated configuration for ranking.
        """

    @api("GET/system")
    def get_system(self) -> System:
        """Get system configuration for the index."""

    @api("PUT/system", system="system")
    def update_system(self, *, system: System) -> None:
        """Update system configuration in the index.

        Parameters:
            system: The updated configuration for system.
        """

    @api("GET/query_highlighter")
    def get_query_highlighter(self) -> QueryHighlighter:
        """Get query highlighter configuration for the index."""

    @api("PUT/query_highlighter")
    def update_query_highlighter(self, *, query_highlighter: QueryHighlighter) -> None:
        """Update query highlighter configuration in the index.

        Parameters:
            query_highlighter: The updated configuration for query highlighter.
        """

    @api("GET/query_highlighter/highlight_tags")
    def get_highlight_tags(self) -> List[HighlightTag]:
        """Get all the highlight tags in the index."""

    @api("GET/query_highlighter/highlight_tags/{highlight_tag_id}", highlight_tag_id="HighlightTagID")
    def get_highlight_tag(self, *, highlight_tag_id: int) -> HighlightTag:
        """Get a highlight tag from the index.

        Parameters:
            highlight_tag_id: The id of the highlight tag.
        """

    @api("POST/query_highlighter/highlight_tags")
    def add_highlight_tag(self, *, highlight_tag: HighlightTag) -> None:
        """Add a highlight tag to the index.

        Parameters:
            highlight_tag: The new highlight tag.
        """

    @api("PUT/query_highlighter/highlight_tags/{highlight_tag_id}", highlight_tag_id="HighlightTagID")
    def update_highlight_tag(self, *, highlight_tag_id: int, highlight_tag: HighlightTag) -> None:
        """Update a highlight tag in the index.

        Parameters:
            highlight_tag_id: The id of the highlight tag.
            highlight_tag: The updated highlight tag.
        """

    @api("DELETE/query_highlighter/highlight_tags/{highlight_tag_id}", highlight_tag_id="HighlightTagID")
    def delete_highlight_tag(self, *, highlight_tag_id: int) -> None:
        """Delete a highlight tag contained in the index.

        Parameters:
            highlight_tag_id: The id of the highlight tag.
        """

    @api("GET/slices")
    def get_slices(self) -> List[Slice]:
        """Get all the slices in the index."""

    @api("GET/slices/{slice_id}", slice_id="SliceID")
    def get_slice(self, *, slice_id: int) -> Slice:
        """Get a slice from the index.

        Parameters:
            slice_id: The id of the slice.
        """

    @api("POST/slices", slice_="Slice")
    def add_slice(self, *, slice_: Slice) -> None:
        """Add a slice to the index.

        Parameters:
            slice_: The new slice.
        """

    @api("PUT/slices/{slice_id}", slice_id="SliceID", slice_="Slice")
    def update_slice(self, *, slice_id: int, slice_: Slice) -> None:
        """Update a slice in the index.

        Parameters:
            slice_id: The id of the slice.
            slice_: The updated slice.
        """

    @api("DELETE/slices/{slice_id}", slice_id="SliceID")
    def delete_slice(self, *, slice_id: int) -> None:
        """Delete a slice from the index.

        Parameters:
            slice_id: The id of the slice.
        """

    @api("GET/results_previewers")
    def get_results_previewers(self) -> List[ResultsPreviewer]:
        """Get all the results previewers in the index."""

    @api("GET/results_previewers/{results_previewer_id}", results_previewer_id="ResultsPreviewerID")
    def get_results_previewer(self, *, results_previewer_id: int) -> ResultsPreviewer:
        """Get a results previewer from the index.

        Parameters:
            results_previewer_id: The id of the results previewer.
        """

    @api("POST/results_previewers")
    def add_results_previewer(self, *, results_previewer: ResultsPreviewer) -> None:
        """Add a results previewer to the index.

        Parameters:
            results_previewer: The new results previewer.
        """

    @api("PUT/results_previewers/{results_previewer_id}", results_previewer_id="ResultsPreviewerID")
    def update_results_previewer(self, *, results_previewer_id: int, results_previewer: ResultsPreviewer) -> None:
        """Update a results previewer in the index.

        Parameters:
            results_previewer_id: The id of the results previewer.
            results_previewer: The updated results previewer.
        """

    @api("DELETE/results_previewers/{results_previewer_id}", results_previewer_id="ResultsPreviewerID")
    def delete_results_previewer(self, *, results_previewer_id: int) -> None:
        """Delete a results previewer from the index.

        Parameters:
            results_previewer_id: The id of the results previewer.
        """

    @api("GET/tag_fields")
    def get_tag_fields(self) -> List[TagField]:
        """Get all the tag fields in the index."""

    @api("GET/tag_fields/{tag_field_id}", tag_field_id="TagFieldID")
    def get_tag_field(self, *, tag_field_id: int) -> TagField:
        """Get a tag field from the index.

        Parameters:
            tag_field_id: The id of the tag field.
        """

    @api("POST/tag_fields")
    def add_tag_field(self, *, tag_field: TagField) -> None:
        """Add a tag field to the index.

        Parameters:
            tag_field: The new tag field.
        """

    @api("PUT/tag_fields/{tag_field_id}", tag_field_id="TagFieldID")
    def update_tag_field(self, *, tag_field_id: int, tag_field: TagField) -> None:
        """Update a tag field in the index.

        Parameters:
            tag_field_id: The id of the tag field.
            tag_field: The updated tag field.
        """

    @api("DELETE/tag_fields/{tag_field_id}", tag_field_id="TagFieldID")
    def delete_tag_field(self, *, tag_field_id: int) -> None:
        """Delete a tag field from the index.

        Parameters:
            tag_field_id: The id of the tag field.
        """

    @api("GET/collaborative_ranking")
    def get_collaborative_ranking(self) -> CollaborativeRanking:
        """Get collaborative ranking configuration for the index."""

    @api("PUT/collaborative_ranking")
    def update_collaborative_ranking(self, *, collaborative_ranking: CollaborativeRanking) -> None:
        """Update collaborative ranking configuration in the index.

        Parameters:
            collaborative_ranking: The updated configuration for collaborative ranking.
        """

    @api("GET/physical_index")
    def get_physical_index(self) -> PhysicalIndex:
        """Get physical index configuration for the index."""

    @api("PUT/physical_index")
    def update_physical_index(self, *, physical_index: PhysicalIndex) -> None:
        """Update physical index configuration in the index.

        Parameters:
            physical_index: The updated configuration for physical index.
        """

    @api("GET/search_certificates")
    def get_search_certificates(self) -> List[SearchCertificate]:
        """Get the search certificates for the index."""

    @api("GET/search_certificates/{search_certificate_id}", search_certificate_id="SearchCertificateID")
    def get_search_certificate(self, *, search_certificate_id: int) -> SearchCertificate:
        """Get a search certificate from the index.

        Parameters:
            search_certificate_id: The id of the search certificate.
        """

    @api("POST/search_certificates")
    def add_search_certificate(self, *, search_certificate: SearchCertificate) -> None:
        """Add a new search certificate to the index.

        Parameters:
            search_certificate: The new search certificate
        """

    @api("PUT/search_certificates/{search_certificate_id}", search_certificate_id="SearchCertificateID")
    def update_search_certificate(self, *, search_certificate_id: int, search_certificate: SearchCertificate) -> None:
        """Update a search certificate in the index.

        Parameters:
            search_certificate_id: The id of the search certificate.
            search_certificate: The updated search certificate.
        """

    @api("DELETE/search_certificates/{search_certificate_id}", search_certificate_id="SearchCertificateID")
    def delete_search_certificate(self, *, search_certificate_id: int) -> None:
        """Delete a search certificate from the index.

        Parameters:
            search_certificate_id: The id of the search certificate.
        """

    @api("PUT/index")
    def set_config(self, *, configuration: IndexerConfig) -> None:
        """Set the indexer configuration

        Parameters:
            configuration: The new configuration.
        """

    @api("GET/index")
    def get_config(self) -> IndexerConfig:
        """Get the indexer configuration"""

    @api("GET/status")
    def get_state(self) -> BladeState:
        """Get the state of the index."""

    @api("DELETE/index")
    def delete_index_data(self, *, delete_config: bool) -> None:
        """Delete all files used by an index node.

        Parameters:
            delete_config: True to delete the config folder.
        """

    @api("GET/creation_date")
    def get_creation_date(self) -> datetime:
        """Get the index creation date. Will be set to the source's value on the destination when synchronizing."""

    @api("GET/readonly")
    def is_in_read_only_mode(self) -> bool:
        ...

    @api("PUT/readonly")
    def set_read_only_mode(self, *, read_only_mode: bool) -> None:
        ...

    @api("POST/restore_security_module")
    def restore_security_module(self) -> None:
        ...

    @api("POST/check_integrity")
    def check_index_integrity(self) -> None:
        ...

    @api("POST/cancel_check_integrity")
    def cancel_index_integrity_check(self) -> None:
        ...

    @api("GET/check_integrity_in_progress")
    def is_checking_integrity(self) -> bool:
        ...

    @api("POST/commit_transaction")
    def commit_current_transaction(self, *, wait_for_documents: bool = False) -> None:
        ...

    @api("POST/flush")
    def flush(self) -> None:
        ...

    @api("POST/export_tags")
    def export_tags(self, *, output_file_name: str) -> None:
        ...

    @api("DELETE/groupby_cache")
    def clear_group_by_cache(self) -> None:
        ...

    @api("POST/rebuild_wcl")
    def rebuild_wcl(self) -> None:
        ...

    @api("DELETE/stem_classes_correlation")
    def decorrelate_stem_classes(self) -> None:
        ...

    @api("DELETE/profilings_logs")
    def delete_old_profiling_logs(self, *, days_to_keep_profiling_logs: int) -> None:
        ...

    @api("GET/statistics")
    def get_indexer_statistics(self) -> IndexStatus:
        ...

    @api("GET/document_keys")
    def get_document_keys(self, *, starting_document_key: str, page_size: int = 1000) -> List[str]:
        """Gets a list of indexed document keys, starting from the specified position.

        Parameters:
            starting_document_key: The key used to specify where to start the document keys listing.
            page_size: The maximum number of document keys to list.
        """

    @api("POST/document_permission_model")
    def get_document_permission_model(self, *, document_key: str) -> PermissionModel:
        ...

    @api("POST/document_permission_model_info")
    def get_document_permission_model_information(
        self, *, document_key: str, filter_effective_permissions_duplicates: bool = True
    ) -> PermissionModelInformation:
        ...

    @api("POST/document_effective_permissions")
    def get_document_effective_permissions(
        self, *, document_key: str, beautify_effective_permissions: bool = True
    ) -> PermissionSet:
        ...

    @api("POST/document_effective_permissions_info")
    def get_document_effective_permissions_information(
        self, *, document_key: str, listing_options: EffectivePermissionsListingOptions
    ) -> MultiOut:
        ...

    @api("POST/dump_all_unique_permission_models_to_file")
    def dump_all_unique_permission_models_to_file(self) -> None:
        ...

    @api("POST/are_security_identities_used_in_document_permissions")
    def are_security_identities_used_in_document_permissions(self, *, security_identities: List[SID]) -> List[bool]:
        ...


class IIndexingConfig(CoveoInterface):
    """Interface used to modify configurations that affect document indexing."""

    @api("GET/collections")
    def get_collections(self) -> List[Collection]:
        """Get all the collections in the index."""

    @api("GET/collections/{collection_id}", collection_id="CollectionID")
    def get_collection(self, *, collection_id: int) -> Collection:
        """Get the config of a collection from the index.

        Parameters:
            collection_id: The id of the collection.
        """

    @api("PUT/collections")
    def set_collections(self, *, collections: List[Collection]) -> None:
        """Set the collections in the index.

        Parameters:
            collections: The collections for the index.
        """

    @api("POST/collections")
    def add_collection(self, *, collection: Collection) -> None:
        """Add a collection to the index.

        Parameters:
            collection: The configuration for the new collection.
        """

    @api("PUT/collections/{collection_id}", collection_id="CollectionID")
    def update_collection(self, *, collection_id: int, collection: Collection) -> None:
        """Update a collection in the index.

        Parameters:
            collection_id: The id of the collection.
            collection: The updated configuration for the collection.
        """

    @api("DELETE/collections/{collection_id}", collection_id="CollectionID")
    def delete_collection(self, *, collection_id: int) -> None:
        """Delete a collection from the index.

        Parameters:
            collection_id: The id of the collection.
        """

    @api("GET/collections/{collection_id}/sources", collection_id="CollectionID")
    def get_sources(self, *, collection_id: int) -> List[Source]:
        """Get all the sources for a collection.

        Parameters:
            collection_id: The id of the parent collection.
        """

    @api("GET/collections/{collection_id}/sources/{source_id}", collection_id="CollectionID", source_id="SourceID")
    def get_source(self, *, collection_id: int, source_id: int) -> Source:
        """Get the config of a source for a collection.

        Parameters:
            collection_id: The id of the parent collection.
            source_id: The id of the source.
        """

    @api("PUT/collections/{collection_id}/sources", collection_id="CollectionID")
    def set_sources(self, *, collection_id: int, sources: List[Source]) -> None:
        """Set the sources for a collection in the index.

        Parameters:
            collection_id: The id of the parent collection.
            sources: The sources for the collection in the index.
        """

    @api("POST/collections/{collection_id}/sources", collection_id="CollectionID")
    def add_source(self, *, collection_id: int, source: Source) -> None:
        """Add a source to the index.

        Parameters:
            collection_id: The id of the parent collection.
            source: The configuration for the new source.
        """

    @api("PUT/collections/{collection_id}/sources/{source_id}", collection_id="CollectionID", source_id="SourceID")
    def update_source(self, *, collection_id: int, source_id: int, source: Source) -> None:
        """Update a source in the index.

        Parameters:
            collection_id: The id of the parent collection.
            source_id: The id of the source.
            source: The updated configuration for the source.
        """

    @api("DELETE/collections/{collection_id}/sources/{source_id}", collection_id="CollectionID", source_id="SourceID")
    def delete_source(self, *, collection_id: int, source_id: int) -> None:
        """Delete a source contained in the index.

        Parameters:
            collection_id: The id of the parent collection.
            source_id: The id of the source.
        """

    @api("GET/fields")
    def get_fields(self) -> List[Field]:
        """Get all fields in the index."""

    @api("PUT/fields/id")
    def set_fields_by_id(self, *, fields: List[Field]) -> None:
        """Set the fields in the index.

        Parameters:
            fields: The fields for the index.
        """

    @api("PUT/fields/name")
    def set_fields_by_name(self, *, fields: List[Field]) -> None:
        """Set the fields in the index.

        Parameters:
            fields: The fields for the index.
        """

    @api("GET/fields/id/{field_id}", field_id="FieldID")
    def get_field_by_id(self, *, field_id: int) -> Field:
        """Get the config of a field from the index.

        Parameters:
            field_id: The id of the field.
        """

    @api("GET/fields/name/{field_name}")
    def get_field_by_name(self, *, field_name: str) -> Field:
        """Get the config of a field from the index.

        Parameters:
            field_name: The name of the field.
        """

    @api("POST/fields/batch")
    def add_fields(self, *, fields: List[Field]) -> None:
        """Add a batch of fields to the index.

        Parameters:
            fields: The configurations for the new fields.
        """

    @api("PUT/fields/batch/id")
    def update_fields_by_id(self, *, fields: List[Field]) -> None:
        """Update a batch fields in the index.

        Parameters:
            fields: The updated configurations for the fields.
        """

    @api("PUT/fields/batch/name")
    def update_fields_by_name(self, *, fields: List[Field]) -> None:
        """Update a batch of fields in the index.

        Parameters:
            fields: The updated configurations for the fields.
        """

    @api("DELETE/fields/batch/id", field_ids="FieldIDs")
    def delete_fields_by_id(self, *, field_ids: List[int]) -> None:
        """Delete a batch of field contained in the index.

        Parameters:
            field_ids: The ids of the fields.
        """

    @api("DELETE/fields/batch/name")
    def delete_fields_by_name(self, *, field_names: List[str]) -> None:
        """Delete a batch of fields contained in the index.

        Parameters:
            field_names: The names of the fields.
        """

    @api("POST/fields")
    def add_field(self, *, field: Field) -> None:
        """Add a field to the index.

        Parameters:
            field: The configuration for the new field.
        """

    @api("PUT/fields/id/{field_id}", field_id="FieldID")
    def update_field_by_id(self, *, field_id: int, field: Field) -> None:
        """Update a field in the index.

        Parameters:
            field_id: The id of the field.
            field: The updated configuration for the field.
        """

    @api("PUT/fields/name/{field_name}")
    def update_field_by_name(self, *, field_name: str, field: Field) -> None:
        """Update a field in the index.

        Parameters:
            field_name: The name of the field.
            field: The updated configuration for the field.
        """

    @api("DELETE/fields/id/{field_id}", field_id="FieldID")
    def delete_field_by_id(self, *, field_id: int) -> None:
        """Delete a field contained in the index.

        Parameters:
            field_id: The id of the field.
        """

    @api("DELETE/fields/name/{field_name}")
    def delete_field_by_name(self, *, field_name: str) -> None:
        """Delete a field contained in the index.

        Parameters:
            field_name: The name of the field.
        """


class IElasticSearchIndexAdmin(CoveoInterface):
    """Main interface used to control an index node."""

    @api("PUT/elasticsearch")
    def set_elastic_search_config(self, *, configuration: ElasticSearchConfig) -> None:
        """Set the elasticsearch configuration

        Parameters:
            configuration: The new configuration.
        """

    @api("GET/elasticsearch")
    def get_elastic_search_config(self) -> ElasticSearchConfig:
        """Get the elasticsearch configuration"""
