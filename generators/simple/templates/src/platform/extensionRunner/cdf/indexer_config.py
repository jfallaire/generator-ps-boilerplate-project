"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/IndexerBladeConfig.jid

"""

from attr import attrib, attrs
from enum import auto
from typing import List, Optional as Opt
from .root import CASING, JidEnumFlag, JidType
from .security_provider import SIDDeclarator


class PriorityType(JidEnumFlag):
    """TODO"""

    Highest: int = auto()
    AboveNormal: int = auto()
    Normal: int = auto()
    BelowNormal: int = auto()
    Lowest: int = auto()


class PerformanceModeType(JidEnumFlag):
    """TODO

    Attributes:
        Index: TODO
        Query: TODO
        IndexAndQuery: TODO
    """

    Index: int = auto()
    Query: int = auto()
    IndexAndQuery: int = auto()


class IndexingBlockerModeType(JidEnumFlag):
    """TODO"""

    Disabled: int = auto()
    MinimumBlocking: int = auto()
    NormalBlocking: int = auto()
    MaximumBlocking: int = auto()


class StreamCompressionMethodType(JidEnumFlag):
    """TODO"""

    ZLib: int = auto()
    LZMA: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class ConfigSIDDeclarator(SIDDeclarator, hint="Coveo.IndexConfig.ConfigSIDDeclarator"):
    """

    Attributes:
        id_: TODO
    """

    id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"})

    def __init__(self, *, id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"})) -> None:
        """

        Parameters:
            id_: TODO
        """


@attrs(kw_only=True, auto_attribs=True)
class Slice(JidType, hint="Coveo.IndexConfig.Slice"):
    """TODO

    Attributes:
        id_: Between 0 and 32767.
        name: Length between 1 and 192 (readonly)
        description: Length at most 5000
        lexicon_cache_size: At least 1024
        lexicon_string_cf_cache_size: At least 1024
        lexicon_tag_cf_cache_size: At least 1024
        lexicon_double_cf_cache_size: At least 1024
        lexicon_long_cf_cache_size: At least 1024
        lexicon_long64cf_cache_size: At least 1024
        lexicon_date_cf_cache_size: At least 1024
        lexicon_field_sort_cache_size: At least 1024
        lexicon_group_by_cache_size: At least 1024
        lexicon_query_field_sort_cache_size: At least 1024
        wcl_min_occurrences: At least 1
        wcl_max_words: Between 1000 and 100000000
        security_index_cache_size: At least 1024
        security_info_cache_size: At least 1024
        query_cache_size: At least 1024
        documents_cache_size: At least 1024
        external_security_cache_size: At least 1024
        term_id_cache_size: At least 1024
        tag_value_cache_size: At least 1024
        stem_expansion_map_cache_size: At least 1024
        performance_cache_memory: Between 0.01 and 0.90
        auto_index_compaction_history_size: Between 0 and 365
    """

    id_: int = attrib(default=32767, metadata={CASING: "Id"})
    name: str = "SliceName"
    description: Opt[str] = None
    lexicon_cache_size: int = 10485760
    lexicon_string_cf_cache_size: int = attrib(default=1048576, metadata={CASING: "LexiconStringCFCacheSize"})
    lexicon_tag_cf_cache_size: int = attrib(default=262144, metadata={CASING: "LexiconTagCFCacheSize"})
    lexicon_double_cf_cache_size: int = attrib(default=262144, metadata={CASING: "LexiconDoubleCFCacheSize"})
    lexicon_long_cf_cache_size: int = attrib(default=262144, metadata={CASING: "LexiconLongCFCacheSize"})
    lexicon_long64cf_cache_size: int = attrib(default=262144, metadata={CASING: "LexiconLong64CFCacheSize"})
    lexicon_date_cf_cache_size: int = attrib(default=262144, metadata={CASING: "LexiconDateCFCacheSize"})
    lexicon_field_sort_cache_size: int = 262144
    lexicon_group_by_cache_size: int = 8388608
    lexicon_query_field_sort_cache_size: int = 1048576
    wcl_min_occurrences: int = attrib(default=5, metadata={CASING: "WCLMinOccurrences"})
    wcl_max_words: int = attrib(default=2000000, metadata={CASING: "WCLMaxWords"})
    security_index_cache_size: int = 1048576
    security_info_cache_size: int = 33554432
    query_cache_size: int = 33554432
    documents_cache_size: int = 268435456
    external_security_cache_size: int = 2097152
    term_id_cache_size: int = attrib(default=2097152, metadata={CASING: "TermIDCacheSize"})
    tag_value_cache_size: int = 4194304
    stem_expansion_map_cache_size: int = 4194304
    performance_cache_memory: float = 0.2
    auto_index_compaction_history_size: int = 10

    def __init__(
        self,
        *,
        id_: int = attrib(default=32767, metadata={CASING: "Id"}),
        name: str = "SliceName",
        description: Opt[str] = None,
        lexicon_cache_size: int = 10485760,
        lexicon_string_cf_cache_size: int = attrib(default=1048576, metadata={CASING: "LexiconStringCFCacheSize"}),
        lexicon_tag_cf_cache_size: int = attrib(default=262144, metadata={CASING: "LexiconTagCFCacheSize"}),
        lexicon_double_cf_cache_size: int = attrib(default=262144, metadata={CASING: "LexiconDoubleCFCacheSize"}),
        lexicon_long_cf_cache_size: int = attrib(default=262144, metadata={CASING: "LexiconLongCFCacheSize"}),
        lexicon_long64cf_cache_size: int = attrib(default=262144, metadata={CASING: "LexiconLong64CFCacheSize"}),
        lexicon_date_cf_cache_size: int = attrib(default=262144, metadata={CASING: "LexiconDateCFCacheSize"}),
        lexicon_field_sort_cache_size: int = 262144,
        lexicon_group_by_cache_size: int = 8388608,
        lexicon_query_field_sort_cache_size: int = 1048576,
        wcl_min_occurrences: int = attrib(default=5, metadata={CASING: "WCLMinOccurrences"}),
        wcl_max_words: int = attrib(default=2000000, metadata={CASING: "WCLMaxWords"}),
        security_index_cache_size: int = 1048576,
        security_info_cache_size: int = 33554432,
        query_cache_size: int = 33554432,
        documents_cache_size: int = 268435456,
        external_security_cache_size: int = 2097152,
        term_id_cache_size: int = attrib(default=2097152, metadata={CASING: "TermIDCacheSize"}),
        tag_value_cache_size: int = 4194304,
        stem_expansion_map_cache_size: int = 4194304,
        performance_cache_memory: float = 0.2,
        auto_index_compaction_history_size: int = 10,
    ) -> None:
        """

        Parameters:
            id_: Between 0 and 32767.
            name: Length between 1 and 192 (readonly)
            description: Length at most 5000
            lexicon_cache_size: At least 1024
            lexicon_string_cf_cache_size: At least 1024
            lexicon_tag_cf_cache_size: At least 1024
            lexicon_double_cf_cache_size: At least 1024
            lexicon_long_cf_cache_size: At least 1024
            lexicon_long64cf_cache_size: At least 1024
            lexicon_date_cf_cache_size: At least 1024
            lexicon_field_sort_cache_size: At least 1024
            lexicon_group_by_cache_size: At least 1024
            lexicon_query_field_sort_cache_size: At least 1024
            wcl_min_occurrences: At least 1
            wcl_max_words: Between 1000 and 100000000
            security_index_cache_size: At least 1024
            security_info_cache_size: At least 1024
            query_cache_size: At least 1024
            documents_cache_size: At least 1024
            external_security_cache_size: At least 1024
            term_id_cache_size: At least 1024
            tag_value_cache_size: At least 1024
            stem_expansion_map_cache_size: At least 1024
            performance_cache_memory: Between 0.01 and 0.90
            auto_index_compaction_history_size: Between 0 and 365
        """


class SourceReputationType(JidEnumFlag):
    """TODO"""

    Lowest: int = auto()
    Low: int = auto()
    BelowMedium: int = auto()
    Medium: int = auto()
    AboveMedium: int = auto()
    High: int = auto()
    Higher: int = auto()
    Highest: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class Source(JidType, hint="Coveo.IndexConfig.Source"):
    """TODO

    Attributes:
        id_: TODO
        name: Length between 1 and 512
        crawler: Length between 1 and 512
        image_minimum_size: TODO
        max_ht_ml_output_size: TODO
        min_data_size_for_duplicate_check: TODO
        reputation: TODO
        style_sheet_file_name: TODO
        style_sheet_is_merged: TODO
    """

    id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"})
    name: str = "SourceName"
    crawler: str = "Web"
    image_minimum_size: int = 32
    max_ht_ml_output_size: int = attrib(default=10485760, metadata={CASING: "MaxHTMLOutputSize"})
    min_data_size_for_duplicate_check: int = 4096
    reputation: SourceReputationType = SourceReputationType.Medium
    style_sheet_file_name: str = "cachedpage.css"
    style_sheet_is_merged: Opt[bool] = None

    def __init__(
        self,
        *,
        id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"}),
        name: str = "SourceName",
        crawler: str = "Web",
        image_minimum_size: int = 32,
        max_ht_ml_output_size: int = attrib(default=10485760, metadata={CASING: "MaxHTMLOutputSize"}),
        min_data_size_for_duplicate_check: int = 4096,
        reputation: SourceReputationType = SourceReputationType.Medium,
        style_sheet_file_name: str = "cachedpage.css",
        style_sheet_is_merged: Opt[bool] = None,
    ) -> None:
        """

        Parameters:
            id_: TODO
            name: Length between 1 and 512
            crawler: Length between 1 and 512
            image_minimum_size: TODO
            max_ht_ml_output_size: TODO
            min_data_size_for_duplicate_check: TODO
            reputation: TODO
            style_sheet_file_name: TODO
            style_sheet_is_merged: TODO
        """


@attrs(kw_only=True, auto_attribs=True)
class Collection(JidType, hint="Coveo.IndexConfig.Collection"):
    """TODO

    Attributes:
        id_: TODO
        name: Length between 1 and 512
        sources: TODO
    """

    id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"})
    name: str = "CollectionName"
    sources: Opt[List[Source]] = None

    def __init__(
        self,
        *,
        id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"}),
        name: str = "CollectionName",
        sources: Opt[List[Source]] = None,
    ) -> None:
        """

        Parameters:
            id_: TODO
            name: Length between 1 and 512
            sources: TODO
        """


class RankingHeuristicType(JidEnumFlag):
    """TODO"""

    Precision: int = auto()
    Average: int = auto()
    Speed: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class Ranking(JidType, hint="Coveo.IndexConfig.Ranking"):
    """TODO

    Attributes:
        ranking_heuristic: TODO
        ranking_heuristic_use_index_size: TODO
        title_mult: Between 0 and 9
        concept_mult: Between 0 and 9
        summary_mult: Between 0 and 9
        uri_mult: Between 0 and 9
        formatted_mult: Between 0 and 9
        term_correlation_mult: Between 0 and 9
        term_casing_mult: Between 0 and 9
        quality_mult: Between 0 and 9
        doc_date_mult: Between 0 and 9
        link_rank_mult: Between 0 and 9
        tfi_df_mult: Between 0 and 9
        adjacency_mult: Between 0 and 9
        language_mult: Between 0 and 9
        source_reputation_mult: Between 0 and 9
        custom_document_weight_mult: Between 0 and 9
        number_of_results_to_refine: Between 2 and 10000
    """

    ranking_heuristic: RankingHeuristicType = RankingHeuristicType.Speed
    ranking_heuristic_use_index_size: bool = True
    title_mult: int = 5
    concept_mult: int = 5
    summary_mult: int = 5
    uri_mult: int = attrib(default=5, metadata={CASING: "URIMult"})
    formatted_mult: int = 5
    term_correlation_mult: int = 5
    term_casing_mult: int = 5
    quality_mult: int = 5
    doc_date_mult: int = 5
    link_rank_mult: int = 5
    tfi_df_mult: int = attrib(default=5, metadata={CASING: "TFIDFMult"})
    adjacency_mult: int = 5
    language_mult: int = 5
    source_reputation_mult: int = 5
    custom_document_weight_mult: int = 5
    number_of_results_to_refine: int = 100

    def __init__(
        self,
        *,
        ranking_heuristic: RankingHeuristicType = RankingHeuristicType.Speed,
        ranking_heuristic_use_index_size: bool = True,
        title_mult: int = 5,
        concept_mult: int = 5,
        summary_mult: int = 5,
        uri_mult: int = attrib(default=5, metadata={CASING: "URIMult"}),
        formatted_mult: int = 5,
        term_correlation_mult: int = 5,
        term_casing_mult: int = 5,
        quality_mult: int = 5,
        doc_date_mult: int = 5,
        link_rank_mult: int = 5,
        tfi_df_mult: int = attrib(default=5, metadata={CASING: "TFIDFMult"}),
        adjacency_mult: int = 5,
        language_mult: int = 5,
        source_reputation_mult: int = 5,
        custom_document_weight_mult: int = 5,
        number_of_results_to_refine: int = 100,
    ) -> None:
        """

        Parameters:
            ranking_heuristic: TODO
            ranking_heuristic_use_index_size: TODO
            title_mult: Between 0 and 9
            concept_mult: Between 0 and 9
            summary_mult: Between 0 and 9
            uri_mult: Between 0 and 9
            formatted_mult: Between 0 and 9
            term_correlation_mult: Between 0 and 9
            term_casing_mult: Between 0 and 9
            quality_mult: Between 0 and 9
            doc_date_mult: Between 0 and 9
            link_rank_mult: Between 0 and 9
            tfi_df_mult: Between 0 and 9
            adjacency_mult: Between 0 and 9
            language_mult: Between 0 and 9
            source_reputation_mult: Between 0 and 9
            custom_document_weight_mult: Between 0 and 9
            number_of_results_to_refine: Between 2 and 10000
        """


@attrs(kw_only=True, auto_attribs=True)
class HighlightTag(JidType, hint="Coveo.IndexConfig.HighlightTag"):
    """TODO

    Attributes:
        id_: TODO
        start: Length between 3 and 500
        end: Length between 3 and 500
    """

    id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"})
    start: str = "&lt;b style='color:black;background-color:#ffff66'&gt;"
    end: str = "&lt;/b&gt;"

    def __init__(
        self,
        *,
        id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"}),
        start: str = "&lt;b style='color:black;background-color:#ffff66'&gt;",
        end: str = "&lt;/b&gt;",
    ) -> None:
        """

        Parameters:
            id_: TODO
            start: Length between 3 and 500
            end: Length between 3 and 500
        """


@attrs(kw_only=True, auto_attribs=True)
class QueryHighlighter(JidType, hint="Coveo.IndexConfig.QueryHighlighter"):
    """TODO

    Attributes:
        use_stemming: TODO
        ignore_accents: TODO
        ignored_fields: Length at most 32768
        highlight_tags: TODO
    """

    use_stemming: bool = True
    ignore_accents: bool = True
    ignored_fields: Opt[str] = None
    highlight_tags: Opt[List[HighlightTag]] = None

    def __init__(
        self,
        *,
        use_stemming: bool = True,
        ignore_accents: bool = True,
        ignored_fields: Opt[str] = None,
        highlight_tags: Opt[List[HighlightTag]] = None,
    ) -> None:
        """

        Parameters:
            use_stemming: TODO
            ignore_accents: TODO
            ignored_fields: Length at most 32768
            highlight_tags: TODO
        """


@attrs(kw_only=True, auto_attribs=True)
class CollaborativeRanking(JidType, hint="Coveo.IndexConfig.CollaborativeRanking"):
    """TODO"""

    def __init__(self) -> None:
        ...


class FieldType(JidEnumFlag):
    """TODO"""

    Long: int = auto()
    Long64: int = auto()
    Double: int = auto()
    Date: int = auto()
    String: int = auto()


class FieldSourceType(JidEnumFlag):
    """TODO"""

    System: int = auto()
    Notes: int = auto()
    Exchange: int = auto()
    Mail: int = auto()
    Sharepoint: int = auto()
    User: int = auto()
    SalesForce: int = auto()
    Confluence: int = auto()
    DesktopConnector: int = auto()
    ClearSpace: int = auto()
    WebsphereWCM: int = auto()
    CRM: int = auto()
    Liferay: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class Field(JidType, hint="Coveo.IndexConfig.Field"):
    """TODO

    Attributes:
        id_: TODO
        name: Length between 1 and 256 (readonly)
        description: Length at most 5000
        native_field_name: Length at most 256
        field_type: TODO
        default_value: Length at most 50
        include_in_query: TODO
        include_in_results: TODO
        merge_with_lexicon: TODO
        smart_date_facet: TODO
        facet: TODO
        multi_value_facet: TODO
        sort: TODO
        ranking: TODO
        stemming: TODO
        use_cache_for_nested_query: TODO
        use_cache_for_sort: TODO
        use_cache_for_numeric_query: TODO
        use_cache_for_computed_facet: TODO
        multi_value_facet_tokenizers: TODO
        date_format: Length at most 50
        source_type: TODO
        hierarchical_facet: The field is a hierarchical multivalue facet
    """

    id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"})
    name: str = "FieldName"
    description: Opt[str] = None
    native_field_name: Opt[str] = None
    field_type: FieldType = FieldType.String
    default_value: Opt[str] = None
    include_in_query: Opt[bool] = None
    include_in_results: Opt[bool] = None
    merge_with_lexicon: Opt[bool] = None
    smart_date_facet: Opt[bool] = None
    facet: Opt[bool] = None
    multi_value_facet: Opt[bool] = None
    sort: Opt[bool] = None
    ranking: Opt[bool] = None
    stemming: Opt[bool] = None
    use_cache_for_nested_query: Opt[bool] = None
    use_cache_for_sort: Opt[bool] = None
    use_cache_for_numeric_query: Opt[bool] = None
    use_cache_for_computed_facet: Opt[bool] = None
    multi_value_facet_tokenizers: str = ";"
    date_format: Opt[str] = None
    source_type: FieldSourceType = FieldSourceType.System
    hierarchical_facet: Opt[bool] = None

    def __init__(
        self,
        *,
        id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"}),
        name: str = "FieldName",
        description: Opt[str] = None,
        native_field_name: Opt[str] = None,
        field_type: FieldType = FieldType.String,
        default_value: Opt[str] = None,
        include_in_query: Opt[bool] = None,
        include_in_results: Opt[bool] = None,
        merge_with_lexicon: Opt[bool] = None,
        smart_date_facet: Opt[bool] = None,
        facet: Opt[bool] = None,
        multi_value_facet: Opt[bool] = None,
        sort: Opt[bool] = None,
        ranking: Opt[bool] = None,
        stemming: Opt[bool] = None,
        use_cache_for_nested_query: Opt[bool] = None,
        use_cache_for_sort: Opt[bool] = None,
        use_cache_for_numeric_query: Opt[bool] = None,
        use_cache_for_computed_facet: Opt[bool] = None,
        multi_value_facet_tokenizers: str = ";",
        date_format: Opt[str] = None,
        source_type: FieldSourceType = FieldSourceType.System,
        hierarchical_facet: Opt[bool] = None,
    ) -> None:
        """

        Parameters:
            id_: TODO
            name: Length between 1 and 256 (readonly)
            description: Length at most 5000
            native_field_name: Length at most 256
            field_type: TODO
            default_value: Length at most 50
            include_in_query: TODO
            include_in_results: TODO
            merge_with_lexicon: TODO
            smart_date_facet: TODO
            facet: TODO
            multi_value_facet: TODO
            sort: TODO
            ranking: TODO
            stemming: TODO
            use_cache_for_nested_query: TODO
            use_cache_for_sort: TODO
            use_cache_for_numeric_query: TODO
            use_cache_for_computed_facet: TODO
            multi_value_facet_tokenizers: TODO
            date_format: Length at most 50
            source_type: TODO
            hierarchical_facet: The field is a hierarchical multivalue facet
        """


@attrs(kw_only=True, auto_attribs=True)
class TagField(JidType, hint="Coveo.IndexConfig.TagField"):
    """TODO

    Attributes:
        id_: TODO
        name: TODO (readonly field name)
        description: Length at most 5000
        read_write_users_list: TODO
        read_only_users_list: TODO
    """

    id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"})
    name: str = "FieldName"
    description: Opt[str] = None
    read_write_users_list: Opt[List[ConfigSIDDeclarator]] = None
    read_only_users_list: Opt[List[ConfigSIDDeclarator]] = None

    def __init__(
        self,
        *,
        id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"}),
        name: str = "FieldName",
        description: Opt[str] = None,
        read_write_users_list: Opt[List[ConfigSIDDeclarator]] = None,
        read_only_users_list: Opt[List[ConfigSIDDeclarator]] = None,
    ) -> None:
        """

        Parameters:
            id_: TODO
            name: TODO (readonly field name)
            description: Length at most 5000
            read_write_users_list: TODO
            read_only_users_list: TODO
        """


@attrs(kw_only=True, auto_attribs=True)
class ResultsPreviewer(JidType, hint="Coveo.IndexConfig.ResultsPreviewer"):
    """TODO

    Attributes:
        id_: TODO
        name: Length between 1 and 512
        valid_users: TODO
        filter_: Length at most 5000
    """

    id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"})
    name: str = "ResultsPreviewer"
    valid_users: Opt[List[ConfigSIDDeclarator]] = None
    filter_: Opt[str] = attrib(default=None, metadata={CASING: "Filter"})

    def __init__(
        self,
        *,
        id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"}),
        name: str = "ResultsPreviewer",
        valid_users: Opt[List[ConfigSIDDeclarator]] = None,
        filter_: Opt[str] = attrib(default=None, metadata={CASING: "Filter"}),
    ) -> None:
        """

        Parameters:
            id_: TODO
            name: Length between 1 and 512
            valid_users: TODO
            filter_: Length at most 5000
        """


@attrs(kw_only=True, auto_attribs=True)
class PhysicalIndex(JidType, hint="Coveo.IndexConfig.PhysicalIndex"):
    """TODO

    Attributes:
        name: Length between 1 and 512
        description: Length at most 5000
        apply_stemming_on_exact_phrase_terms: TODO
        wildcards_number_of_terms: At least 1
        wildcards_number_of_leading_chars: Between 0 and 65535
        group_by_max_to_cache: At least 1048576
        unique_terms_per_document: Between 65536 and 2097152
        languages_settings: Length between 0 and 67108864
        performance_cache_memory: Between 0.01 and 0.90
        enable_realtime_indexing: TODO
        realtime_indexing_documents_threshold: TODO
        realtime_indexing_start_threshold: TODO
        normalizer_unicode_set_exclusion: The set of unicode to exclude from the icu normalization process.
        allowed_sources: Regex used to reject documents according to source names
    """

    name: str = "Default"
    description: Opt[str] = None
    apply_stemming_on_exact_phrase_terms: Opt[bool] = None
    wildcards_number_of_terms: int = 32
    wildcards_number_of_leading_chars: int = 2
    group_by_max_to_cache: int = 134217728
    unique_terms_per_document: int = 1048576
    languages_settings: Opt[str] = None
    performance_cache_memory: float = 0.2
    enable_realtime_indexing: bool = True
    realtime_indexing_documents_threshold: int = 200000
    realtime_indexing_start_threshold: int = 1000000
    normalizer_unicode_set_exclusion: str = "[]"
    allowed_sources: Opt[str] = None

    def __init__(
        self,
        *,
        name: str = "Default",
        description: Opt[str] = None,
        apply_stemming_on_exact_phrase_terms: Opt[bool] = None,
        wildcards_number_of_terms: int = 32,
        wildcards_number_of_leading_chars: int = 2,
        group_by_max_to_cache: int = 134217728,
        unique_terms_per_document: int = 1048576,
        languages_settings: Opt[str] = None,
        performance_cache_memory: float = 0.2,
        enable_realtime_indexing: bool = True,
        realtime_indexing_documents_threshold: int = 200000,
        realtime_indexing_start_threshold: int = 1000000,
        normalizer_unicode_set_exclusion: str = "[]",
        allowed_sources: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            name: Length between 1 and 512
            description: Length at most 5000
            apply_stemming_on_exact_phrase_terms: TODO
            wildcards_number_of_terms: At least 1
            wildcards_number_of_leading_chars: Between 0 and 65535
            group_by_max_to_cache: At least 1048576
            unique_terms_per_document: Between 65536 and 2097152
            languages_settings: Length between 0 and 67108864
            performance_cache_memory: Between 0.01 and 0.90
            enable_realtime_indexing: TODO
            realtime_indexing_documents_threshold: TODO
            realtime_indexing_start_threshold: TODO
            normalizer_unicode_set_exclusion: The set of unicode to exclude from the icu normalization process.
            allowed_sources: Regex used to reject documents according to source names
        """


