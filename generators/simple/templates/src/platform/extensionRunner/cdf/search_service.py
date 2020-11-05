"""
    - THIS FILE IS GENERATED -

CoveoServices/SearchService/CoveoSearchService.jid

"""

from attr import attrib, attrs
from datetime import datetime
from enum import auto
from typing import Any, Dict, List, Optional as Opt, Union
from .root import CASING, CoveoInterface, ExceptionBase, JidEnumFlag, JidType, api


@attrs(kw_only=True, auto_attribs=True)
class InvalidScopeException(ExceptionBase, hint="Coveo.SearchService.InvalidScopeException"):
    """Exception thrown when the specified scope is invalid."""

    def __init__(self) -> None:
        ...


class SortBy(JidEnumFlag):
    """List of sort criteria that may be used to sort results.

    Attributes:
        Relevancy: Sort by result relevancy, using the main ranking algorithm.
        CustomSortField: Sort by one or more custom field values. The name of the fields are specified through the <b>QueryParams.SortByFields</b> property.
        NoRanking: Do not sort results (documents will not be ranked).
        QRE: Will rank using Query ranking expressions only. See <b>QueryParams.RankingExpression</b>.
    """

    Relevancy: int = auto()
    CustomSortField: int = auto()
    NoRanking: int = auto()
    QRE: int = auto()


class FacetSortCriteria(JidEnumFlag):
    """List of sort criteria that may be used to sort the values of a field within the results of a query.

    Attributes:
        SortByOccurrence: Sort values by number of results that have this value.
        SortByScore: Sort values by score. The score is computed using the number of results having the value and the proximity of those results to the top of the result list.
        SortByScoreAlphaAscending: Sort values in ascending alphabetical order, but only the best ones.
        SortByScoreAlphaDescending: Sort values in descending alphabetical order, but only the best ones.
        SortByAlphaReturnAll: Sort values in ascending alphabetical order, possibly returning all values.
        SortByComputedFieldAscending: Sort values in ascending order of the result for a computed field.
        SortByComputedFieldDescending: Sort values in descending order of the result for a computed field.
        SortByNoSort: No sort.
        SortByChiSquare: Sort values using a chi-square statistical distribution.
        SortByAlphaAscending: Sort values in ascending alphabetical order, all values returned by injection.
        SortByAlphaDescending: Sort values in descending alphabetical order, all values returned by injection.
    """

    SortByOccurrence: int = auto()
    SortByScore: int = auto()
    SortByScoreAlphaAscending: int = auto()
    SortByScoreAlphaDescending: int = auto()
    SortByAlphaReturnAll: int = auto()
    SortByComputedFieldAscending: int = auto()
    SortByComputedFieldDescending: int = auto()
    SortByNoSort: int = auto()
    SortByChiSquare: int = auto()
    SortByAlphaAscending: int = auto()
    SortByAlphaDescending: int = auto()


class ComputedFieldOperation(JidEnumFlag):
    """List of possible numerical operations on computed fields.

    Attributes:
        NoOperation: No operation.
        Sum: The sum of all the values.
        Average: The average for all the values.
        Minimum: The lowest value.
        Maximum: The highest value.
        Median: The median value.
        Variance: The variance of the data set.
        StandardDeviation: The standard deviation of the data set.
    """

    NoOperation: int = auto()
    Sum: int = auto()
    Average: int = auto()
    Minimum: int = auto()
    Maximum: int = auto()
    Median: int = auto()
    Variance: int = auto()
    StandardDeviation: int = auto()


class ListFacetFieldValuesRequest(JidEnumFlag):
    """List of the possible ListFacetFieldValues request types.

    Attributes:
        Wildcards: Wildcards matching pattern.
        RegularExpression: Regular expression matching pattern.
        EditDistance: Edit distance fuzzy matching pattern.
        Phonetic: Phonetic matching pattern.
        Verbatim: Filter to be interpreted as such.
    """

    Wildcards: int = auto()
    RegularExpression: int = auto()
    EditDistance: int = auto()
    Phonetic: int = auto()
    Verbatim: int = auto()


