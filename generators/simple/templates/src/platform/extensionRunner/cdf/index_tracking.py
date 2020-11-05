"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/IndexTracking.jid

"""

from attr import attrib, attrs
from datetime import datetime
from enum import auto
from typing import List, Optional as Opt
from .root import CASING, JidEnumFlag, JidType
from .tracking import MetricEntry, StatusEntry


@attrs(kw_only=True, auto_attribs=True)
class IndexSourceStatus(JidType, hint="Coveo.IndexTracking.IndexSourceStatus"):
    """Status of a single source in the index

    Attributes:
        collection_id: ID of collection containing the source
        source_id: Source ID
        document_count: Number of documents in the source
        document_total_size: Total size of documents in the source
        pending_docs_to_add: Number of documents waiting to be added in transactions for this source
        pending_docs_to_update: Number of documents waiting to be updated in transactions for this source
        pending_docs_to_delete: Number of documents waiting to be deleted in transactions for this source
    """

    collection_id: Opt[int] = None
    source_id: Opt[int] = None
    document_count: Opt[int] = None
    document_total_size: Opt[int] = None
    pending_docs_to_add: Opt[int] = None
    pending_docs_to_update: Opt[int] = None
    pending_docs_to_delete: Opt[int] = None

    def __init__(
        self,
        *,
        collection_id: Opt[int] = None,
        source_id: Opt[int] = None,
        document_count: Opt[int] = None,
        document_total_size: Opt[int] = None,
        pending_docs_to_add: Opt[int] = None,
        pending_docs_to_update: Opt[int] = None,
        pending_docs_to_delete: Opt[int] = None,
    ) -> None:
        """

        Parameters:
            collection_id: ID of collection containing the source
            source_id: Source ID
            document_count: Number of documents in the source
            document_total_size: Total size of documents in the source
            pending_docs_to_add: Number of documents waiting to be added in transactions for this source
            pending_docs_to_update: Number of documents waiting to be updated in transactions for this source
            pending_docs_to_delete: Number of documents waiting to be deleted in transactions for this source
        """


@attrs(kw_only=True, auto_attribs=True)
class LexiconMemoryBreakdown(JidType, hint="Coveo.IndexTracking.LexiconMemoryBreakdown"):
    """All the memory used by the lexicon

    Attributes:
        b_tree_caches: Memory used by the BTree caches
        facets_cache: Memory used by the facets cache
        terms_cache: Memory used by the terms cache
        term_ids_cache: Memory used by the string to identifier mapping cache
        sort_cache_num_fields: Memory used by the numerical fields sort cache
        sort_cache_string_fields: Memory used by the string fields sort cache
        sort_string_table: Memory used by the sort cache string table
        evaluator_long_fields: Memory used by the long field evaluators
        evaluator_long64fields: Memory used by the 64 bits long field evaluators
        evaluator_date_fields: Memory used by the date field evaluators
        evaluator_double_fields: Memory used by the double field evaluators
        word_corrector_lexicon: Memory used by the word corrector lexicon structure
        facets: Memory used by the facets structure
        stem_expansion_map: Memory used by the stem expansion map structure
        total: Total memory used by the lexicon
    """

    b_tree_caches: Opt[int] = None
    facets_cache: Opt[int] = None
    terms_cache: Opt[int] = None
    term_ids_cache: Opt[int] = attrib(default=None, metadata={CASING: "TermIDsCache"})
    sort_cache_num_fields: Opt[int] = None
    sort_cache_string_fields: Opt[int] = None
    sort_string_table: Opt[int] = None
    evaluator_long_fields: Opt[int] = None
    evaluator_long64fields: Opt[int] = attrib(default=None, metadata={CASING: "EvaluatorLong64Fields"})
    evaluator_date_fields: Opt[int] = None
    evaluator_double_fields: Opt[int] = None
    word_corrector_lexicon: Opt[int] = None
    facets: Opt[int] = None
    stem_expansion_map: Opt[int] = None
    total: Opt[int] = None

    def __init__(
        self,
        *,
        b_tree_caches: Opt[int] = None,
        facets_cache: Opt[int] = None,
        terms_cache: Opt[int] = None,
        term_ids_cache: Opt[int] = attrib(default=None, metadata={CASING: "TermIDsCache"}),
        sort_cache_num_fields: Opt[int] = None,
        sort_cache_string_fields: Opt[int] = None,
        sort_string_table: Opt[int] = None,
        evaluator_long_fields: Opt[int] = None,
        evaluator_long64fields: Opt[int] = attrib(default=None, metadata={CASING: "EvaluatorLong64Fields"}),
        evaluator_date_fields: Opt[int] = None,
        evaluator_double_fields: Opt[int] = None,
        word_corrector_lexicon: Opt[int] = None,
        facets: Opt[int] = None,
        stem_expansion_map: Opt[int] = None,
        total: Opt[int] = None,
    ) -> None:
        """

        Parameters:
            b_tree_caches: Memory used by the BTree caches
            facets_cache: Memory used by the facets cache
            terms_cache: Memory used by the terms cache
            term_ids_cache: Memory used by the string to identifier mapping cache
            sort_cache_num_fields: Memory used by the numerical fields sort cache
            sort_cache_string_fields: Memory used by the string fields sort cache
            sort_string_table: Memory used by the sort cache string table
            evaluator_long_fields: Memory used by the long field evaluators
            evaluator_long64fields: Memory used by the 64 bits long field evaluators
            evaluator_date_fields: Memory used by the date field evaluators
            evaluator_double_fields: Memory used by the double field evaluators
            word_corrector_lexicon: Memory used by the word corrector lexicon structure
            facets: Memory used by the facets structure
            stem_expansion_map: Memory used by the stem expansion map structure
            total: Total memory used by the lexicon
        """


@attrs(kw_only=True, auto_attribs=True)
class MemoryBreakdown(JidType, hint="Coveo.IndexTracking.MemoryBreakdown"):
    """All the memory used by indexing structures

    Attributes:
        facet_lookup_cache: Memory used by the facet lookup cache
        expression_cache: Memory used by the expressions cache
        documents_cache: Memory used by the documents cache
        transaction_writer: Memory used by the transaction writer
        transaction_optimizer: Memory used by the transaction optimizer
        transaction_reader: Memory used by the transaction reader
        lexicon: Memory used by the lexicon (including facets)
        authorization_manager: Memory used by the authorization manager
        indexed_documents: Memory used by the indexed documents structure
        collections: Memory used by the collections structure
        file_security: Memory used by the file security structure and cache
        ranking: Memory used by the ranking engine
        total: Total memory used by the index structures
    """

    facet_lookup_cache: Opt[int] = None
    expression_cache: Opt[int] = None
    documents_cache: Opt[int] = None
    transaction_writer: Opt[int] = None
    transaction_optimizer: Opt[int] = None
    transaction_reader: Opt[int] = None
    lexicon: Opt[LexiconMemoryBreakdown] = None
    authorization_manager: Opt[int] = None
    indexed_documents: Opt[int] = None
    collections: Opt[int] = None
    file_security: Opt[int] = None
    ranking: Opt[int] = None
    total: Opt[int] = None

    def __init__(
        self,
        *,
        facet_lookup_cache: Opt[int] = None,
        expression_cache: Opt[int] = None,
        documents_cache: Opt[int] = None,
        transaction_writer: Opt[int] = None,
        transaction_optimizer: Opt[int] = None,
        transaction_reader: Opt[int] = None,
        lexicon: Opt[LexiconMemoryBreakdown] = None,
        authorization_manager: Opt[int] = None,
        indexed_documents: Opt[int] = None,
        collections: Opt[int] = None,
        file_security: Opt[int] = None,
        ranking: Opt[int] = None,
        total: Opt[int] = None,
    ) -> None:
        """

        Parameters:
            facet_lookup_cache: Memory used by the facet lookup cache
            expression_cache: Memory used by the expressions cache
            documents_cache: Memory used by the documents cache
            transaction_writer: Memory used by the transaction writer
            transaction_optimizer: Memory used by the transaction optimizer
            transaction_reader: Memory used by the transaction reader
            lexicon: Memory used by the lexicon (including facets)
            authorization_manager: Memory used by the authorization manager
            indexed_documents: Memory used by the indexed documents structure
            collections: Memory used by the collections structure
            file_security: Memory used by the file security structure and cache
            ranking: Memory used by the ranking engine
            total: Total memory used by the index structures
        """


@attrs(kw_only=True, auto_attribs=True)
class IndexSliceStatus(JidType, hint="Coveo.IndexTracking.IndexSliceStatus"):
    """Status of an index slice

    Attributes:
        slice_id: Slice ID
        last_transactions_application: Date/time of last application of transactions in the slice
        visibility_delay: Time in seconds between creating and applying the the most recent transaction
        documents_fragmentation: Percentage between 0 and 100 of fragmentation for document-based structures
    """

    slice_id: Opt[int] = None
    last_transactions_application: Opt[datetime] = None
    visibility_delay: Opt[int] = None
    documents_fragmentation: Opt[int] = None

    def __init__(
        self,
        *,
        slice_id: Opt[int] = None,
        last_transactions_application: Opt[datetime] = None,
        visibility_delay: Opt[int] = None,
        documents_fragmentation: Opt[int] = None,
    ) -> None:
        """

        Parameters:
            slice_id: Slice ID
            last_transactions_application: Date/time of last application of transactions in the slice
            visibility_delay: Time in seconds between creating and applying the the most recent transaction
            documents_fragmentation: Percentage between 0 and 100 of fragmentation for document-based structures
        """


@attrs(kw_only=True, auto_attribs=True)
class IndexStatus(StatusEntry, hint="Coveo.IndexTracking.IndexStatus"):
    """Status entry sent by the Indexer blade

    Attributes:
        pending_pre_transactions: Total number of pending pre-transactions waiting to be optimized
        pending_transactions: Total number of pending transactions waiting to be applied
        disk_space_used: Total disk space used by the index for all slices
        remaining_disk_space: The remaining disk space on the index drive.
        total_memory_used: Total memory used by all the index structures (excluding realtime indexing)
        document_count: Total number of documents in the index
        document_total_size: Total size of documents in the index
        pending_docs_to_add: Total number of documents waiting to be added in transactions
        pending_docs_to_update: Total number of documents waiting to be updated in transactions
        pending_docs_to_delete: Total number of documents waiting to be deleted in transactions
        visibility_delay: Time in seconds between creating and applying the the most recent transaction
        realtime_pending_pre_transactions: Total number of pending pre-transactions waiting to be optimized in the realtime portion of the index
        realtime_pending_transactions: Total number of pending transactions waiting to be applied in the realtime portion of the index
        realtime_disk_space_used: Total disk space used by the realtime portion of the index
        realtime_total_memory_used: Total memory used by all the realtime index structures
        realtime_document_count: Total number of documents in the realtime portion of the index
        realtime_document_total_size: Total size of documents in the realtime portion of the index
        realtime_pending_docs_to_add: Total number of documents waiting to be added in transactions in the realtime portion of the index
        realtime_pending_docs_to_update: Total number of documents waiting to be updated in transactions in the realtime portion of the index
        realtime_pending_docs_to_delete: Total number of documents waiting to be deleted in transactions in the realtime portion of the index
        realtime_visibility_delay: Time in seconds between creating and applying the the most recent transaction in the realtime portion of the index
        fragmentation_level: Index fragmentation level
        last_commit: Date/time of last Commit operation in Indexer blade (for pre-transactions)
        sources: Status of each index source
        slices: Status of each index slice
        resident_set_size: Resident set size for the process
        virtual_memory_size: Virtual memory size for the process
        peak_resident_set_size: Peak resident set size for the process
        peak_virtual_memory_size: Peak virtual memory size for the process
        total_physical_memory: Total physical memory on the server
        total_disk_space: Total disk space on the index drive
        total_ocr_pages: The total number of pages that were extracted by the OCR module for documents
        documents_fragmentation: Percentage between 0 and 100 of fragmentation for document-based structures
    """

    pending_pre_transactions: Opt[int] = None
    pending_transactions: Opt[int] = None
    disk_space_used: Opt[int] = None
    remaining_disk_space: Opt[int] = None
    total_memory_used: Opt[MemoryBreakdown] = None
    document_count: Opt[int] = None
    document_total_size: Opt[int] = None
    pending_docs_to_add: Opt[int] = None
    pending_docs_to_update: Opt[int] = None
    pending_docs_to_delete: Opt[int] = None
    visibility_delay: Opt[int] = None
    realtime_pending_pre_transactions: Opt[int] = None
    realtime_pending_transactions: Opt[int] = None
    realtime_disk_space_used: Opt[int] = None
    realtime_total_memory_used: Opt[MemoryBreakdown] = None
    realtime_document_count: Opt[int] = None
    realtime_document_total_size: Opt[int] = None
    realtime_pending_docs_to_add: Opt[int] = None
    realtime_pending_docs_to_update: Opt[int] = None
    realtime_pending_docs_to_delete: Opt[int] = None
    realtime_visibility_delay: Opt[int] = None
    fragmentation_level: Opt[int] = None
    last_commit: Opt[datetime] = None
    sources: Opt[List[IndexSourceStatus]] = None
    slices: Opt[List[IndexSliceStatus]] = None
    resident_set_size: Opt[int] = None
    virtual_memory_size: Opt[int] = None
    peak_resident_set_size: Opt[int] = None
    peak_virtual_memory_size: Opt[int] = None
    total_physical_memory: Opt[int] = None
    total_disk_space: Opt[int] = None
    total_ocr_pages: Opt[int] = None
    documents_fragmentation: Opt[int] = None

    def __init__(
        self,
        *,
        pending_pre_transactions: Opt[int] = None,
        pending_transactions: Opt[int] = None,
        disk_space_used: Opt[int] = None,
        remaining_disk_space: Opt[int] = None,
        total_memory_used: Opt[MemoryBreakdown] = None,
        document_count: Opt[int] = None,
        document_total_size: Opt[int] = None,
        pending_docs_to_add: Opt[int] = None,
        pending_docs_to_update: Opt[int] = None,
        pending_docs_to_delete: Opt[int] = None,
        visibility_delay: Opt[int] = None,
        realtime_pending_pre_transactions: Opt[int] = None,
        realtime_pending_transactions: Opt[int] = None,
        realtime_disk_space_used: Opt[int] = None,
        realtime_total_memory_used: Opt[MemoryBreakdown] = None,
        realtime_document_count: Opt[int] = None,
        realtime_document_total_size: Opt[int] = None,
        realtime_pending_docs_to_add: Opt[int] = None,
        realtime_pending_docs_to_update: Opt[int] = None,
        realtime_pending_docs_to_delete: Opt[int] = None,
        realtime_visibility_delay: Opt[int] = None,
        fragmentation_level: Opt[int] = None,
        last_commit: Opt[datetime] = None,
        sources: Opt[List[IndexSourceStatus]] = None,
        slices: Opt[List[IndexSliceStatus]] = None,
        resident_set_size: Opt[int] = None,
        virtual_memory_size: Opt[int] = None,
        peak_resident_set_size: Opt[int] = None,
        peak_virtual_memory_size: Opt[int] = None,
        total_physical_memory: Opt[int] = None,
        total_disk_space: Opt[int] = None,
        total_ocr_pages: Opt[int] = None,
        documents_fragmentation: Opt[int] = None,
    ) -> None:
        """

        Parameters:
            pending_pre_transactions: Total number of pending pre-transactions waiting to be optimized
            pending_transactions: Total number of pending transactions waiting to be applied
            disk_space_used: Total disk space used by the index for all slices
            remaining_disk_space: The remaining disk space on the index drive.
            total_memory_used: Total memory used by all the index structures (excluding realtime indexing)
            document_count: Total number of documents in the index
            document_total_size: Total size of documents in the index
            pending_docs_to_add: Total number of documents waiting to be added in transactions
            pending_docs_to_update: Total number of documents waiting to be updated in transactions
            pending_docs_to_delete: Total number of documents waiting to be deleted in transactions
            visibility_delay: Time in seconds between creating and applying the the most recent transaction
            realtime_pending_pre_transactions: Total number of pending pre-transactions waiting to be optimized in the realtime portion of the index
            realtime_pending_transactions: Total number of pending transactions waiting to be applied in the realtime portion of the index
            realtime_disk_space_used: Total disk space used by the realtime portion of the index
            realtime_total_memory_used: Total memory used by all the realtime index structures
            realtime_document_count: Total number of documents in the realtime portion of the index
            realtime_document_total_size: Total size of documents in the realtime portion of the index
            realtime_pending_docs_to_add: Total number of documents waiting to be added in transactions in the realtime portion of the index
            realtime_pending_docs_to_update: Total number of documents waiting to be updated in transactions in the realtime portion of the index
            realtime_pending_docs_to_delete: Total number of documents waiting to be deleted in transactions in the realtime portion of the index
            realtime_visibility_delay: Time in seconds between creating and applying the the most recent transaction in the realtime portion of the index
            fragmentation_level: Index fragmentation level
            last_commit: Date/time of last Commit operation in Indexer blade (for pre-transactions)
            sources: Status of each index source
            slices: Status of each index slice
            resident_set_size: Resident set size for the process
            virtual_memory_size: Virtual memory size for the process
            peak_resident_set_size: Peak resident set size for the process
            peak_virtual_memory_size: Peak virtual memory size for the process
            total_physical_memory: Total physical memory on the server
            total_disk_space: Total disk space on the index drive
            total_ocr_pages: The total number of pages that were extracted by the OCR module for documents
            documents_fragmentation: Percentage between 0 and 100 of fragmentation for document-based structures
        """


class IndexMetricOperation(JidEnumFlag):
    """Type of operation that can send metrics in the Indexer blade

    Attributes:
        Added: One or more documents were added
        Updated: One or more documents were updated
        Deleted: One or more documents were deleted
    """

    Added: int = auto()
    Updated: int = auto()
    Deleted: int = auto()


class IndexMetricStatus(JidEnumFlag):
    """Status of an Indexer blade metric, depending on where it is sent in the indexing process

    Attributes:
        Received: Operation was received by the Indexer blade and added to a transaction
        Finished: Operation has been applied to the index and is now completed
    """

    Received: int = auto()
    Finished: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class BaseIndexerMetric(MetricEntry, hint="Coveo.IndexTracking.BaseIndexerMetric"):
    """Base metric entry class used for all metric entries sent by the Indexer blade

    Attributes:
        instance_id: ID of the Indexer instance sending the metric
    """

    instance_id: Opt[str] = None

    def __init__(self, *, instance_id: Opt[str] = None) -> None:
        """

        Parameters:
            instance_id: ID of the Indexer instance sending the metric
        """


@attrs(kw_only=True, auto_attribs=True)
class IndexMetric(BaseIndexerMetric, hint="Coveo.IndexTracking.IndexMetric"):
    """Metric entry sent by the Indexer blade during indexing operations

    Attributes:
        source_operation_id: ID of source operation bound to the metric
        slice_id: ID of slice that received the operation
        collection_id: ID of collection containing affected source
        source_id: ID of affected source
        operation: Type of operation performed
        status: Status of the operation (depending on where it is sent in the indexing process)
        count: Number of affected documents
        size: Total size of affected documents
        error: Error message if the operation failed
    """

    source_operation_id: Opt[str] = None
    slice_id: Opt[int] = None
    collection_id: Opt[int] = None
    source_id: Opt[int] = None
    operation: Opt[IndexMetricOperation] = None
    status: Opt[IndexMetricStatus] = None
    count: Opt[int] = None
    size: Opt[int] = None
    error: Opt[str] = None

    def __init__(
        self,
        *,
        source_operation_id: Opt[str] = None,
        slice_id: Opt[int] = None,
        collection_id: Opt[int] = None,
        source_id: Opt[int] = None,
        operation: Opt[IndexMetricOperation] = None,
        status: Opt[IndexMetricStatus] = None,
        count: Opt[int] = None,
        size: Opt[int] = None,
        error: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            source_operation_id: ID of source operation bound to the metric
            slice_id: ID of slice that received the operation
            collection_id: ID of collection containing affected source
            source_id: ID of affected source
            operation: Type of operation performed
            status: Status of the operation (depending on where it is sent in the indexing process)
            count: Number of affected documents
            size: Total size of affected documents
            error: Error message if the operation failed
        """