@attrs(kw_only=True, auto_attribs=True)
class System(JidType, hint="Coveo.IndexConfig.System"):
    """TODO

    Attributes:
        minimum_disk_space: Between 51200 and 10485760
        maximum_terms_per_query: Between 8 and 65536
        enable_word_corrector_lexicon: TODO
        number_of_query_threads: Between 0 and 256
        number_of_batch_query_threads: Between 0 and 256
        document_duplicate_factor: Between 0 and 100
        maximum_results: Between 100 and 50000
        transaction_update_frequency: Between 1 and 7200
        transaction_max_documents_size: At least 1048576
        document_limit_warning: Between 0 and 100
        performance_cache_memory: Between 0.01 and 0.90
        indexing_blocker_mode: TODO
        performance_minimum_cache_memory: At least 1048576
        limit_system_file_cache_size: TODO
        max_system_file_cache_size: Between 0.01 and 1.00
        system_file_cache_trim_interval: TODO
        enable_live_tagging: TODO
        enable_internal_live_tagging: TODO
        max_b_tree_flush_pending_memory_mb: TODO
        max_mmf_flush_pending_memory_mb: TODO
        max_chunks_cleanup_per_transaction_peak_period: Between 0.0 and 1.0
        max_chunks_cleanup_time_per_transaction_peak_period: Between 0.0 and 1.0
        terms_chunks_to_defragment_per_transaction_peak_period: At least 1
        max_term_defragmentation_time_peak_period: Between 0 and 3600
        max_term_defragmentation_time_percent_peak_period: Between 0.0 and 1.0
        max_doc_id_recycling_time_per_transaction_peak_period: Between 0 and 86400
        min_doc_id_count_for_recycling: At least 10000
        max_recycled_term_id_cleanup_time_peak_period: Between 0 and 86400
        max_recycled_term_id_cleanup_time_percent_peak_period: Between 0.0 and 1.0
        min_term_id_count_for_recycling: At least 10000
        recycling_threshold_multiplier_in_indexing_mode: Between 1.0 and 100.0
        documents_fragmentation_target: Between 0.0 and 1.0
        documents_chunk_to_defragment: At least 1
        stream_compression_method: TODO
        free_space_before_rebalancing_b_tree: Between 20 and 90
        free_space_before_rebalancing_b_tree_during_cleanup: Between 20 and 90
        enable_search_debug_argument: TODO
        enable_index_status: Enable index status reports to the StatusTracker
        enable_service_index_metrics: Enable indexing metrics sent when service receives commands
        enable_transactions_index_metrics: Enable indexing metrics when applying transactions
        enable_query_metrics: Enable query metrics
        query_metric_interval: The query metric interval in seconds
        security_entity_resolver_refresh_delay_s: The refresh lookup delay for the Security Entity Resolver, in seconds
        slow_query_threshold: Threshold to consider query as slow and log them in warning. Between 0.0 and 30.0
    """

    minimum_disk_space: int = 5242880
    maximum_terms_per_query: int = 128
    enable_word_corrector_lexicon: bool = True
    number_of_query_threads: Opt[int] = None
    number_of_batch_query_threads: Opt[int] = None
    document_duplicate_factor: int = 85
    maximum_results: int = 1000
    transaction_update_frequency: int = 60
    transaction_max_documents_size: int = 31457280
    document_limit_warning: int = 80
    performance_cache_memory: float = 0.5
    indexing_blocker_mode: IndexingBlockerModeType = IndexingBlockerModeType.NormalBlocking
    performance_minimum_cache_memory: int = 41943040
    limit_system_file_cache_size: bool = True
    max_system_file_cache_size: float = 0.25
    system_file_cache_trim_interval: int = 120
    enable_live_tagging: bool = True
    enable_internal_live_tagging: bool = True
    max_b_tree_flush_pending_memory_mb: Opt[int] = attrib(
        default=None, metadata={CASING: "MaxBTreeFlushPendingMemoryMB"}
    )
    max_mmf_flush_pending_memory_mb: Opt[int] = attrib(default=None, metadata={CASING: "MaxMMFFlushPendingMemoryMB"})
    max_chunks_cleanup_per_transaction_peak_period: float = 0.1
    max_chunks_cleanup_time_per_transaction_peak_period: float = 0.4
    terms_chunks_to_defragment_per_transaction_peak_period: int = 5
    max_term_defragmentation_time_peak_period: int = 5
    max_term_defragmentation_time_percent_peak_period: float = 0.1
    max_doc_id_recycling_time_per_transaction_peak_period: int = attrib(
        default=600, metadata={CASING: "MaxDocIDRecyclingTimePerTransactionPeakPeriod"}
    )
    min_doc_id_count_for_recycling: int = attrib(default=500000, metadata={CASING: "MinDocIDCountForRecycling"})
    max_recycled_term_id_cleanup_time_peak_period: int = attrib(
        default=90, metadata={CASING: "MaxRecycledTermIDCleanupTimePeakPeriod"}
    )
    max_recycled_term_id_cleanup_time_percent_peak_period: float = attrib(
        default=0.5, metadata={CASING: "MaxRecycledTermIDCleanupTimePercentPeakPeriod"}
    )
    min_term_id_count_for_recycling: int = attrib(default=500000, metadata={CASING: "MinTermIDCountForRecycling"})
    recycling_threshold_multiplier_in_indexing_mode: float = 10.0
    documents_fragmentation_target: float = 0.1
    documents_chunk_to_defragment: int = 10
    stream_compression_method: StreamCompressionMethodType = StreamCompressionMethodType.LZMA
    free_space_before_rebalancing_b_tree: int = 50
    free_space_before_rebalancing_b_tree_during_cleanup: int = 80
    enable_search_debug_argument: bool = True
    enable_index_status: bool = True
    enable_service_index_metrics: Opt[bool] = None
    enable_transactions_index_metrics: Opt[bool] = None
    enable_query_metrics: bool = True
    query_metric_interval: int = 300
    security_entity_resolver_refresh_delay_s: int = attrib(
        default=5, metadata={CASING: "SecurityEntityResolverRefreshDelay_s"}
    )
    slow_query_threshold: float = 2.0

    def __init__(
        self,
        *,
        minimum_disk_space: int = 5242880,
        maximum_terms_per_query: int = 128,
        enable_word_corrector_lexicon: bool = True,
        number_of_query_threads: Opt[int] = None,
        number_of_batch_query_threads: Opt[int] = None,
        document_duplicate_factor: int = 85,
        maximum_results: int = 1000,
        transaction_update_frequency: int = 60,
        transaction_max_documents_size: int = 31457280,
        document_limit_warning: int = 80,
        performance_cache_memory: float = 0.5,
        indexing_blocker_mode: IndexingBlockerModeType = IndexingBlockerModeType.NormalBlocking,
        performance_minimum_cache_memory: int = 41943040,
        limit_system_file_cache_size: bool = True,
        max_system_file_cache_size: float = 0.25,
        system_file_cache_trim_interval: int = 120,
        enable_live_tagging: bool = True,
        enable_internal_live_tagging: bool = True,
        max_b_tree_flush_pending_memory_mb: Opt[int] = attrib(
            default=None, metadata={CASING: "MaxBTreeFlushPendingMemoryMB"}
        ),
        max_mmf_flush_pending_memory_mb: Opt[int] = attrib(
            default=None, metadata={CASING: "MaxMMFFlushPendingMemoryMB"}
        ),
        max_chunks_cleanup_per_transaction_peak_period: float = 0.1,
        max_chunks_cleanup_time_per_transaction_peak_period: float = 0.4,
        terms_chunks_to_defragment_per_transaction_peak_period: int = 5,
        max_term_defragmentation_time_peak_period: int = 5,
        max_term_defragmentation_time_percent_peak_period: float = 0.1,
        max_doc_id_recycling_time_per_transaction_peak_period: int = attrib(
            default=600, metadata={CASING: "MaxDocIDRecyclingTimePerTransactionPeakPeriod"}
        ),
        min_doc_id_count_for_recycling: int = attrib(default=500000, metadata={CASING: "MinDocIDCountForRecycling"}),
        max_recycled_term_id_cleanup_time_peak_period: int = attrib(
            default=90, metadata={CASING: "MaxRecycledTermIDCleanupTimePeakPeriod"}
        ),
        max_recycled_term_id_cleanup_time_percent_peak_period: float = attrib(
            default=0.5, metadata={CASING: "MaxRecycledTermIDCleanupTimePercentPeakPeriod"}
        ),
        min_term_id_count_for_recycling: int = attrib(default=500000, metadata={CASING: "MinTermIDCountForRecycling"}),
        recycling_threshold_multiplier_in_indexing_mode: float = 10.0,
        documents_fragmentation_target: float = 0.1,
        documents_chunk_to_defragment: int = 10,
        stream_compression_method: StreamCompressionMethodType = StreamCompressionMethodType.LZMA,
        free_space_before_rebalancing_b_tree: int = 50,
        free_space_before_rebalancing_b_tree_during_cleanup: int = 80,
        enable_search_debug_argument: bool = True,
        enable_index_status: bool = True,
        enable_service_index_metrics: Opt[bool] = None,
        enable_transactions_index_metrics: Opt[bool] = None,
        enable_query_metrics: bool = True,
        query_metric_interval: int = 300,
        security_entity_resolver_refresh_delay_s: int = attrib(
            default=5, metadata={CASING: "SecurityEntityResolverRefreshDelay_s"}
        ),
        slow_query_threshold: float = 2.0,
    ) -> None:
        """

        Parameters:
            minimum_disk_space: Between 51200 and 10485760
            maximum_terms_per_query: Between 8 and 65536
            enable_word_corrector_lexicon: TODO
            number_of_query_threads: Between 0 and 256
            number_of_batch_query_threads: Between 0 and 256
            document_duplicate_factor: Between 0 and 100
            maximum_results: Between 100 and 50000
            transaction_update_frequency: Between 1 and 7200
            transaction_max_documents_size: At least 1048576
            document_limit_warning: Between 0 and 100
            performance_cache_memory: Between 0.01 and 0.90
            indexing_blocker_mode: TODO
            performance_minimum_cache_memory: At least 1048576
            limit_system_file_cache_size: TODO
            max_system_file_cache_size: Between 0.01 and 1.00
            system_file_cache_trim_interval: TODO
            enable_live_tagging: TODO
            enable_internal_live_tagging: TODO
            max_b_tree_flush_pending_memory_mb: TODO
            max_mmf_flush_pending_memory_mb: TODO
            max_chunks_cleanup_per_transaction_peak_period: Between 0.0 and 1.0
            max_chunks_cleanup_time_per_transaction_peak_period: Between 0.0 and 1.0
            terms_chunks_to_defragment_per_transaction_peak_period: At least 1
            max_term_defragmentation_time_peak_period: Between 0 and 3600
            max_term_defragmentation_time_percent_peak_period: Between 0.0 and 1.0
            max_doc_id_recycling_time_per_transaction_peak_period: Between 0 and 86400
            min_doc_id_count_for_recycling: At least 10000
            max_recycled_term_id_cleanup_time_peak_period: Between 0 and 86400
            max_recycled_term_id_cleanup_time_percent_peak_period: Between 0.0 and 1.0
            min_term_id_count_for_recycling: At least 10000
            recycling_threshold_multiplier_in_indexing_mode: Between 1.0 and 100.0
            documents_fragmentation_target: Between 0.0 and 1.0
            documents_chunk_to_defragment: At least 1
            stream_compression_method: TODO
            free_space_before_rebalancing_b_tree: Between 20 and 90
            free_space_before_rebalancing_b_tree_during_cleanup: Between 20 and 90
            enable_search_debug_argument: TODO
            enable_index_status: Enable index status reports to the StatusTracker
            enable_service_index_metrics: Enable indexing metrics sent when service receives commands
            enable_transactions_index_metrics: Enable indexing metrics when applying transactions
            enable_query_metrics: Enable query metrics
            query_metric_interval: The query metric interval in seconds
            security_entity_resolver_refresh_delay_s: The refresh lookup delay for the Security Entity Resolver, in seconds
            slow_query_threshold: Threshold to consider query as slow and log them in warning. Between 0.0 and 30.0
        """


