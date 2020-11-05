"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/CoveoDocumentConfigDefinition.jid

"""

from attr import attrib, attrs
from enum import auto
from typing import Dict, List, Optional as Opt, Union
from .root import CASING, JidEnumFlag, JidType
from .script_store import ScriptPackage


@attrs(kw_only=True, auto_attribs=True)
class XMLMetaData(JidType, hint="Coveo.XMLMetaData"):
    name: Opt[str] = None
    value: Opt[str] = None

    def __init__(self, *, name: Opt[str] = None, value: Opt[str] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class XMLRecordDefinition(JidType, hint="Coveo.XMLRecordDefinition"):
    root: Opt[str] = None
    unique_id: Opt[str] = None
    body: Opt[str] = None
    title: Opt[str] = None
    uri: Opt[str] = attrib(default=None, metadata={CASING: "URI"})
    author: Opt[str] = None
    date: Opt[str] = None
    date_format: Opt[str] = None
    summary: Opt[str] = None
    unescape_xml_entities: bool = attrib(default=True, metadata={CASING: "UnescapeXMLEntities"})
    meta_data: Opt[List[XMLMetaData]] = None

    def __init__(
        self,
        *,
        root: Opt[str] = None,
        unique_id: Opt[str] = None,
        body: Opt[str] = None,
        title: Opt[str] = None,
        uri: Opt[str] = attrib(default=None, metadata={CASING: "URI"}),
        author: Opt[str] = None,
        date: Opt[str] = None,
        date_format: Opt[str] = None,
        summary: Opt[str] = None,
        unescape_xml_entities: bool = attrib(default=True, metadata={CASING: "UnescapeXMLEntities"}),
        meta_data: Opt[List[XMLMetaData]] = None,
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ConditionNode(JidType, hint="Coveo.ConditionNode"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class AndNode(ConditionNode, hint="Coveo.AndNode"):
    children: Opt[List[ConditionNode]] = None

    def __init__(self, *, children: Opt[List[ConditionNode]] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class OrNode(ConditionNode, hint="Coveo.OrNode"):
    children: Opt[List[ConditionNode]] = None

    def __init__(self, *, children: Opt[List[ConditionNode]] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class NotNode(ConditionNode, hint="Coveo.NotNode"):
    child: Opt[ConditionNode] = None

    def __init__(self, *, child: Opt[ConditionNode] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExistsNode(ConditionNode, hint="Coveo.ExistsNode"):
    meta_name: Opt[str] = None

    def __init__(self, *, meta_name: Opt[str] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class EqualsNode(ConditionNode, hint="Coveo.EqualsNode"):
    meta_name: Opt[str] = None
    values: Opt[List[str]] = None
    ignore_order: Opt[bool] = None
    case_sensitive: Opt[bool] = None

    def __init__(
        self,
        *,
        meta_name: Opt[str] = None,
        values: Opt[List[str]] = None,
        ignore_order: Opt[bool] = None,
        case_sensitive: Opt[bool] = None,
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class LowerThanNode(ConditionNode, hint="Coveo.LowerThanNode"):
    meta_name: Opt[str] = None
    value: Opt[str] = None
    match_all: Opt[bool] = None
    case_sensitive: Opt[bool] = None

    def __init__(
        self,
        *,
        meta_name: Opt[str] = None,
        value: Opt[str] = None,
        match_all: Opt[bool] = None,
        case_sensitive: Opt[bool] = None,
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class GreaterThanNode(ConditionNode, hint="Coveo.GreaterThanNode"):
    meta_name: Opt[str] = None
    value: Opt[str] = None
    match_all: Opt[bool] = None
    case_sensitive: Opt[bool] = None

    def __init__(
        self,
        *,
        meta_name: Opt[str] = None,
        value: Opt[str] = None,
        match_all: Opt[bool] = None,
        case_sensitive: Opt[bool] = None,
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class DocumentProcessorParameters(JidType, hint="Coveo.DocumentProcessorParameters"):
    """

    Attributes:
        values: The map of parameters
        delete_on_error: Whether to delete the document on a execution error
        condition: Execute only if this condition is true
        streams: The streams needed by the document processor
        name: The step name that will be use as Origin
    """

    values: Opt[Dict[str, str]] = None
    delete_on_error: Opt[bool] = None
    condition: Opt[ConditionNode] = None
    streams: Opt[List[str]] = None
    name: Opt[str] = None

    def __init__(
        self,
        *,
        values: Opt[Dict[str, str]] = None,
        delete_on_error: Opt[bool] = None,
        condition: Opt[ConditionNode] = None,
        streams: Opt[List[str]] = None,
        name: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            values: The map of parameters
            delete_on_error: Whether to delete the document on a execution error
            condition: Execute only if this condition is true
            streams: The streams needed by the document processor
            name: The step name that will be use as Origin
        """