@attrs(kw_only=True, auto_attribs=True)
class QueryMetric(BaseIndexerMetric, hint="Coveo.IndexTracking.QueryMetric"):
    """Metric entry sent by the Indexer blade during queries

    Attributes:
        matches: Number of matching documents
        filtered_matches: Number of matching documents once filtering has been performed
        duration: Total query duration, in seconds
        query_cpu_time: Duration of the actual query execution, excluding waiting time before being processed
    """

    matches: Opt[int] = None
    filtered_matches: Opt[int] = None
    duration: Opt[float] = None
    query_cpu_time: Opt[float] = attrib(default=None, metadata={CASING: "QueryCPUTime"})

    def __init__(
        self,
        *,
        matches: Opt[int] = None,
        filtered_matches: Opt[int] = None,
        duration: Opt[float] = None,
        query_cpu_time: Opt[float] = attrib(default=None, metadata={CASING: "QueryCPUTime"}),
    ) -> None:
        """

        Parameters:
            matches: Number of matching documents
            filtered_matches: Number of matching documents once filtering has been performed
            duration: Total query duration, in seconds
            query_cpu_time: Duration of the actual query execution, excluding waiting time before being processed
        """


@attrs(kw_only=True, auto_attribs=True)
class IntervalQueryMetric(BaseIndexerMetric, hint="Coveo.IndexTracking.IntervalQueryMetric"):
    """Query metrics for an interval of time

    Attributes:
        nb_query: Number of queries for that time period
        avg_duration: Average query duration, in seconds
    """

    nb_query: Opt[int] = None
    avg_duration: Opt[float] = None

    def __init__(self, *, nb_query: Opt[int] = None, avg_duration: Opt[float] = None) -> None:
        """

        Parameters:
            nb_query: Number of queries for that time period
            avg_duration: Average query duration, in seconds
        """