class NetworkAddressType(JidEnumFlag):
    """TODO"""

    IP: int = auto()
    FQDN: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class NetworkAddress(JidType, hint="Coveo.IndexConfig.NetworkAddress"):
    """TODO

    Attributes:
        id_: TODO
        address: TODO
        address_type: TODO
    """

    id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"})
    address: Opt[str] = None
    address_type: Opt[NetworkAddressType] = None

    def __init__(
        self,
        *,
        id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"}),
        address: Opt[str] = None,
        address_type: Opt[NetworkAddressType] = None,
    ) -> None:
        """

        Parameters:
            id_: TODO
            address: TODO
            address_type: TODO
        """


@attrs(kw_only=True, auto_attribs=True)
class SearchCertificate(JidType, hint="Coveo.IndexConfig.SearchCertificate"):
    """TODO

    Attributes:
        id_: TODO
        thumbprint: TODO (readonly)
        allowed_impersonated_user_ids: TODO
        allowed_network_addresses: TODO
        allowed_to_grant_super_user_mode: Whether this search certificate can grant super user mode
    """

    id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"})
    thumbprint: Opt[str] = None
    allowed_impersonated_user_ids: Opt[List[ConfigSIDDeclarator]] = attrib(
        default=None, metadata={CASING: "AllowedImpersonatedUserIDs"}
    )
    allowed_network_addresses: Opt[List[NetworkAddress]] = None
    allowed_to_grant_super_user_mode: Opt[bool] = None

    def __init__(
        self,
        *,
        id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"}),
        thumbprint: Opt[str] = None,
        allowed_impersonated_user_ids: Opt[List[ConfigSIDDeclarator]] = attrib(
            default=None, metadata={CASING: "AllowedImpersonatedUserIDs"}
        ),
        allowed_network_addresses: Opt[List[NetworkAddress]] = None,
        allowed_to_grant_super_user_mode: Opt[bool] = None,
    ) -> None:
        """

        Parameters:
            id_: TODO
            thumbprint: TODO (readonly)
            allowed_impersonated_user_ids: TODO
            allowed_network_addresses: TODO
            allowed_to_grant_super_user_mode: Whether this search certificate can grant super user mode
        """