@attrs(kw_only=True, auto_attribs=True)
class DocumentProcessorScriptParameters(DocumentProcessorParameters, hint="Coveo.DocumentProcessorScriptParameters"):
    """

    Attributes:
        language: The script language
        code: The script code
        compiled_code: The compiled script
        script_id: The unique id of the script
        script_location: The location of the script in the ScriptStore
        script_version: The version of the script in the ScriptStore
        timeout: Maximum script execution time
        packages: Packages needed by the script
    """

    language: Opt[str] = None
    code: Opt[str] = None
    compiled_code: Opt[Union[str, bytes]] = None
    script_id: Opt[str] = None
    script_location: Opt[str] = None
    script_version: Opt[str] = None
    timeout: Opt[int] = None
    packages: Opt[List[ScriptPackage]] = None

    def __init__(
        self,
        *,
        language: Opt[str] = None,
        code: Opt[str] = None,
        compiled_code: Opt[Union[str, bytes]] = None,
        script_id: Opt[str] = None,
        script_location: Opt[str] = None,
        script_version: Opt[str] = None,
        timeout: Opt[int] = None,
        packages: Opt[List[ScriptPackage]] = None,
    ) -> None:
        """

        Parameters:
            language: The script language
            code: The script code
            compiled_code: The compiled script
            script_id: The unique id of the script
            script_location: The location of the script in the ScriptStore
            script_version: The version of the script in the ScriptStore
            timeout: Maximum script execution time
            packages: Packages needed by the script
        """


@attrs(kw_only=True, auto_attribs=True)
class DocumentProcessor(JidType, hint="Coveo.DocumentProcessor"):
    """

    Attributes:
        type_: Main/Script
    """

    type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"})
    parameters: Opt[DocumentProcessorParameters] = None

    def __init__(
        self,
        *,
        type_: Opt[str] = attrib(default=None, metadata={CASING: "Type"}),
        parameters: Opt[DocumentProcessorParameters] = None,
    ) -> None:
        """

        Parameters:
            type_: Main/Script
        """


@attrs(kw_only=True, auto_attribs=True)
class CharsetDetectionHint(JidType, hint="Coveo.CharsetDetectionHint"):
    charset: str = "unsure"
    confidence: float = 0.5

    def __init__(self, *, charset: str = "unsure", confidence: float = 0.5) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class LanguageHint(JidType, hint="Coveo.LanguageHint"):
    language: Opt[str] = None
    probability: float = 1.0

    def __init__(self, *, language: Opt[str] = None, probability: float = 1.0) -> None:
        ...


class Action(JidEnumFlag):
    """

    Attributes:
        Retrieve: Retrieve and index the document
        Reference: Only index a reference on the document
        Ignore: Completely skip the document
    """

    Retrieve: int = auto()
    Reference: int = auto()
    Ignore: int = auto()


class ActionOnError(JidEnumFlag):
    """

    Attributes:
        Reference: Only index a reference on the document
        Ignore: Completely skip the document
    """

    Reference: int = auto()
    Ignore: int = auto()


class ConverterType(JidEnumFlag):
    """

    Attributes:
        Skip: Do not convert
    """

    Detect: int = auto()
    Skip: int = auto()
    Html: int = auto()
    IFilter: int = auto()
    Wordperfect: int = auto()
    Rtf: int = auto()
    Excel: int = auto()
    Word: int = auto()
    Pdf: int = auto()
    Powerpoint: int = auto()
    PlainText: int = auto()
    Zip: int = auto()
    Xml: int = auto()
    Msg: int = auto()
    Mime: int = auto()
    Image: int = auto()