class HealthCheckStatusType(JidEnumFlag):
    """List of the possible HealthCheck return values.

    Attributes:
        Healthy: Search is healthy.
        QueriesAreDisabled: Queries are disabled.
        Other: Other, search is NOT healthy.
    """

    Healthy: int = auto()
    QueriesAreDisabled: int = auto()
    Other: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class HealthCheckStatus(JidType, hint="Coveo.SearchService.HealthCheckStatus"):
    """Return value for the health check call.

    Attributes:
        type_: The optional name of the field to use for sorting results.
        description: Whether to sort ascending or descending.
    """

    type_: Opt[HealthCheckStatusType] = attrib(default=None, metadata={CASING: "Type"})
    description: Opt[str] = None

    def __init__(
        self,
        *,
        type_: Opt[HealthCheckStatusType] = attrib(default=None, metadata={CASING: "Type"}),
        description: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            type_: The optional name of the field to use for sorting results.
            description: Whether to sort ascending or descending.
        """


@attrs(kw_only=True, auto_attribs=True)
class SortByField(JidType, hint="Coveo.SearchService.SortByField"):
    """Used to sort results using additional sort order.

    Attributes:
        field_name: The optional name of the field to use for sorting results.
        ascending: Whether to sort ascending or descending.
    """

    field_name: Opt[str] = None
    ascending: Opt[bool] = None

    def __init__(self, *, field_name: Opt[str] = None, ascending: Opt[bool] = None) -> None:
        """

        Parameters:
            field_name: The optional name of the field to use for sorting results.
            ascending: Whether to sort ascending or descending.
        """


@attrs(kw_only=True, auto_attribs=True)
class ComputedFieldRequest(JidType, hint="Coveo.SearchService.ComputedFieldRequest"):
    """Used to ask for field value aggregation.

    Attributes:
        operation: The type of computed field operation.
        field: The field name.
    """

    operation: Opt[ComputedFieldOperation] = None
    field: Opt[str] = None

    def __init__(self, *, operation: Opt[ComputedFieldOperation] = None, field: Opt[str] = None) -> None:
        """

        Parameters:
            operation: The type of computed field operation.
            field: The field name.
        """


class UserIdType(JidEnumFlag):
    """The type of user identification. Useful when intereacting with security providers.

    Attributes:
        Unspecified: The UserId name maps to either a user or group. The security provider will know.
        User: The UserId name maps to a user.
        Group: The UserId name maps to a group.
        VirtualGroup: The UserId name maps to a virtual group.
    """

    Unspecified: int = auto()
    User: int = auto()
    Group: int = auto()
    VirtualGroup: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class UserId(JidType, hint="Coveo.SearchService.UserId"):
    """User identification. Among others things, this is used to find out which documents are or are not allowed to be seen by that user.

    Attributes:
        name: String for the user/group. Security provider specific.
        provider: Name of the security provider to which the user is bound.
        type_: The type of UserId. See <b>UserIdType</b>.
        infos: Security provider-specific extra information.
        auth_cookie: This field is opaque and is set by a successful call to AuthenticateUser.
    """

    name: Opt[str] = None
    provider: Opt[str] = None
    type_: Opt[UserIdType] = attrib(default=None, metadata={CASING: "Type"})
    infos: Opt[Dict[str, str]] = None
    auth_cookie: Opt[Union[str, bytes]] = None

    def __init__(
        self,
        *,
        name: Opt[str] = None,
        provider: Opt[str] = None,
        type_: Opt[UserIdType] = attrib(default=None, metadata={CASING: "Type"}),
        infos: Opt[Dict[str, str]] = None,
        auth_cookie: Opt[Union[str, bytes]] = None,
    ) -> None:
        """

        Parameters:
            name: String for the user/group. Security provider specific.
            provider: Name of the security provider to which the user is bound.
            type_: The type of UserId. See <b>UserIdType</b>.
            infos: Security provider-specific extra information.
            auth_cookie: This field is opaque and is set by a successful call to AuthenticateUser.
        """


@attrs(kw_only=True, auto_attribs=True)
class NumberRangeFacet(JidType, hint="Coveo.SearchService.NumberRangeFacet"):
    """Used to group facet values in a <b>Facet</b> request.

    Attributes:
        range_start: The start of the range for the facet.
        range_end: The end of the range for the numerical facet.
        range_label: The optional label to tag the result with.
        range_end_inclusive: Whether the end range is inclusive or not.
    """

    range_start: Opt[Any] = None
    range_end: Opt[Any] = None
    range_label: Opt[str] = None
    range_end_inclusive: Opt[bool] = None

    def __init__(
        self,
        *,
        range_start: Opt[Any] = None,
        range_end: Opt[Any] = None,
        range_label: Opt[str] = None,
        range_end_inclusive: Opt[bool] = None,
    ) -> None:
        """

        Parameters:
            range_start: The start of the range for the facet.
            range_end: The end of the range for the numerical facet.
            range_label: The optional label to tag the result with.
            range_end_inclusive: Whether the end range is inclusive or not.
        """


class UnitOfMeasurementType(JidEnumFlag):
    """The unit of measurement associated with the data stored in a field.

    Attributes:
        Default: Standard precision in power of ten.
        PowerOfTwo: Standard precision in power of two.
        SIPrefixYocto: Standard prefix of the metric system.
        SIPrefixZepto: Standard prefix of the metric system. There's 1000 units before the next prefix.
        SIPrefixAtto: Standard prefix of the metric system. There's 1000 units before the next prefix.
        SIPrefixPico: Standard prefix of the metric system. There's 1000 units before the next prefix.
        SIPrefixNano: Standard prefix of the metric system. There's 1000 units before the next prefix.
        SIPrefixMicro: Standard prefix of the metric system. There's 1000 units before the next prefix.
        SIPrefixMilli: Standard prefix of the metric system. There's 10 units before the next prefix.
        SIPrefixCenti: Standard prefix of the metric system. There's 10 units before the next prefix.
        SIPrefixDeci: Standard prefix of the metric system. There's 10 units before the next prefix.
        SIPrefixNone: Standard prefix of the metric system. There's 10 units before the next prefix.
        SIPrefixDeca: Standard prefix of the metric system. There's 10 units before the next prefix.
        SIPrefixHecto: Standard prefix of the metric system. There's 10 units before the next prefix.
        SIPrefixKilo: Standard prefix of the metric system. There's 1000 units before the next prefix.
        SIPrefixMega: Standard prefix of the metric system. There's 1000 units before the next prefix.
        SIPrefixGiga: Standard prefix of the metric system. There's 1000 units before the next prefix.
        SIPrefixTera: Standard prefix of the metric system. There's 1000 units before the next prefix.
        SIPrefixPeta: Standard prefix of the metric system. There's 1000 units before the next prefix.
        SIPrefixExa: Standard prefix of the metric system. There's 1000 units before the next prefix.
        SIPrefixZetta: Standard prefix of the metric system. There's 1000 units before the next prefix.
        SIPrefixYotta: Standard prefix of the metric system. There's 1000 units before the next prefix.
        SIPrefix_MAX: Standard prefix of the metric system. MAX.
        DigitalInformationBinaryBit: Standard unit of computing storage. There's is 8 bit in a byte.
        DigitalInformationBinaryOther: Standard unit of computing storage. Use the value 2^10 for delimitation between each unit prefix.
        DigitalInformationBinary_MAX: Standard unit of computing storage. MAX.
        DigitalInformationDecimalBit: Standard unit of computing storage. There's is 8 bit in a byte.
        DigitalInformationDecimalOther: Standard unit of computing storage. Use the value 10^3 for delimitation between each unit prefix.
        DigitalInformationDecimal_MAX: Standard unit of computing storage. MAX.
        USLengthPoint: United States customary units of length.
        USLengthPica: United States customary units of length. Represents 12 points.
        USLengthInch: United States customary units of length. Represents 6 picas.
        USLengthFoot: United States customary units of length. Represents 12 inches.
        USLengthYard: United States customary units of length. Represents 3 feet.
        USLengthMile: United States customary units of length. Represents 1760 yards.
        USLength_MAX: United States customary units of length. MAX.
        USVolumeMinim: United States customary units of volume.
        USVolumeTeaspoon: United States customary units of volume. Represents 80 minims.
        USVolumeTablespoon: United States customary units of volume. Represents 3 teaspoons.
        USVolumeFluidOunce: United States customary units of volume. Represents 2 tablespoons2.
        USVolumeCup: United States customary units of volume. Represents 8 fluid ounces.
        USVolumePint: United States customary units of volume. Represents 2 cups.
        USVolumeQuart: United States customary units of volume. Represents 2 quarters.
        USVolumeGallon: United States customary units of volume. Represents 4 quarters.
        USVolume_MAX: United States customary units of volume. MAX.
        USMassGrain: United States customary units of mass.
        USMassDram: United States customary units of mass. Represents 27 + 11/32 grains.
        USMassOunce: United States customary units of mass. Represents 16 drams.
        USMassPound: United States customary units of mass. Represents 16 ounces.
        USMassHundredweight: United States customary units of mass. Represents 100 pounds.
        USMassTon: United States customary units of mass. Represents 20 hundredweights.
        USMass_MAX: United States customary units of mass. MAX.
    """

    Default: int = auto()
    PowerOfTwo: int = auto()
    SIPrefixYocto: int = auto()
    SIPrefixZepto: int = auto()
    SIPrefixAtto: int = auto()
    SIPrefixPico: int = auto()
    SIPrefixNano: int = auto()
    SIPrefixMicro: int = auto()
    SIPrefixMilli: int = auto()
    SIPrefixCenti: int = auto()
    SIPrefixDeci: int = auto()
    SIPrefixNone: int = auto()
    SIPrefixDeca: int = auto()
    SIPrefixHecto: int = auto()
    SIPrefixKilo: int = auto()
    SIPrefixMega: int = auto()
    SIPrefixGiga: int = auto()
    SIPrefixTera: int = auto()
    SIPrefixPeta: int = auto()
    SIPrefixExa: int = auto()
    SIPrefixZetta: int = auto()
    SIPrefixYotta: int = auto()
    SIPrefix_MAX: int = auto()
    DigitalInformationBinaryBit: int = auto()
    DigitalInformationBinaryOther: int = auto()
    DigitalInformationBinary_MAX: int = auto()
    DigitalInformationDecimalBit: int = auto()
    DigitalInformationDecimalOther: int = auto()
    DigitalInformationDecimal_MAX: int = auto()
    USLengthPoint: int = auto()
    USLengthPica: int = auto()
    USLengthInch: int = auto()
    USLengthFoot: int = auto()
    USLengthYard: int = auto()
    USLengthMile: int = auto()
    USLength_MAX: int = auto()
    USVolumeMinim: int = auto()
    USVolumeTeaspoon: int = auto()
    USVolumeTablespoon: int = auto()
    USVolumeFluidOunce: int = auto()
    USVolumeCup: int = auto()
    USVolumePint: int = auto()
    USVolumeQuart: int = auto()
    USVolumeGallon: int = auto()
    USVolume_MAX: int = auto()
    USMassGrain: int = auto()
    USMassDram: int = auto()
    USMassOunce: int = auto()
    USMassPound: int = auto()
    USMassHundredweight: int = auto()
    USMassTon: int = auto()
    USMass_MAX: int = auto()


class AutomaticRangeAlgorithm(JidEnumFlag):
    """Available algorithms for generating number ranges automatically.

    Attributes:
        Even: The generated ranges will evenly partition the value range.
        Equiprobable: Partitioning by occurrence count -- the generated ranges will be roughly equiprobable
    """

    Even: int = auto()
    Equiprobable: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class Facet(JidType, hint="Coveo.SearchService.Facet"):
    """Used to ask for the values of a field in all the matching documents.

    Attributes:
        field_name: The name of the field for which to list the possible values.
        id_: The Id of the refine. Used by the caller to match its Facets in case the name is not enough !
        hints: Specified if we want to restrict the values to group.
        hints_type: The type of filtering for Hints, if set.
        sort_criteria: The criteria to use for sorting the results.
        optional_field_value_to_lookup: Optional field value to get for each group.
        thorough_lookup: Whether to do a thorough lookup or not.
        injection_depth: The number of documents to gather values for when injecting.
        max_number_of_facet_results: The maximum number of values to return.
        overriding_filter: Filter that will override the main query. Used for facet multi-selection.
        overriding_filter_constant: The constant part of the overriding filter, for caching and performance.
        overriding_filter_disjunction: The disjunction part of the overriding filter.
        unit_of_measurement: The unit of measurement stored in the field, for dynamic range generation.
        complete_facet_with_standard_values: If they are not enough Hints, standard values will complete the facet (this parameter is ignored if the Hints vector is empty.)
        generate_automatic_ranges: Whether to generate automatic ranges if none are provided, or not.
        filter_facet_count: Whether to adjust facet count when filtering, or not.
        range_algorithm: The partitioning algorithm to use to generate the ranges.
    """

    field_name: Opt[str] = None
    id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"})
    hints: Opt[List[str]] = None
    hints_type: ListFacetFieldValuesRequest = ListFacetFieldValuesRequest.Verbatim
    sort_criteria: FacetSortCriteria = FacetSortCriteria.SortByOccurrence
    optional_field_value_to_lookup: Opt[str] = None
    thorough_lookup: bool = True
    injection_depth: int = 1000
    max_number_of_facet_results: int = 16
    computed_field_requests: Opt[List[ComputedFieldRequest]] = None
    number_range_facet_requests: Opt[List[NumberRangeFacet]] = None
    overriding_filter: Opt[str] = None
    overriding_filter_constant: Opt[str] = None
    overriding_filter_disjunction: Opt[str] = None
    unit_of_measurement: Opt[UnitOfMeasurementType] = None
    complete_facet_with_standard_values: Opt[bool] = None
    generate_automatic_ranges: Opt[bool] = None
    filter_facet_count: bool = True
    range_algorithm: AutomaticRangeAlgorithm = AutomaticRangeAlgorithm.Even

    def __init__(
        self,
        *,
        field_name: Opt[str] = None,
        id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"}),
        hints: Opt[List[str]] = None,
        hints_type: ListFacetFieldValuesRequest = ListFacetFieldValuesRequest.Verbatim,
        sort_criteria: FacetSortCriteria = FacetSortCriteria.SortByOccurrence,
        optional_field_value_to_lookup: Opt[str] = None,
        thorough_lookup: bool = True,
        injection_depth: int = 1000,
        max_number_of_facet_results: int = 16,
        computed_field_requests: Opt[List[ComputedFieldRequest]] = None,
        number_range_facet_requests: Opt[List[NumberRangeFacet]] = None,
        overriding_filter: Opt[str] = None,
        overriding_filter_constant: Opt[str] = None,
        overriding_filter_disjunction: Opt[str] = None,
        unit_of_measurement: Opt[UnitOfMeasurementType] = None,
        complete_facet_with_standard_values: Opt[bool] = None,
        generate_automatic_ranges: Opt[bool] = None,
        filter_facet_count: bool = True,
        range_algorithm: AutomaticRangeAlgorithm = AutomaticRangeAlgorithm.Even,
    ) -> None:
        """

        Parameters:
            field_name: The name of the field for which to list the possible values.
            id_: The Id of the refine. Used by the caller to match its Facets in case the name is not enough !
            hints: Specified if we want to restrict the values to group.
            hints_type: The type of filtering for Hints, if set.
            sort_criteria: The criteria to use for sorting the results.
            optional_field_value_to_lookup: Optional field value to get for each group.
            thorough_lookup: Whether to do a thorough lookup or not.
            injection_depth: The number of documents to gather values for when injecting.
            max_number_of_facet_results: The maximum number of values to return.
            overriding_filter: Filter that will override the main query. Used for facet multi-selection.
            overriding_filter_constant: The constant part of the overriding filter, for caching and performance.
            overriding_filter_disjunction: The disjunction part of the overriding filter.
            unit_of_measurement: The unit of measurement stored in the field, for dynamic range generation.
            complete_facet_with_standard_values: If they are not enough Hints, standard values will complete the facet (this parameter is ignored if the Hints vector is empty.)
            generate_automatic_ranges: Whether to generate automatic ranges if none are provided, or not.
            filter_facet_count: Whether to adjust facet count when filtering, or not.
            range_algorithm: The partitioning algorithm to use to generate the ranges.
        """


@attrs(kw_only=True, auto_attribs=True)
class RankingExpression(JidType, hint="Coveo.SearchService.RankingExpression"):
    """Holds information about a ranking expression.

    Attributes:
        expression: The expression that matches documents whose ranking to affect.
        modifier: The ranking modifier to apply. A positive value boosts, and a negative value dampens.
        is_constant: Whether the expression is constant or not. A constant expression will be cached longer.
        is_deterministic: Whether the QRE is deterministic in ranking (slow), or not (heuristics possible, faster).
    """

    expression: Opt[str] = None
    modifier: Opt[int] = None
    is_constant: Opt[bool] = None
    is_deterministic: bool = True

    def __init__(
        self,
        *,
        expression: Opt[str] = None,
        modifier: Opt[int] = None,
        is_constant: Opt[bool] = None,
        is_deterministic: bool = True,
    ) -> None:
        """

        Parameters:
            expression: The expression that matches documents whose ranking to affect.
            modifier: The ranking modifier to apply. A positive value boosts, and a negative value dampens.
            is_constant: Whether the expression is constant or not. A constant expression will be cached longer.
            is_deterministic: Whether the QRE is deterministic in ranking (slow), or not (heuristics possible, faster).
        """


@attrs(kw_only=True, auto_attribs=True)
class BoundRankingExpressionsGroup(JidType, hint="Coveo.SearchService.BoundRankingExpressionsGroup"):
    """Holds information about ranking expressions that are made to boost only a given number of documents.

    Attributes:
        ranking_expressions: The ranking expressions that will be executed in order.
        number_of_documents: The number of documents to boost, by executing expressions in order.
    """

    ranking_expressions: Opt[List[RankingExpression]] = None
    number_of_documents: Opt[int] = None

    def __init__(
        self, *, ranking_expressions: Opt[List[RankingExpression]] = None, number_of_documents: Opt[int] = None
    ) -> None:
        """

        Parameters:
            ranking_expressions: The ranking expressions that will be executed in order.
            number_of_documents: The number of documents to boost, by executing expressions in order.
        """


@attrs(kw_only=True, auto_attribs=True)
class RankingFunction(JidType, hint="Coveo.SearchService.RankingFunction"):
    """Holds information about a ranking function.

    Attributes:
        expression: The expression that will be executed.
        normalize_weight: Whether to normalize the weight or not.
        modifier: The modifier to use when normalizing weight.
    """

    expression: Opt[str] = None
    normalize_weight: Opt[bool] = None
    modifier: int = 600

    def __init__(self, *, expression: Opt[str] = None, normalize_weight: Opt[bool] = None, modifier: int = 600) -> None:
        """

        Parameters:
            expression: The expression that will be executed.
            normalize_weight: Whether to normalize the weight or not.
            modifier: The modifier to use when normalizing weight.
        """


@attrs(kw_only=True, auto_attribs=True)
class QueryFunction(JidType, hint="Coveo.SearchService.QueryFunction"):
    """Holds information about a query function.

    Attributes:
        function: The function to execute.
        field_name: The dynamic field that will hold the results.
        modifier: The modifier internally used by Ranking Functions.
    """

    function: Opt[str] = None
    field_name: Opt[str] = None
    modifier: Opt[int] = None

    def __init__(self, *, function: Opt[str] = None, field_name: Opt[str] = None, modifier: Opt[int] = None) -> None:
        """

        Parameters:
            function: The function to execute.
            field_name: The dynamic field that will hold the results.
            modifier: The modifier internally used by Ranking Functions.
        """


class RankingOverrideType(JidEnumFlag):
    """The type of ranking override we target in a RankingOverride."""

    AdjacencyMult: int = auto()
    ConceptMult: int = auto()
    CustomDocumentWeightMult: int = auto()
    DocDateMult: int = auto()
    FormattedMult: int = auto()
    LanguageMult: int = auto()
    LastDirInURIMult: int = auto()
    QualityMult: int = auto()
    SourceReputationMult: int = auto()
    SummaryMult: int = auto()
    TermCorrelationMult: int = auto()
    TermCasingMult: int = auto()
    TFIDFMult: int = auto()
    TitleMult: int = auto()
    URIMult: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class RankingOverride(JidType, hint="Coveo.SearchService.RankingOverride"):
    """Holds information about an override to the default ranking weights.

    Attributes:
        type_: The name of the ranking weight to override.
        value: The ranking override (from 0 to 9, default is 5).
    """

    type_: Opt[RankingOverrideType] = attrib(default=None, metadata={CASING: "Type"})
    value: Opt[int] = None

    def __init__(
        self,
        *,
        type_: Opt[RankingOverrideType] = attrib(default=None, metadata={CASING: "Type"}),
        value: Opt[int] = None,
    ) -> None:
        """

        Parameters:
            type_: The name of the ranking weight to override.
            value: The ranking override (from 0 to 9, default is 5).
        """


@attrs(kw_only=True, auto_attribs=True)
class SearchSession(JidType, hint="Coveo.SearchService.SearchSession"):
    """Describes <b>who</b> is calling the server.<p>The ExecuteQuery for instance uses this to only return documents the user has rights to see.</p>

    Attributes:
        user_id: The main user.
        additional_user_ids: Optional users.
        super_user_mode: Perform call as super user.
    """

    user_id: Opt[UserId] = None
    additional_user_ids: Opt[List[UserId]] = None
    client_code: Opt[str] = None
    super_user_mode: Opt[bool] = None

    def __init__(
        self,
        *,
        user_id: Opt[UserId] = None,
        additional_user_ids: Opt[List[UserId]] = None,
        client_code: Opt[str] = None,
        super_user_mode: Opt[bool] = None,
    ) -> None:
        """

        Parameters:
            user_id: The main user.
            additional_user_ids: Optional users.
            super_user_mode: Perform call as super user.
        """


class DesiredLanguages(JidEnumFlag):
    """Specifies the languages to use for term expansion.

    Attributes:
        UserSpecifiedLanguage: Special case of SpecifiedLanguages, where only the user culture language is specified.
        NoExpansion: Use only the original terms.
    """

    MainIndexLanguages: int = auto()
    AllLanguages: int = auto()
    SpecifiedLanguages: int = auto()
    UserSpecifiedLanguage: int = auto()
    NoExpansion: int = auto()


class Language(JidEnumFlag):
    Unsupported: int = auto()
    Unknown: int = auto()
    English: int = auto()
    French: int = auto()
    Japanese: int = auto()
    German: int = auto()
    Spanish: int = auto()
    Korean: int = auto()
    Italian: int = auto()
    Portuguese: int = auto()
    Danish: int = auto()
    Dutch: int = auto()
    Catalan: int = auto()
    Basque: int = auto()
    Finnish: int = auto()
    Norwegian: int = auto()
    Swedish: int = auto()
    Icelandic: int = auto()
    Bulgarian: int = auto()
    Russian: int = auto()
    Greek: int = auto()
    Chinese: int = auto()
    Croatian: int = auto()
    Czech: int = auto()
    Hungarian: int = auto()
    Serbian: int = auto()
    Polish: int = auto()
    Romanian: int = auto()
    Arabic: int = auto()
    Hebrew: int = auto()
    Esperanto: int = auto()
    Turkish: int = auto()
    Malay: int = auto()
    Hindi: int = auto()
    Indonesian: int = auto()
    Persian: int = auto()
    Thai: int = auto()
    Yiddish: int = auto()
    Mongolian: int = auto()
    Bokmal: int = auto()
    Slovak: int = auto()
    Slovenian: int = auto()
    Lithuanian: int = auto()
    Vietnamese: int = auto()
    Afrikaans: int = auto()
    Armenian: int = auto()
    Belarusian: int = auto()
    Estonian: int = auto()
    Filipino: int = auto()
    Latvian: int = auto()
    Swahili: int = auto()
    Ukrainian: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class ScopeIndexSlice(JidType, hint="Coveo.SearchService.ScopeIndexSlice"):
    name: Opt[str] = None
    uri: Opt[str] = None
    timeout: int = attrib(default=1, metadata={CASING: "TimeOut"})
    search_session: Opt[SearchSession] = None

    def __init__(
        self,
        *,
        name: Opt[str] = None,
        uri: Opt[str] = None,
        timeout: int = attrib(default=1, metadata={CASING: "TimeOut"}),
        search_session: Opt[SearchSession] = None,
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ScopeIndex(JidType, hint="Coveo.SearchService.ScopeIndex"):
    name: Opt[str] = None
    filter_: Opt[str] = attrib(default=None, metadata={CASING: "Filter"})
    slices: Opt[List[ScopeIndexSlice]] = None

    def __init__(
        self,
        *,
        name: Opt[str] = None,
        filter_: Opt[str] = attrib(default=None, metadata={CASING: "Filter"}),
        slices: Opt[List[ScopeIndexSlice]] = None,
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class Scope(JidType, hint="Coveo.SearchService.Scope"):
    """The scope to use for the query"""

    perform_cross_index_features: Opt[bool] = None
    indexes: Opt[List[ScopeIndex]] = None

    def __init__(
        self, *, perform_cross_index_features: Opt[bool] = None, indexes: Opt[List[ScopeIndex]] = None
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class DesiredFields(JidType, hint="Coveo.SearchService.DesiredFields"):
    """The fields to be included or excluded for each document returned by the query.

    Attributes:
        include_fields: Whether to only include specified fields or exclude them.
        field_names: The names of the fields to include/exclude.
    """

    include_fields: Opt[bool] = None
    field_names: Opt[List[str]] = None

    def __init__(self, *, include_fields: Opt[bool] = None, field_names: Opt[List[str]] = None) -> None:
        """

        Parameters:
            include_fields: Whether to only include specified fields or exclude them.
            field_names: The names of the fields to include/exclude.
        """


class LoadTextFormat(JidEnumFlag):
    """Different formats available for loading document text along with query results.

    Attributes:
        None_: Do not return document text along with results.
        Text: Return the document text as text.
        Html: Return the document text as HTML.
    """

    None_: int = auto()
    Text: int = auto()
    Html: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class QueryParams(JidType, hint="Coveo.SearchService.QueryParams"):
    """The definition of all the parameters that can modify a query's execution.

    Attributes:
        expression: The basic query expression is used for <b>Did You Mean</b>, the thesaurus, etc. Basically, it should be the one entered by the user.
        advanced_expression: The advanced query expression contains the various expressions that should not be seen by the user and that are generated by the search page. Most of the time, those are custom field expressions such as <code>@Categories=News</code>.
        constant_expression: The query constant expression, that can be cached.
        mandatory_expression: The mandatory expression, oftentimes a user filter that we want to isolate from the other expressions in case of parsing errors
        parent_field_name: The name of the field on a parent result.  Set if you want automatic parent result loading.
        child_field_name: The name of the field on a child result.  Set if you want automatic parent result loading.
        collection_names: The names of the collections in which the query is be performed. If nothing is specified, all the collections the user can accessed are used.
        facets: The list of fields for which to retrieve possible refinements. This list specifies, for the results of the current query, the fields for which you want to retrieve the list of values. The information about the field and how to sort the values is specified through the Facet structure.
        first_result: The 0-based index of the first result to retrieve. Specify a value other than 0 when you want to display the second, third, etc. page of results.
        number_of_results: The maximum number of results to retrieve. This is the number of results per page.
        specified_languages: If LanguageExpansion = SpecifiedLanguages, this lists the desired ones.
        preferred_language: The optional name of the preferred language for results (e.g.: English, French, Spanish, Dutch, etc). <p>When specified, results in the preferred language have a slight priority boost over the other ones when the results are ranked and sorted.</p>
        sort_by: The sort criteria to use for sorting results. The most common criterion is Relevance, which uses the main ranking algorithm. You may also sort by date, or by the value of a custom field.
        sort_by_fields: The optional names of the fields to use for sorting results (when Field <b>SortBy</b> is set to sort by a field value).<p>These fields have to be registered in the Administration Tool before they can be specified here.</p>
        time_zone_offset: The offset from local time to UTC, in minutes for the user that is performing the query. This value is usually retrieved from the Web browser, not from the server.
        time_zone: The local time zone.
        excerpt_length: The length of the excerpt to retrieve for each result (in characters). You must set this property to a non-zero value to retrieve an excerpt, otherwise no excerpt is provided.
        summary_length: The length of the summary to retrieve for each result (in words). You must set this property to a non-zero value to retrieve a summary.
        custom_filter: The name of the field on which to fold.
        custom_filter_range: The number of folded results per field value. The default value only makes sense if Field <b>CustomFilter</b> is specified.
        ranking_expressions: Alias RankingModifiers. QRE.
        bound_ranking_expressions_groups: List of bound ranking expressions groups.
        ranking_functions: Functions used to influence ranking, typically through numerical fields.
        query_functions: Query functions that will generate dynamic field, used by queries and/or ranking.
        execute_document_count: Only the number of documents matching the query will be returned.
        enable_wildcards: Set to <code>True</code> to enable the use of wildcards for this query.
        enable_question_mark: Set to <code>True</code> to enable the use of ? as a wildcard for this query.
        enable_did_you_mean: Set to <code>True</code> to enable use of <b>Did You Mean</b> for this query.
        load_tags_on_results: Set to <code>True</code> to load a document's tags in its result.
        enable_duplicate_filtering: Set to <code>True</code> to enable duplicate document filtering. If this is enabled, documents that resemble others will appear only once in the results. Also, the <b>QueryResults.FilteredResults</b> will be populated.<p>Enabling this feature may render the total result count less precise, as only the results up to those being retrieved are submitted to filtering. So, if you have 10 unique documents and then 90 duplicate ones in the result, the first result page will display a total count of 100 results, but when the user jumps to the second page the count will be lowered to 11 and only one result will be displayed.</p>
        extract_first_sentences: Do we extract the sentences from the document's excerpt ? ExcerptLength must not be 0.
        index_browser_query: If set, this returns all documents matching the query, but trims down sensible information from documents that would not normally be returned.
        background_query: Whether the query is a background query or not.
        disjunction_expression: Expression to be used
        desired_fields: The fields to include/exclude
        enable_ranking_information: Whether to enable ranking information or not for this query
        enable_query_profiling: Whether to enable query profiling or not for this query.
        is_gdi_query: Whether the query is a GDI query.
        use_and_by_default: Whether to use AND or OR by default.
        timeout: Timeout in seconds after which the query will stop executing.  0 means infinite.
        load_document: Desired return format for document.
    """

    expression: Opt[str] = None
    advanced_expression: Opt[str] = None
    constant_expression: Opt[str] = None
    mandatory_expression: Opt[str] = None
    parent_field_name: Opt[str] = None
    child_field_name: Opt[str] = None
    collection_names: Opt[List[str]] = None
    facets: Opt[List[Facet]] = None
    first_result: Opt[int] = None
    number_of_results: int = 10
    language_expansion: Opt[DesiredLanguages] = None
    specified_languages: Opt[List[Language]] = None
    preferred_language: Opt[str] = None
    sort_by: SortBy = SortBy.Relevancy
    sort_by_fields: Opt[List[SortByField]] = None
    time_zone_offset: Opt[int] = None
    time_zone: Opt[str] = None
    excerpt_length: int = 200
    summary_length: Opt[int] = None
    custom_filter: Opt[str] = None
    custom_filter_range: int = 30
    ranking_expressions: Opt[List[RankingExpression]] = None
    bound_ranking_expressions_groups: Opt[List[BoundRankingExpressionsGroup]] = None
    ranking_functions: Opt[List[RankingFunction]] = None
    query_functions: Opt[List[QueryFunction]] = None
    ranking_overrides: Opt[List[RankingOverride]] = None
    execute_document_count: Opt[bool] = None
    enable_wildcards: Opt[bool] = None
    enable_question_mark: Opt[bool] = None
    disable_logging: Opt[bool] = None
    enable_did_you_mean: bool = True
    load_tags_on_results: bool = True
    enable_duplicate_filtering: bool = True
    extract_first_sentences: Opt[bool] = None
    index_browser_query: Opt[bool] = None
    background_query: Opt[bool] = None
    disjunction_expression: Opt[str] = None
    desired_fields: Opt[DesiredFields] = None
    enable_ranking_information: Opt[bool] = None
    enable_query_profiling: Opt[bool] = None
    is_gdi_query: Opt[bool] = attrib(default=None, metadata={CASING: "IsGDIQuery"})
    use_and_by_default: bool = True
    timeout: Opt[int] = attrib(default=None, metadata={CASING: "TimeOut"})
    load_document: LoadTextFormat = LoadTextFormat.None_

    def __init__(
        self,
        *,
        expression: Opt[str] = None,
        advanced_expression: Opt[str] = None,
        constant_expression: Opt[str] = None,
        mandatory_expression: Opt[str] = None,
        parent_field_name: Opt[str] = None,
        child_field_name: Opt[str] = None,
        collection_names: Opt[List[str]] = None,
        facets: Opt[List[Facet]] = None,
        first_result: Opt[int] = None,
        number_of_results: int = 10,
        language_expansion: Opt[DesiredLanguages] = None,
        specified_languages: Opt[List[Language]] = None,
        preferred_language: Opt[str] = None,
        sort_by: SortBy = SortBy.Relevancy,
        sort_by_fields: Opt[List[SortByField]] = None,
        time_zone_offset: Opt[int] = None,
        time_zone: Opt[str] = None,
        excerpt_length: int = 200,
        summary_length: Opt[int] = None,
        custom_filter: Opt[str] = None,
        custom_filter_range: int = 30,
        ranking_expressions: Opt[List[RankingExpression]] = None,
        bound_ranking_expressions_groups: Opt[List[BoundRankingExpressionsGroup]] = None,
        ranking_functions: Opt[List[RankingFunction]] = None,
        query_functions: Opt[List[QueryFunction]] = None,
        ranking_overrides: Opt[List[RankingOverride]] = None,
        execute_document_count: Opt[bool] = None,
        enable_wildcards: Opt[bool] = None,
        enable_question_mark: Opt[bool] = None,
        disable_logging: Opt[bool] = None,
        enable_did_you_mean: bool = True,
        load_tags_on_results: bool = True,
        enable_duplicate_filtering: bool = True,
        extract_first_sentences: Opt[bool] = None,
        index_browser_query: Opt[bool] = None,
        background_query: Opt[bool] = None,
        disjunction_expression: Opt[str] = None,
        desired_fields: Opt[DesiredFields] = None,
        enable_ranking_information: Opt[bool] = None,
        enable_query_profiling: Opt[bool] = None,
        is_gdi_query: Opt[bool] = attrib(default=None, metadata={CASING: "IsGDIQuery"}),
        use_and_by_default: bool = True,
        timeout: Opt[int] = attrib(default=None, metadata={CASING: "TimeOut"}),
        load_document: LoadTextFormat = LoadTextFormat.None_,
    ) -> None:
        """

        Parameters:
            expression: The basic query expression is used for <b>Did You Mean</b>, the thesaurus, etc. Basically, it should be the one entered by the user.
            advanced_expression: The advanced query expression contains the various expressions that should not be seen by the user and that are generated by the search page. Most of the time, those are custom field expressions such as <code>@Categories=News</code>.
            constant_expression: The query constant expression, that can be cached.
            mandatory_expression: The mandatory expression, oftentimes a user filter that we want to isolate from the other expressions in case of parsing errors
            parent_field_name: The name of the field on a parent result.  Set if you want automatic parent result loading.
            child_field_name: The name of the field on a child result.  Set if you want automatic parent result loading.
            collection_names: The names of the collections in which the query is be performed. If nothing is specified, all the collections the user can accessed are used.
            facets: The list of fields for which to retrieve possible refinements. This list specifies, for the results of the current query, the fields for which you want to retrieve the list of values. The information about the field and how to sort the values is specified through the Facet structure.
            first_result: The 0-based index of the first result to retrieve. Specify a value other than 0 when you want to display the second, third, etc. page of results.
            number_of_results: The maximum number of results to retrieve. This is the number of results per page.
            specified_languages: If LanguageExpansion = SpecifiedLanguages, this lists the desired ones.
            preferred_language: The optional name of the preferred language for results (e.g.: English, French, Spanish, Dutch, etc). <p>When specified, results in the preferred language have a slight priority boost over the other ones when the results are ranked and sorted.</p>
            sort_by: The sort criteria to use for sorting results. The most common criterion is Relevance, which uses the main ranking algorithm. You may also sort by date, or by the value of a custom field.
            sort_by_fields: The optional names of the fields to use for sorting results (when Field <b>SortBy</b> is set to sort by a field value).<p>These fields have to be registered in the Administration Tool before they can be specified here.</p>
            time_zone_offset: The offset from local time to UTC, in minutes for the user that is performing the query. This value is usually retrieved from the Web browser, not from the server.
            time_zone: The local time zone.
            excerpt_length: The length of the excerpt to retrieve for each result (in characters). You must set this property to a non-zero value to retrieve an excerpt, otherwise no excerpt is provided.
            summary_length: The length of the summary to retrieve for each result (in words). You must set this property to a non-zero value to retrieve a summary.
            custom_filter: The name of the field on which to fold.
            custom_filter_range: The number of folded results per field value. The default value only makes sense if Field <b>CustomFilter</b> is specified.
            ranking_expressions: Alias RankingModifiers. QRE.
            bound_ranking_expressions_groups: List of bound ranking expressions groups.
            ranking_functions: Functions used to influence ranking, typically through numerical fields.
            query_functions: Query functions that will generate dynamic field, used by queries and/or ranking.
            execute_document_count: Only the number of documents matching the query will be returned.
            enable_wildcards: Set to <code>True</code> to enable the use of wildcards for this query.
            enable_question_mark: Set to <code>True</code> to enable the use of ? as a wildcard for this query.
            enable_did_you_mean: Set to <code>True</code> to enable use of <b>Did You Mean</b> for this query.
            load_tags_on_results: Set to <code>True</code> to load a document's tags in its result.
            enable_duplicate_filtering: Set to <code>True</code> to enable duplicate document filtering. If this is enabled, documents that resemble others will appear only once in the results. Also, the <b>QueryResults.FilteredResults</b> will be populated.<p>Enabling this feature may render the total result count less precise, as only the results up to those being retrieved are submitted to filtering. So, if you have 10 unique documents and then 90 duplicate ones in the result, the first result page will display a total count of 100 results, but when the user jumps to the second page the count will be lowered to 11 and only one result will be displayed.</p>
            extract_first_sentences: Do we extract the sentences from the document's excerpt ? ExcerptLength must not be 0.
            index_browser_query: If set, this returns all documents matching the query, but trims down sensible information from documents that would not normally be returned.
            background_query: Whether the query is a background query or not.
            disjunction_expression: Expression to be used
            desired_fields: The fields to include/exclude
            enable_ranking_information: Whether to enable ranking information or not for this query
            enable_query_profiling: Whether to enable query profiling or not for this query.
            is_gdi_query: Whether the query is a GDI query.
            use_and_by_default: Whether to use AND or OR by default.
            timeout: Timeout in seconds after which the query will stop executing.  0 means infinite.
            load_document: Desired return format for document.
        """


@attrs(kw_only=True, auto_attribs=True)
class QueryParamsForTagging(JidType, hint="Coveo.SearchService.QueryParamsForTagging"):
    """The definition of all the parameters that can modify a query's execution.

    Attributes:
        expression: The basic query expression is used for <b>Did You Mean</b>, the thesaurus, etc. Basically, it should be the one entered by the user.
        advanced_expression: The advanced query expression contains the various expressions that should not be seen by the user and that are generated by the search page. Most of the time, those are custom field expressions such as <code>@Categories=News</code>.
        constant_expression: The query constant expression, that can be cached.
        mandatory_expression: The query mandatory expression.
        collection_names: The names of the collections in which the query is be performed. If nothing is specified, all the collections the user can accessed are used.
        specified_languages: If LanguageExpansion = SpecifiedLanguages, this lists the desired ones.
        time_zone_offset: The offset from local time to UTC, in minutes for the user that is performing the query. This value is usually retrieved from the Web browser, not from the server.
        time_zone: The local time zone.
        enable_wildcards: Set to <code>True</code> to enable the use of wildcards for this query.
        enable_question_mark: Set to <code>True</code> to enable the use of ? as a wildcard for this query.
        index_browser_query: If set, this returns all documents matching the query, but trims down sensible information from documents that would not normally be returned.
        background_query: Whether the query is a background query or not.
        disjunction_expression: Expression to be used
    """

    expression: Opt[str] = None
    advanced_expression: Opt[str] = None
    constant_expression: Opt[str] = None
    mandatory_expression: Opt[str] = None
    collection_names: Opt[List[str]] = None
    language_expansion: Opt[DesiredLanguages] = None
    specified_languages: Opt[List[Language]] = None
    time_zone_offset: Opt[int] = None
    time_zone: Opt[str] = None
    enable_wildcards: Opt[bool] = None
    enable_question_mark: Opt[bool] = None
    index_browser_query: Opt[bool] = None
    background_query: Opt[bool] = None
    disjunction_expression: Opt[str] = None

    def __init__(
        self,
        *,
        expression: Opt[str] = None,
        advanced_expression: Opt[str] = None,
        constant_expression: Opt[str] = None,
        mandatory_expression: Opt[str] = None,
        collection_names: Opt[List[str]] = None,
        language_expansion: Opt[DesiredLanguages] = None,
        specified_languages: Opt[List[Language]] = None,
        time_zone_offset: Opt[int] = None,
        time_zone: Opt[str] = None,
        enable_wildcards: Opt[bool] = None,
        enable_question_mark: Opt[bool] = None,
        index_browser_query: Opt[bool] = None,
        background_query: Opt[bool] = None,
        disjunction_expression: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            expression: The basic query expression is used for <b>Did You Mean</b>, the thesaurus, etc. Basically, it should be the one entered by the user.
            advanced_expression: The advanced query expression contains the various expressions that should not be seen by the user and that are generated by the search page. Most of the time, those are custom field expressions such as <code>@Categories=News</code>.
            constant_expression: The query constant expression, that can be cached.
            mandatory_expression: The query mandatory expression.
            collection_names: The names of the collections in which the query is be performed. If nothing is specified, all the collections the user can accessed are used.
            specified_languages: If LanguageExpansion = SpecifiedLanguages, this lists the desired ones.
            time_zone_offset: The offset from local time to UTC, in minutes for the user that is performing the query. This value is usually retrieved from the Web browser, not from the server.
            time_zone: The local time zone.
            enable_wildcards: Set to <code>True</code> to enable the use of wildcards for this query.
            enable_question_mark: Set to <code>True</code> to enable the use of ? as a wildcard for this query.
            index_browser_query: If set, this returns all documents matching the query, but trims down sensible information from documents that would not normally be returned.
            background_query: Whether the query is a background query or not.
            disjunction_expression: Expression to be used
        """


class DocumentFlag(JidEnumFlag):
    """Flags describing a QueryResult document.

    Attributes:
        IsAttachment: Document is an attachment.
        ContainsAttachment: Document contains attachment.
        HasHtmlVersion: Document has an HTML version.
        IsRecord: Document is a record.
        IsReference: Document is a reference to a document.
        IsCopyProtected: Document is copy protected.
        HasThumbnail: Document has a thumbnail.
        HasMobileHtmlVersion: Document has a mobile html version.
        SkipSentencesScoring: Skip sentences scoring on document.
    """

    IsAttachment: int = auto()
    ContainsAttachment: int = auto()
    HasHtmlVersion: int = auto()
    IsRecord: int = auto()
    IsReference: int = auto()
    IsCopyProtected: int = auto()
    HasThumbnail: int = auto()
    HasMobileHtmlVersion: int = auto()
    SkipSentencesScoring: int = auto()


class SourceType(JidEnumFlag):
    """Flags describing the kind of source a QueryResult document was extracted from.

    Attributes:
        System: The field is system, but not specific to a source type.
        Notes: The field is Lotus Notes specific.
        Exchange: The field is Microsoft Exchange specific.
        Mail: The field is Microsoft Exchange or Lotus Notes specific.
        SharePoint: The field is Microsoft SharePoint specific.
        User: The field is a user field and not specific to any source type.
        SalesForce: The field is SalesForce specific.
        Confluence: The field is Confluence specific.
        DesktopConnector: The field is Desktop connector specific.
        Clearspace: The field is Clearspace specific.
        WebsphereWCM: The field is WebsphereWCM specific.
        CRM: The field is CRM specific.
    """

    System: int = auto()
    Notes: int = auto()
    Exchange: int = auto()
    Mail: int = auto()
    SharePoint: int = auto()
    User: int = auto()
    SalesForce: int = auto()
    Confluence: int = auto()
    DesktopConnector: int = auto()
    Clearspace: int = auto()
    WebsphereWCM: int = auto()
    CRM: int = auto()


class QueryException(JidEnumFlag):
    """Describes the possible errors returned by a query execution."""

    NoException: int = auto()
    InvalidSyntax: int = auto()
    InvalidCustomField: int = auto()
    InvalidDate: int = auto()
    InvalidExactPhrase: int = auto()
    InvalidDateOp: int = auto()
    InvalidNear: int = auto()
    InvalidWeightedNear: int = auto()
    InvalidTerm: int = auto()
    TooManyTerms: int = auto()
    WildcardTooGeneral: int = auto()
    InvalidSortField: int = auto()
    RequestedResultsMax: int = auto()
    AggregatedMirrorDead: int = auto()
    AggregatedMirrorQueryTimeOut: int = auto()
    AggregatedMirrorInvalidBuildNumber: int = auto()
    AggregatedMirrorCannotConnect: int = auto()
    NotEnoughLeadingCharsWildcard: int = auto()
    AggregatedMirrorCannotImpersonate: int = auto()
    Unexpected: int = auto()
    AccessDenied: int = auto()
    LicenseQueriesExpired: int = auto()
    InvalidSession: int = auto()
    SearchDisabled: int = auto()
    InvalidDocument: int = auto()
    NotAllowedInReadOnlyMode: int = auto()
    TaggingIsDisabled: int = auto()
    TaggingNotAllowed: int = auto()
    IndexNotStarted: int = auto()
    InvalidCustomEvaluatorSyntax: int = auto()
    UnknownCustomEvaluatorFunction: int = auto()
    TaggingFieldDoesntExist: int = auto()
    TaggingValueTooLong: int = auto()
    InvalidQueryFunction: int = auto()
    InvalidQueryFunctionField: int = auto()
    InvalidQueryFunctionFieldType: int = auto()
    InvalidQueryFunctionSyntax: int = auto()
    QueryTimeOut: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class FailedToImpersonateUsersException(ExceptionBase, hint="Coveo.SearchService.FailedToImpersonateUsersException"):
    """Exception thrown when user impersonification failed for some UserIds.

    Attributes:
        is_trusted: Indicates whether the client certificate was accepted by the server.
        user_ids: UserIds that were rejected by the server (usually in Session.UserId or AdditionalUserIds).
    """

    is_trusted: Opt[bool] = None
    user_ids: Opt[List[UserId]] = None

    def __init__(self, *, is_trusted: Opt[bool] = None, user_ids: Opt[List[UserId]] = None) -> None:
        """

        Parameters:
            is_trusted: Indicates whether the client certificate was accepted by the server.
            user_ids: UserIds that were rejected by the server (usually in Session.UserId or AdditionalUserIds).
        """


@attrs(kw_only=True, auto_attribs=True)
class Highlight(JidType, hint="Coveo.SearchService.Highlight"):
    """Holds information about a highlight within a string (a keyword position).

    Attributes:
        offset: The position at which the keyword begins.
        length: The length of the keyword.
    """

    offset: Opt[int] = None
    length: Opt[int] = None

    def __init__(self, *, offset: Opt[int] = None, length: Opt[int] = None) -> None:
        """

        Parameters:
            offset: The position at which the keyword begins.
            length: The length of the keyword.
        """


@attrs(kw_only=True, auto_attribs=True)
class Sentence(JidType, hint="Coveo.SearchService.Sentence"):
    """

    Attributes:
        text: The sentence text.
        word_count: The number of words in the sentence.
        score: The score of the sentence for the current query.
        highlights: The vector of highlights in the sentence, according to the query terms.
    """

    text: Opt[str] = None
    word_count: Opt[int] = None
    score: Opt[int] = None
    highlights: Opt[List[Highlight]] = None

    def __init__(
        self,
        *,
        text: Opt[str] = None,
        word_count: Opt[int] = None,
        score: Opt[int] = None,
        highlights: Opt[List[Highlight]] = None,
    ) -> None:
        """

        Parameters:
            text: The sentence text.
            word_count: The number of words in the sentence.
            score: The score of the sentence for the current query.
            highlights: The vector of highlights in the sentence, according to the query terms.
        """


@attrs(kw_only=True, auto_attribs=True)
class Concept(JidType, hint="Coveo.SearchService.Concept"):
    """

    Attributes:
        text: The concept text.
        highlights: The vector of highlights in the concept, according to the query terms.
    """

    text: Opt[str] = None
    highlights: Opt[List[Highlight]] = None

    def __init__(self, *, text: Opt[str] = None, highlights: Opt[List[Highlight]] = None) -> None:
        """

        Parameters:
            text: The concept text.
            highlights: The vector of highlights in the concept, according to the query terms.
        """


@attrs(kw_only=True, auto_attribs=True)
class FieldValue(JidType, hint="Coveo.SearchService.FieldValue"):
    value: Opt[Any] = None
    source_type: Opt[SourceType] = None
    is_system: Opt[bool] = None

    def __init__(
        self, *, value: Opt[Any] = None, source_type: Opt[SourceType] = None, is_system: Opt[bool] = None
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ComputedFieldResult(JidType, hint="Coveo.SearchService.ComputedFieldResult"):
    """Describes a result from a <b>ComputedFieldRequest</b>.

    Attributes:
        result: The result of a computed field operation.
        variance: The variance (used to compute the variance and standard deviation only).
        variance_sum: The sum (used to compute the variance and standard deviation only).
        median_values: The values used to find the median (used to compute the median only).
        operation: The requested operation.
        number_of_docs: The number of documents used in performing the numerical operation.
    """

    result: Opt[float] = None
    variance: Opt[float] = None
    variance_sum: Opt[float] = None
    median_values: Opt[List[float]] = None
    operation: Opt[ComputedFieldOperation] = None
    number_of_docs: Opt[int] = None

    def __init__(
        self,
        *,
        result: Opt[float] = None,
        variance: Opt[float] = None,
        variance_sum: Opt[float] = None,
        median_values: Opt[List[float]] = None,
        operation: Opt[ComputedFieldOperation] = None,
        number_of_docs: Opt[int] = None,
    ) -> None:
        """

        Parameters:
            result: The result of a computed field operation.
            variance: The variance (used to compute the variance and standard deviation only).
            variance_sum: The sum (used to compute the variance and standard deviation only).
            median_values: The values used to find the median (used to compute the median only).
            operation: The requested operation.
            number_of_docs: The number of documents used in performing the numerical operation.
        """


class FacetValueType(JidEnumFlag):
    """Possible types for a FacetValue.

    Attributes:
        Desired: Value from the desired values.
        Standard: Standard facet value
    """

    Desired: int = auto()
    Standard: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class FacetValue(JidType, hint="Coveo.SearchService.FacetValue"):
    """Describes a value from a FacetResult.

    Attributes:
        display_value: The display value to use.
        lookup_value: The value looked up through <b>Facet.OptionalFieldValueToLookup</b>.
        value_for_sort: The value to sort. This has been processed to remove accents, casing, etc.
        number_of_occurrences: The number of occurrences of the value in the results.
        score: The score of the value. The score depends on the number of occurrences and how close are these from the top of the result list.
        chi_square: Chi-square score.
        computed_field_results: The Facet.ComputedFieldRequests results.
        is_range: Whether the result is a range or not.
        value_type: The value type: Standard or Desired.
        number_range_facet: The numeric values of the requested number range.
    """

    display_value: Opt[str] = None
    lookup_value: Opt[str] = None
    value_for_sort: Opt[str] = None
    number_of_occurrences: Opt[int] = None
    score: Opt[int] = None
    chi_square: Opt[float] = None
    computed_field_results: Opt[List[ComputedFieldResult]] = None
    is_range: Opt[bool] = None
    value_type: FacetValueType = FacetValueType.Standard
    number_range_facet: Opt[NumberRangeFacet] = None

    def __init__(
        self,
        *,
        display_value: Opt[str] = None,
        lookup_value: Opt[str] = None,
        value_for_sort: Opt[str] = None,
        number_of_occurrences: Opt[int] = None,
        score: Opt[int] = None,
        chi_square: Opt[float] = None,
        computed_field_results: Opt[List[ComputedFieldResult]] = None,
        is_range: Opt[bool] = None,
        value_type: FacetValueType = FacetValueType.Standard,
        number_range_facet: Opt[NumberRangeFacet] = None,
    ) -> None:
        """

        Parameters:
            display_value: The display value to use.
            lookup_value: The value looked up through <b>Facet.OptionalFieldValueToLookup</b>.
            value_for_sort: The value to sort. This has been processed to remove accents, casing, etc.
            number_of_occurrences: The number of occurrences of the value in the results.
            score: The score of the value. The score depends on the number of occurrences and how close are these from the top of the result list.
            chi_square: Chi-square score.
            computed_field_results: The Facet.ComputedFieldRequests results.
            is_range: Whether the result is a range or not.
            value_type: The value type: Standard or Desired.
            number_range_facet: The numeric values of the requested number range.
        """


@attrs(kw_only=True, auto_attribs=True)
class FacetResult(JidType, hint="Coveo.SearchService.FacetResult"):
    """

    Attributes:
        field_name: The name of the field whose values are listed.
        id_: The id given in Facet.Id
        lookup_field_name: The value from the Facet.OptionalFieldValueToLookup's lookup.
        display_values: The values and number of occurrences from the Facet request.
        global_computed_field_results: The results from Facet.ComputedFieldRequests.
        score: The score for the facet field.
    """

    field_name: Opt[str] = None
    id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"})
    lookup_field_name: Opt[str] = None
    display_values: Opt[List[FacetValue]] = None
    global_computed_field_results: Opt[List[ComputedFieldResult]] = None
    score: Opt[float] = None

    def __init__(
        self,
        *,
        field_name: Opt[str] = None,
        id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"}),
        lookup_field_name: Opt[str] = None,
        display_values: Opt[List[FacetValue]] = None,
        global_computed_field_results: Opt[List[ComputedFieldResult]] = None,
        score: Opt[float] = None,
    ) -> None:
        """

        Parameters:
            field_name: The name of the field whose values are listed.
            id_: The id given in Facet.Id
            lookup_field_name: The value from the Facet.OptionalFieldValueToLookup's lookup.
            display_values: The values and number of occurrences from the Facet request.
            global_computed_field_results: The results from Facet.ComputedFieldRequests.
            score: The score for the facet field.
        """


@attrs(kw_only=True, auto_attribs=True)
class FacetFieldValue(JidType, hint="Coveo.SearchService.FacetFieldValue"):
    """One facet value returned from ListFacetFieldValues.

    Attributes:
        value: The facet value.
        number_of_occurrences: The number of documents having that value
    """

    value: Opt[str] = None
    number_of_occurrences: Opt[int] = None

    def __init__(self, *, value: Opt[str] = None, number_of_occurrences: Opt[int] = None) -> None:
        """

        Parameters:
            value: The facet value.
            number_of_occurrences: The number of documents having that value
        """


@attrs(kw_only=True, auto_attribs=True)
class ListFacetFieldValuesParameters(JidType, hint="Coveo.SearchService.ListFacetFieldValuesParameters"):
    field_name: Opt[str] = None
    query_expression: Opt[str] = None
    query_expression_constant: Opt[str] = None
    query_expression_mandatory: Opt[str] = None
    query_expression_disjunction: Opt[str] = None
    matching_pattern: Opt[str] = None
    matching_pattern_type: Opt[ListFacetFieldValuesRequest] = None
    sort_by_occurrences: Opt[bool] = None
    ignore_accents: Opt[bool] = None
    max_to_return: Opt[int] = None

    def __init__(
        self,
        *,
        field_name: Opt[str] = None,
        query_expression: Opt[str] = None,
        query_expression_constant: Opt[str] = None,
        query_expression_mandatory: Opt[str] = None,
        query_expression_disjunction: Opt[str] = None,
        matching_pattern: Opt[str] = None,
        matching_pattern_type: Opt[ListFacetFieldValuesRequest] = None,
        sort_by_occurrences: Opt[bool] = None,
        ignore_accents: Opt[bool] = None,
        max_to_return: Opt[int] = None,
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class WordCorrection(JidType, hint="Coveo.SearchService.WordCorrection"):
    """Holds the data for a word correction.

    Attributes:
        offset: The position at which the correction was made.
        length: The length of the word corrected.
        original_word: The original word on which the correction was made.
        corrected_word: The corrected word.
    """

    offset: Opt[int] = None
    length: Opt[int] = None
    original_word: Opt[str] = None
    corrected_word: Opt[str] = None

    def __init__(
        self,
        *,
        offset: Opt[int] = None,
        length: Opt[int] = None,
        original_word: Opt[str] = None,
        corrected_word: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            offset: The position at which the correction was made.
            length: The length of the word corrected.
            original_word: The original word on which the correction was made.
            corrected_word: The corrected word.
        """


@attrs(kw_only=True, auto_attribs=True)
class QueryCorrection(JidType, hint="Coveo.SearchService.QueryCorrection"):
    """Holds the data for a query correction.

    Attributes:
        corrected_query: The corrected query. This contains the full query, with all corrections applied, but without any HTML tag to identify them.
        word_corrections: The <b>WordCorrection</b> objects holding information about each word that was corrected. Those objects provide the positions of the corrections in the query, allowing you to highlight them in some way so that the user may see them.
    """

    corrected_query: Opt[str] = None
    word_corrections: Opt[List[WordCorrection]] = None

    def __init__(self, *, corrected_query: Opt[str] = None, word_corrections: Opt[List[WordCorrection]] = None) -> None:
        """

        Parameters:
            corrected_query: The corrected query. This contains the full query, with all corrections applied, but without any HTML tag to identify them.
            word_corrections: The <b>WordCorrection</b> objects holding information about each word that was corrected. Those objects provide the positions of the corrections in the query, allowing you to highlight them in some way so that the user may see them.
        """


@attrs(kw_only=True, auto_attribs=True)
class SortInformation(JidType, hint="Coveo.SearchService.SortInformation"):
    """Sort data needed to sort on fields when using multiple indexes.

    Attributes:
        type_: Type of the field on which the sort is made.
        ascending: Whether the sort is ascending or not.
        has_value: Whether the result has a value for that given field or not.
        value: The field value, if applicable.
    """

    type_: Opt[int] = attrib(default=None, metadata={CASING: "Type"})
    ascending: Opt[bool] = None
    has_value: Opt[bool] = None
    value: Opt[Any] = None

    def __init__(
        self,
        *,
        type_: Opt[int] = attrib(default=None, metadata={CASING: "Type"}),
        ascending: Opt[bool] = None,
        has_value: Opt[bool] = None,
        value: Opt[Any] = None,
    ) -> None:
        """

        Parameters:
            type_: Type of the field on which the sort is made.
            ascending: Whether the sort is ascending or not.
            has_value: Whether the result has a value for that given field or not.
            value: The field value, if applicable.
        """


@attrs(kw_only=True, auto_attribs=True)
class QueryResult(JidType, hint="Coveo.SearchService.QueryResult"):
    """Holds information about a single query result.

    Attributes:
        index_name: The name of the index from which this result comes from. This is only populated when aggregating multiple indexes.
        collection_id: The id of the collection the document comes from, as found in the admin's definition of collections.
        source_id: The id of the source the document comes from, as found in the admin's definition of sources.
        unique_id: The unique identifier of the result.
        uri: The uri of the result. Loading this uri in a browser opens the result from its original location.
        printable_uri: The printable version of the uri of the result. This field is considered equal to the Field <b>Uri</b> if <b>PrintableUri</b> is empty. This field is useful for some types of results (namely Microsoft Exchange), because the uri used to open email within outlook consists of a hex-encoded blob. For those results, the printable uri is the path within the MAPI folders where the items was found.
        title: The title of the result.
        size: The size of the result, in bytes.
        indexed_date: The indexation date of the document.
        flags: Flags describing the resulting document.
        date: The last modification date of the document.
        sentences: Vector of summary sentences with their highlights. Note that QueryParams.ExcerptLength has to be different from 0 to get them.
        concepts: The concepts of the result. The concepts are words (along with their highlights) that have been identified as important by the same linguistic algorithms that the ones used to generate the summary.
        excerpt: The excerpt of the result. This excerpt consists of passages of the document that contain the query keywords that have been entered.<p>To retrieve this value, you must set the <b>QueryParams.ExcerptLength</b> to a non-zero value.</p>
        fields: System and user fields.
        last_time_clicked: The last time the result was viewed by the user that performed the query.
        number_of_clicks: The number of times the result has been viewed by the user that performed the query.
        summary: The summary of the result. This summary is automatically generated for each result when it is indexed. It is created by advanced linguistic algorithms that attempt to locate the important sentences in the document. To retrieve this value, you must set the QueryParams.SummaryLength property to a non-zero value.
        tags: The map of tags.
        loaded_text: The text loaded from the document
        score: The score of the result for the query.
        is_index_browser_result: Whether the result is an index browser result (trimmed down), or a regular one.
        filtered_results: The results filtered by the custom filter.
        parent_result: The parent result, if applicable.
        total_custom_filter_results: Total number that could fill FilteredResults.
        title_highlights: The positions of the query keywords within the title.
        printable_uri_highlights: The positions of the query keywords within the printable uri.
        excerpt_highlights: The positions of the query keywords within the excerpt.
        first_sentences: Extracted from the excerpt if QueryParams.ExtractFirstSentences is true. Note that QueryParams.ExcerptLength has to be non-zero.
        first_sentences_highlights: The FirstSentences highlights.
        summary_highlights: See summary above.
        ranking_info: String that contains the ranking weights given to document (only filled if required).
        ranking_information_json: Json string that contains the ranking weights given to a document.
        absent_terms: The list of terms not matching the result
    """

    index_name: Opt[str] = None
    collection_id: Opt[int] = None
    source_id: Opt[int] = None
    unique_id: Opt[str] = None
    uri: Opt[str] = None
    printable_uri: Opt[str] = None
    target_uri: Opt[str] = None
    title: Opt[str] = None
    size: Opt[int] = None
    indexed_date: Opt[datetime] = None
    flags: Opt[DocumentFlag] = None
    date: Opt[datetime] = None
    sentences: Opt[List[Sentence]] = None
    concepts: Opt[List[Concept]] = None
    excerpt: Opt[str] = None
    fields: Opt[Dict[str, FieldValue]] = None
    last_time_clicked: Opt[datetime] = None
    number_of_clicks: Opt[int] = None
    summary: Opt[str] = None
    tags: Opt[Dict[str, List[str]]] = None
    loaded_text: Opt[str] = None
    score: Opt[int] = None
    pct_score: Opt[float] = None
    is_index_browser_result: Opt[bool] = None
    filtered_results: "Opt[List[QueryResult]]" = None
    parent_result: "Opt[QueryResult]" = None
    total_custom_filter_results: Opt[int] = None
    title_highlights: Opt[List[Highlight]] = None
    printable_uri_highlights: Opt[List[Highlight]] = None
    excerpt_highlights: Opt[List[Highlight]] = None
    first_sentences: Opt[str] = None
    first_sentences_highlights: Opt[List[Highlight]] = None
    summary_highlights: Opt[List[Highlight]] = None
    ranking_info: Opt[str] = None
    ranking_information_json: Opt[str] = None
    text_size: Opt[int] = None
    detected_language: Opt[Language] = None
    shingle_bag: Opt[Union[str, bytes]] = None
    summary_sentences: Opt[List[Sentence]] = None
    wide_score: Opt[int] = None
    sort_information: Opt[List[SortInformation]] = None
    custom_filter_key: Opt[str] = None
    absent_terms: Opt[List[str]] = None

    def __init__(
        self,
        *,
        index_name: Opt[str] = None,
        collection_id: Opt[int] = None,
        source_id: Opt[int] = None,
        unique_id: Opt[str] = None,
        uri: Opt[str] = None,
        printable_uri: Opt[str] = None,
        target_uri: Opt[str] = None,
        title: Opt[str] = None,
        size: Opt[int] = None,
        indexed_date: Opt[datetime] = None,
        flags: Opt[DocumentFlag] = None,
        date: Opt[datetime] = None,
        sentences: Opt[List[Sentence]] = None,
        concepts: Opt[List[Concept]] = None,
        excerpt: Opt[str] = None,
        fields: Opt[Dict[str, FieldValue]] = None,
        last_time_clicked: Opt[datetime] = None,
        number_of_clicks: Opt[int] = None,
        summary: Opt[str] = None,
        tags: Opt[Dict[str, List[str]]] = None,
        loaded_text: Opt[str] = None,
        score: Opt[int] = None,
        pct_score: Opt[float] = None,
        is_index_browser_result: Opt[bool] = None,
        filtered_results: "Opt[List[QueryResult]]" = None,
        parent_result: "Opt[QueryResult]" = None,
        total_custom_filter_results: Opt[int] = None,
        title_highlights: Opt[List[Highlight]] = None,
        printable_uri_highlights: Opt[List[Highlight]] = None,
        excerpt_highlights: Opt[List[Highlight]] = None,
        first_sentences: Opt[str] = None,
        first_sentences_highlights: Opt[List[Highlight]] = None,
        summary_highlights: Opt[List[Highlight]] = None,
        ranking_info: Opt[str] = None,
        ranking_information_json: Opt[str] = None,
        text_size: Opt[int] = None,
        detected_language: Opt[Language] = None,
        shingle_bag: Opt[Union[str, bytes]] = None,
        summary_sentences: Opt[List[Sentence]] = None,
        wide_score: Opt[int] = None,
        sort_information: Opt[List[SortInformation]] = None,
        custom_filter_key: Opt[str] = None,
        absent_terms: Opt[List[str]] = None,
    ) -> None:
        """

        Parameters:
            index_name: The name of the index from which this result comes from. This is only populated when aggregating multiple indexes.
            collection_id: The id of the collection the document comes from, as found in the admin's definition of collections.
            source_id: The id of the source the document comes from, as found in the admin's definition of sources.
            unique_id: The unique identifier of the result.
            uri: The uri of the result. Loading this uri in a browser opens the result from its original location.
            printable_uri: The printable version of the uri of the result. This field is considered equal to the Field <b>Uri</b> if <b>PrintableUri</b> is empty. This field is useful for some types of results (namely Microsoft Exchange), because the uri used to open email within outlook consists of a hex-encoded blob. For those results, the printable uri is the path within the MAPI folders where the items was found.
            title: The title of the result.
            size: The size of the result, in bytes.
            indexed_date: The indexation date of the document.
            flags: Flags describing the resulting document.
            date: The last modification date of the document.
            sentences: Vector of summary sentences with their highlights. Note that QueryParams.ExcerptLength has to be different from 0 to get them.
            concepts: The concepts of the result. The concepts are words (along with their highlights) that have been identified as important by the same linguistic algorithms that the ones used to generate the summary.
            excerpt: The excerpt of the result. This excerpt consists of passages of the document that contain the query keywords that have been entered.<p>To retrieve this value, you must set the <b>QueryParams.ExcerptLength</b> to a non-zero value.</p>
            fields: System and user fields.
            last_time_clicked: The last time the result was viewed by the user that performed the query.
            number_of_clicks: The number of times the result has been viewed by the user that performed the query.
            summary: The summary of the result. This summary is automatically generated for each result when it is indexed. It is created by advanced linguistic algorithms that attempt to locate the important sentences in the document. To retrieve this value, you must set the QueryParams.SummaryLength property to a non-zero value.
            tags: The map of tags.
            loaded_text: The text loaded from the document
            score: The score of the result for the query.
            is_index_browser_result: Whether the result is an index browser result (trimmed down), or a regular one.
            filtered_results: The results filtered by the custom filter.
            parent_result: The parent result, if applicable.
            total_custom_filter_results: Total number that could fill FilteredResults.
            title_highlights: The positions of the query keywords within the title.
            printable_uri_highlights: The positions of the query keywords within the printable uri.
            excerpt_highlights: The positions of the query keywords within the excerpt.
            first_sentences: Extracted from the excerpt if QueryParams.ExtractFirstSentences is true. Note that QueryParams.ExcerptLength has to be non-zero.
            first_sentences_highlights: The FirstSentences highlights.
            summary_highlights: See summary above.
            ranking_info: String that contains the ranking weights given to document (only filled if required).
            ranking_information_json: Json string that contains the ranking weights given to a document.
            absent_terms: The list of terms not matching the result
        """


@attrs(kw_only=True, auto_attribs=True)
class TermToHighlight(JidType, hint="Coveo.SearchService.TermToHighlight"):
    """Holds a term to highlight.

    Attributes:
        original_term: The original term that was queried.
        expansions: The expansions for the queried term.
    """

    original_term: Opt[str] = None
    expansions: Opt[List[str]] = None

    def __init__(self, *, original_term: Opt[str] = None, expansions: Opt[List[str]] = None) -> None:
        """

        Parameters:
            original_term: The original term that was queried.
            expansions: The expansions for the queried term.
        """


@attrs(kw_only=True, auto_attribs=True)
class ExceptionInfo(JidType, hint="Coveo.SearchService.ExceptionInfo"):
    """Exception code and context.

    Attributes:
        exception_code: An error occurred if this is not 'NoException'. ExceptionContext may contain additional information.
    """

    exception_code: Opt[QueryException] = None
    exception_context: Opt[str] = None

    def __init__(self, *, exception_code: Opt[QueryException] = None, exception_context: Opt[str] = None) -> None:
        """

        Parameters:
            exception_code: An error occurred if this is not 'NoException'. ExceptionContext may contain additional information.
        """


@attrs(kw_only=True, auto_attribs=True)
class TagFieldInfo(JidType, hint="Coveo.SearchService.TagFieldInfo"):
    """Holds the results of a TagFields or TagValues on a single GDI server.

    Attributes:
        exception: Exception code, and message.
        values: List of term field names (for TagFields) or a list of tag field values (for TagValues).
    """

    exception: Opt[ExceptionInfo] = None
    values: Opt[List[str]] = None

    def __init__(self, *, exception: Opt[ExceptionInfo] = None, values: Opt[List[str]] = None) -> None:
        """

        Parameters:
            exception: Exception code, and message.
            values: List of term field names (for TagFields) or a list of tag field values (for TagValues).
        """


@attrs(kw_only=True, auto_attribs=True)
class QueryResults(JidType, hint="Coveo.SearchService.QueryResults"):
    """Holds the results of a query.

    Attributes:
        log_entry_id: Log entry ID of the executed query.
        cpu_time: Total CPU time to execute the query (Seconds, whole and fractional).
        total_count: The total number of documents matching the query.
        total_count_filtered: The total number of filtered documents matching the query. This number may be different from TotalCount if duplicate document filtering has been enabled through the <b>QueryParams.EnableDuplicateFiltering</b> property.
        exception_info: An error occurred if this is not 'NoException'. ExceptionContext may contain additional information.
        query_corrections: The <b>QueryCorrection</b> objects holding information about the potential query corrections. Use those corrections to implement the <b>Did You Mean</b> feature. Although several potential corrections can be specified, typically only the first one is used (a single correction may provide corrections for several different words in the query).
        filtered_duplicates: Will be <code>True</code> if duplicate results are filtered. If no duplicate is found in the results, the value will be <code>False</code>.
        results: The <b>QueryResult</b> objects holding information about the individual results that were retrieved.
        facet_results: The results from the <b>Facet</b> requests.
        terms_to_highlight: The list of terms used for highlighting.
        phrases_to_highlight: The list of phrases used for highlighting.
        query_profiling_info: String that contains the query profiling information (only filled if required).
    """

    log_entry_id: Opt[int] = attrib(default=None, metadata={CASING: "LogEntryID"})
    cpu_time: Opt[float] = None
    total_count: Opt[int] = None
    total_count_filtered: Opt[int] = None
    exception_info: Opt[ExceptionInfo] = None
    query_corrections: Opt[List[QueryCorrection]] = None
    filtered_duplicates: Opt[bool] = None
    results: Opt[List[QueryResult]] = None
    facet_results: Opt[List[FacetResult]] = None
    terms_to_highlight: Opt[List[TermToHighlight]] = None
    phrases_to_highlight: Opt[List[List[TermToHighlight]]] = None
    query_profiling_info: Opt[str] = None
    ranking_configuration: Opt[int] = None

    def __init__(
        self,
        *,
        log_entry_id: Opt[int] = attrib(default=None, metadata={CASING: "LogEntryID"}),
        cpu_time: Opt[float] = None,
        total_count: Opt[int] = None,
        total_count_filtered: Opt[int] = None,
        exception_info: Opt[ExceptionInfo] = None,
        query_corrections: Opt[List[QueryCorrection]] = None,
        filtered_duplicates: Opt[bool] = None,
        results: Opt[List[QueryResult]] = None,
        facet_results: Opt[List[FacetResult]] = None,
        terms_to_highlight: Opt[List[TermToHighlight]] = None,
        phrases_to_highlight: Opt[List[List[TermToHighlight]]] = None,
        query_profiling_info: Opt[str] = None,
        ranking_configuration: Opt[int] = None,
    ) -> None:
        """

        Parameters:
            log_entry_id: Log entry ID of the executed query.
            cpu_time: Total CPU time to execute the query (Seconds, whole and fractional).
            total_count: The total number of documents matching the query.
            total_count_filtered: The total number of filtered documents matching the query. This number may be different from TotalCount if duplicate document filtering has been enabled through the <b>QueryParams.EnableDuplicateFiltering</b> property.
            exception_info: An error occurred if this is not 'NoException'. ExceptionContext may contain additional information.
            query_corrections: The <b>QueryCorrection</b> objects holding information about the potential query corrections. Use those corrections to implement the <b>Did You Mean</b> feature. Although several potential corrections can be specified, typically only the first one is used (a single correction may provide corrections for several different words in the query).
            filtered_duplicates: Will be <code>True</code> if duplicate results are filtered. If no duplicate is found in the results, the value will be <code>False</code>.
            results: The <b>QueryResult</b> objects holding information about the individual results that were retrieved.
            facet_results: The results from the <b>Facet</b> requests.
            terms_to_highlight: The list of terms used for highlighting.
            phrases_to_highlight: The list of phrases used for highlighting.
            query_profiling_info: String that contains the query profiling information (only filled if required).
        """


@attrs(kw_only=True, auto_attribs=True)
class HighlightTag(JidType, hint="Coveo.SearchService.HighlightTag"):
    start: Opt[str] = None
    end: Opt[str] = None

    def __init__(self, *, start: Opt[str] = None, end: Opt[str] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class QueryHighlighter(JidType, hint="Coveo.SearchService.QueryHighlighter"):
    """Object that modifies the server behavior when asking for highlighted html."""

    use_stemming: bool = True
    use_stop_words: bool = True
    ignore_accents: bool = True
    use_wildcards: bool = True
    highlight_tags: Opt[List[HighlightTag]] = None

    def __init__(
        self,
        *,
        use_stemming: bool = True,
        use_stop_words: bool = True,
        ignore_accents: bool = True,
        use_wildcards: bool = True,
        highlight_tags: Opt[List[HighlightTag]] = None,
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class HtmlResult(JidType, hint="Coveo.SearchService.HtmlResult"):
    """

    Attributes:
        document_truncated: Document has been truncated.
        encoding_cp: Windows codepage of the resulting document.
        encoding_name: Encoding name of the resulting document.
        html: Document data.
    """

    document_truncated: Opt[bool] = None
    encoding_cp: Opt[int] = attrib(default=None, metadata={CASING: "EncodingCP"})
    encoding_name: Opt[str] = None
    html: Opt[str] = None

    def __init__(
        self,
        *,
        document_truncated: Opt[bool] = None,
        encoding_cp: Opt[int] = attrib(default=None, metadata={CASING: "EncodingCP"}),
        encoding_name: Opt[str] = None,
        html: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            document_truncated: Document has been truncated.
            encoding_cp: Windows codepage of the resulting document.
            encoding_name: Encoding name of the resulting document.
            html: Document data.
        """


class RatingValue(JidEnumFlag):
    """List of document rating values."""

    Undefined: int = auto()
    Lowest: int = auto()
    Low: int = auto()
    Average: int = auto()
    Good: int = auto()
    Best: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class SearchCollection(JidType, hint="Coveo.SearchService.SearchCollection"):
    id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"})
    name: Opt[str] = None

    def __init__(self, *, id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"}), name: Opt[str] = None) -> None:
        ...


class SecurityProviderOptions(JidEnumFlag):
    INVALID: int = auto()
    LOGIN: int = auto()
    AUTHORIZE: int = auto()
    LOGIN_EX: int = auto()
    VALID_FLAGS: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class SecurityProviderParam(JidType, hint="Coveo.SearchService.SecurityProviderParam"):
    """Describes a security provider parameter, as defined in the index configuration."""

    name: Opt[str] = None
    value: Opt[str] = None

    def __init__(self, *, name: Opt[str] = None, value: Opt[str] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SecurityProvider(JidType, hint="Coveo.SearchService.SecurityProvider"):
    """Describes a security provider, as defined in the index configuration."""

    id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"})
    name: Opt[str] = None
    params: Opt[List[SecurityProviderParam]] = None
    capabilities: Opt[SecurityProviderOptions] = None

    def __init__(
        self,
        *,
        id_: Opt[int] = attrib(default=None, metadata={CASING: "Id"}),
        name: Opt[str] = None,
        params: Opt[List[SecurityProviderParam]] = None,
        capabilities: Opt[SecurityProviderOptions] = None,
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SearchProviderData(JidType, hint="Coveo.SearchService.SearchProviderData"):
    """Describes some non-user-specific informations useful for queries.

    Attributes:
        collection_names: Name of the available collections.
    """

    wildcards_enabled: Opt[bool] = None
    wildcards_leading_chars: Opt[int] = None
    maximum_returned_results: Opt[int] = None
    queries_are_enabled: Opt[bool] = None
    read_only: Opt[bool] = None
    available_facet_fields: Opt[List[str]] = None
    available_multi_value_facet_fields: Opt[List[str]] = None
    available_sort_fields: Opt[List[str]] = None
    available_query_fields: Opt[List[str]] = None
    security_providers: Opt[List[SecurityProvider]] = None
    computed_facets_enabled: Opt[bool] = None
    analytics_enabled: Opt[bool] = None
    search_service_version: Opt[int] = None
    search_debug_argument_enabled: Opt[bool] = None
    collection_names: Opt[List[str]] = None

    def __init__(
        self,
        *,
        wildcards_enabled: Opt[bool] = None,
        wildcards_leading_chars: Opt[int] = None,
        maximum_returned_results: Opt[int] = None,
        queries_are_enabled: Opt[bool] = None,
        read_only: Opt[bool] = None,
        available_facet_fields: Opt[List[str]] = None,
        available_multi_value_facet_fields: Opt[List[str]] = None,
        available_sort_fields: Opt[List[str]] = None,
        available_query_fields: Opt[List[str]] = None,
        security_providers: Opt[List[SecurityProvider]] = None,
        computed_facets_enabled: Opt[bool] = None,
        analytics_enabled: Opt[bool] = None,
        search_service_version: Opt[int] = None,
        search_debug_argument_enabled: Opt[bool] = None,
        collection_names: Opt[List[str]] = None,
    ) -> None:
        """

        Parameters:
            collection_names: Name of the available collections.
        """


@attrs(kw_only=True, auto_attribs=True)
class SearchSessionData(JidType, hint="Coveo.SearchService.SearchSessionData"):
    """Describes some user-specific informations useful for queries.

    Attributes:
        collections: The collections the SearchSession user has access to.
    """

    collections: Opt[List[SearchCollection]] = None

    def __init__(self, *, collections: Opt[List[SearchCollection]] = None) -> None:
        """

        Parameters:
            collections: The collections the SearchSession user has access to.
        """


@attrs(kw_only=True, auto_attribs=True)
class SearchProviderField(JidType, hint="Coveo.SearchService.SearchProviderField"):
    """Describes a custom field."""

    name: Opt[str] = None
    description: Opt[str] = None
    default_value: Opt[str] = None
    field_type: Opt[int] = None
    field_source_type: Opt[int] = None
    include_in_query: Opt[bool] = None
    include_in_results: Opt[bool] = None
    native_field_name: Opt[str] = None

    def __init__(
        self,
        *,
        name: Opt[str] = None,
        description: Opt[str] = None,
        default_value: Opt[str] = None,
        field_type: Opt[int] = None,
        field_source_type: Opt[int] = None,
        include_in_query: Opt[bool] = None,
        include_in_results: Opt[bool] = None,
        native_field_name: Opt[str] = None,
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class NameValuePair(JidType, hint="Coveo.SearchService.NameValuePair"):
    """Used to tag or untag a batch of fields.

    Attributes:
        name: The name of the field to tag or untag
        value: The value to tag or untag.
    """

    name: Opt[str] = None
    value: Opt[str] = None

    def __init__(self, *, name: Opt[str] = None, value: Opt[str] = None) -> None:
        """

        Parameters:
            name: The name of the field to tag or untag
            value: The value to tag or untag.
        """


class ISearchServer(CoveoInterface):
    @api("POST/query")
    def execute_query(self, *, scope: Scope, params: QueryParams) -> QueryResults:
        """Executes a query using the <i>Params</i> query.<p>Returns the matching documents.</p>"""

    @api("POST/search_provider_data")
    def get_search_provider_data(self, *, scope: Scope) -> SearchProviderData:
        """Extracts user-independent informations from the index."""

    @api("POST/search_session_data")
    def get_search_session_data(self, *, scope: Scope) -> SearchSessionData:
        """Extracts user-specific informations from the index."""

    @api("POST/login")
    def authenticate_user(self, *, provider: str, user_name: str, password: str) -> UserId:
        """Authenticates a user to the server. The return value can be used in a <b>SearchSession</b> in future calls to the server."""

    @api("GET/stream")
    def load_data_stream(self, *, scope: Scope, doc_key: str, name: str) -> Union[str, bytes]:
        """Returns the named data stream for the named document as a byte array."""

    @api("GET/html")
    def load_html(self, *, scope: Scope, doc_key: str, stream_name: str, requested_output_size: int) -> HtmlResult:
        """Returns a portion of the html for the named document.

        Parameters:
            requested_output_size: Set this to 0 get the complete document
        """

    @api("GET/text")
    def load_text(self, *, scope: Scope, doc_key: str, requested_output_length: int) -> str:
        """Returns a portion of the text for the named document."""

    @api("GET/highlight_html")
    def highlight_html(
        self,
        *,
        scope: Scope,
        doc_key: str,
        highlighter: QueryHighlighter,
        query: str,
        stream_name: str,
        requested_output_size: int,
    ) -> HtmlResult:
        """Returns a portion the html for the named document, highlighted against the <i>Query</i> terms.

        Parameters:
            requested_output_size: Set this to 0 get the complete document
        """

    @api("POST/health_check")
    def health_check(self, *, scope: Scope) -> HealthCheckStatus:
        """Check that search is up"""