class ExcerptSource(JidEnumFlag):
    Document: int = auto()
    Summary: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class ExtensionSetting(JidType, hint="Coveo.ExtensionSetting"):
    custom_converter: Opt[DocumentProcessor] = None
    action: Opt[Action] = None
    action_on_error: Opt[ActionOnError] = None
    converter: Opt[ConverterType] = None
    use_content_type: Opt[bool] = None
    index_container: bool = True
    file_type_value: Opt[str] = None
    generate_thumbnail: bool = True
    use_external_ht_ml_generator: Opt[bool] = attrib(default=None, metadata={CASING: "UseExternalHTMLGenerator"})
    convert_directly_to_html: Opt[bool] = None
    open_result_with_quick_view: Opt[bool] = None
    summarize_document: bool = True
    save_excerpt_blob: bool = True
    excerpt_source: Opt[ExcerptSource] = None

    def __init__(
        self,
        *,
        custom_converter: Opt[DocumentProcessor] = None,
        action: Opt[Action] = None,
        action_on_error: Opt[ActionOnError] = None,
        converter: Opt[ConverterType] = None,
        use_content_type: Opt[bool] = None,
        index_container: bool = True,
        file_type_value: Opt[str] = None,
        generate_thumbnail: bool = True,
        use_external_ht_ml_generator: Opt[bool] = attrib(default=None, metadata={CASING: "UseExternalHTMLGenerator"}),
        convert_directly_to_html: Opt[bool] = None,
        open_result_with_quick_view: Opt[bool] = None,
        summarize_document: bool = True,
        save_excerpt_blob: bool = True,
        excerpt_source: Opt[ExcerptSource] = None,
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExtensionSettingByExtension(JidType, hint="Coveo.ExtensionSettingByExtension"):
    extensions: Opt[List[str]] = None
    extension_setting: Opt[ExtensionSetting] = None

    def __init__(self, *, extensions: Opt[List[str]] = None, extension_setting: Opt[ExtensionSetting] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExtensionSettings(JidType, hint="Coveo.ExtensionSettings"):
    no_extension: Opt[ExtensionSetting] = None
    other: Opt[ExtensionSetting] = None
    by_extensions: Opt[List[ExtensionSettingByExtension]] = None
    by_content_types: Opt[List[ExtensionSettingByExtension]] = None

    def __init__(
        self,
        *,
        no_extension: Opt[ExtensionSetting] = None,
        other: Opt[ExtensionSetting] = None,
        by_extensions: Opt[List[ExtensionSettingByExtension]] = None,
        by_content_types: Opt[List[ExtensionSettingByExtension]] = None,
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class DocumentProcessorConfig(JidType, hint="Coveo.DocumentProcessorConfig"):
    max_ht_ml_output_size: int = attrib(default=10485760, metadata={CASING: "MaxHTMLOutputSize"})
    max_text_output_size: int = 52428800
    excel_floating_point_precision: int = 11
    image_minimum_size: int = 32
    timeout: int = 600
    report_progression_timeout: int = 600
    index_excel_numbers: bool = True
    style_sheet: Opt[str] = None
    languages_settings: Opt[str] = None
    xml_record_definitions: Opt[List[XMLRecordDefinition]] = attrib(
        default=None, metadata={CASING: "XMLRecordDefinitions"}
    )
    maximum_document_size: Opt[int] = None
    title_grammatical_score_weight: float = 0.7
    title_length_probability_weight: float = 0.7
    title_percentage_of_caps_first_letters_weight: float = 0.7
    title_position_score_weight: float = 0.8
    field_mapping_origin: Opt[str] = None
    summary_size: int = 2500
    maximum_number_of_pages_to_convert: Opt[int] = None
    generate_ht_ml: bool = attrib(default=True, metadata={CASING: "GenerateHTML"})
    use_clickable_uri_as_base_path: Opt[bool] = None
    add_raw_text_data_stream: Opt[bool] = None
    beautify_documents: bool = True
    index_meta: Opt[bool] = None
    open_result_with_quick_view: Opt[bool] = None
    summarize_document: bool = True
    save_excerpt_blob: bool = True
    excerpt_source: Opt[ExcerptSource] = None
    charset_detection_hint: Opt[CharsetDetectionHint] = None
    language_hints: Opt[List[LanguageHint]] = None
    extension_settings: Opt[ExtensionSettings] = None

    def __init__(
        self,
        *,
        max_ht_ml_output_size: int = attrib(default=10485760, metadata={CASING: "MaxHTMLOutputSize"}),
        max_text_output_size: int = 52428800,
        excel_floating_point_precision: int = 11,
        image_minimum_size: int = 32,
        timeout: int = 600,
        report_progression_timeout: int = 600,
        index_excel_numbers: bool = True,
        style_sheet: Opt[str] = None,
        languages_settings: Opt[str] = None,
        xml_record_definitions: Opt[List[XMLRecordDefinition]] = attrib(
            default=None, metadata={CASING: "XMLRecordDefinitions"}
        ),
        maximum_document_size: Opt[int] = None,
        title_grammatical_score_weight: float = 0.7,
        title_length_probability_weight: float = 0.7,
        title_percentage_of_caps_first_letters_weight: float = 0.7,
        title_position_score_weight: float = 0.8,
        field_mapping_origin: Opt[str] = None,
        summary_size: int = 2500,
        maximum_number_of_pages_to_convert: Opt[int] = None,
        generate_ht_ml: bool = attrib(default=True, metadata={CASING: "GenerateHTML"}),
        use_clickable_uri_as_base_path: Opt[bool] = None,
        add_raw_text_data_stream: Opt[bool] = None,
        beautify_documents: bool = True,
        index_meta: Opt[bool] = None,
        open_result_with_quick_view: Opt[bool] = None,
        summarize_document: bool = True,
        save_excerpt_blob: bool = True,
        excerpt_source: Opt[ExcerptSource] = None,
        charset_detection_hint: Opt[CharsetDetectionHint] = None,
        language_hints: Opt[List[LanguageHint]] = None,
        extension_settings: Opt[ExtensionSettings] = None,
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class DocumentConfig(JidType, hint="Coveo.DocumentConfig"):
    index_uri: Opt[str] = None
    document_processor_config: Opt[DocumentProcessorConfig] = None
    pre_conversions: Opt[List[DocumentProcessor]] = None
    post_conversions: Opt[List[DocumentProcessor]] = None
    parameters: Opt[Dict[str, str]] = None

    def __init__(
        self,
        *,
        index_uri: Opt[str] = None,
        document_processor_config: Opt[DocumentProcessorConfig] = None,
        pre_conversions: Opt[List[DocumentProcessor]] = None,
        post_conversions: Opt[List[DocumentProcessor]] = None,
        parameters: Opt[Dict[str, str]] = None,
    ) -> None:
        ...
