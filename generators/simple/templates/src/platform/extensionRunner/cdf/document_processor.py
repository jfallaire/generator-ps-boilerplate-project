"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/CoveoDocumentProcessor.jid

"""

from attr import attrib, attrs
from enum import auto
from typing import List, Optional as Opt
from .root import CASING, CoveoInterface, ExceptionBase, JidEnumFlag, JidType, MultiOut, QuitException, api
from .logger import LogEntry
from .document_definition import Document
from .document_config_definition import DocumentProcessorConfig, DocumentProcessorParameters


@attrs(kw_only=True, auto_attribs=True)
class DocumentProcessorException(ExceptionBase, hint="Coveo.DocumentProcessorException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ProcessingStoppedException(QuitException, hint="Coveo.ProcessingStoppedException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class EncryptedDocumentException(DocumentProcessorException, hint="Coveo.EncryptedDocumentException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class CopyProtectedDocumentException(DocumentProcessorException, hint="Coveo.CopyProtectedDocumentException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class CorruptedDocumentException(DocumentProcessorException, hint="Coveo.CorruptedDocumentException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class UnsupportedCharsetException(DocumentProcessorException, hint="Coveo.UnsupportedCharsetException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class UnsupportedVersionException(DocumentProcessorException, hint="Coveo.UnsupportedVersionException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class UnsupportedFileFormatException(DocumentProcessorException, hint="Coveo.UnsupportedFileFormatException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidFileSizeException(DocumentProcessorException, hint="Coveo.InvalidFileSizeException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class TimeoutException(DocumentProcessorException, hint="Coveo.TimeoutException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class RejectedDocumentException(DocumentProcessorException, hint="Coveo.RejectedDocumentException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ConverterConfigException(DocumentProcessorException, hint="Coveo.ConverterConfigException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class UnknownException(DocumentProcessorException, hint="Coveo.UnknownException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ConverterCrashException(DocumentProcessorException, hint="Coveo.ConverterCrashException"):
    def __init__(self) -> None:
        ...


class ExecutionResult(JidEnumFlag):
    Success: int = auto()
    Rejected: int = auto()
    ScriptError: int = auto()
    Timeout: int = auto()
    Skipped: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class ExecutionReport(JidType, hint="Coveo.ExecutionReport"):
    """Report on the execution of an operation"""

    logs: Opt[List[LogEntry]] = None
    duration: Opt[float] = None
    result: Opt[ExecutionResult] = None
    exception: Opt[str] = None

    def __init__(
        self,
        *,
        logs: Opt[List[LogEntry]] = None,
        duration: Opt[float] = None,
        result: Opt[ExecutionResult] = None,
        exception: Opt[str] = None,
    ) -> None:
        ...


class IDocumentProcessor(CoveoInterface):
    """The IDocumentProcessor API exposes methods to interact with the Coveo converter."""

    @api("POST/process_document")
    def process(
        self,
        *,
        document: Document,
        config: DocumentProcessorConfig,
        parameters: DocumentProcessorParameters,
        document_processor_callback_uri: str,
    ) -> MultiOut:
        """Process (convert) a document.

        Parameters:
            document: The document to convert.
            config: The processor configuration for this document.
            parameters: The processor parameters
            document_processor_callback_uri: The callback uri to add attachment
        """


@attrs(kw_only=True, auto_attribs=True)
class ConverterConfiguration(JidType, hint="Coveo.ConverterConfiguration"):
    """Configuration for the DPM.

    Attributes:
        temp_path: The temporary path for the converter.
        libre_office_path: The path to libre office (to generate an enhanced quickview).
        pdf2html_ex_path: The path to PF2HTMLEx (to generate an enhanced quickview).
        pdf2html_ex_params: The parameters to give to PDF2HTMLEx.
        disk_buffer_size: The size of the diskbuffer.
    """

    temp_path: Opt[str] = None
    libre_office_path: Opt[str] = None
    pdf2html_ex_path: Opt[str] = attrib(default=None, metadata={CASING: "PDF2HTMLEXPath"})
    pdf2html_ex_params: str = attrib(
        default="--hdpi 48 --vdpi 48 --embed-external-font 0", metadata={CASING: "PDF2HTMLEXParams"}
    )
    disk_buffer_size: int = 2097152

    def __init__(
        self,
        *,
        temp_path: Opt[str] = None,
        libre_office_path: Opt[str] = None,
        pdf2html_ex_path: Opt[str] = attrib(default=None, metadata={CASING: "PDF2HTMLEXPath"}),
        pdf2html_ex_params: str = attrib(
            default="--hdpi 48 --vdpi 48 --embed-external-font 0", metadata={CASING: "PDF2HTMLEXParams"}
        ),
        disk_buffer_size: int = 2097152,
    ) -> None:
        """

        Parameters:
            temp_path: The temporary path for the converter.
            libre_office_path: The path to libre office (to generate an enhanced quickview).
            pdf2html_ex_path: The path to PF2HTMLEx (to generate an enhanced quickview).
            pdf2html_ex_params: The parameters to give to PDF2HTMLEx.
            disk_buffer_size: The size of the diskbuffer.
        """


class IConverter(CoveoInterface):
    """The IConverter API to change a converter configuration."""

    @api("POST/config")
    def set_config(self, *, configuration: ConverterConfiguration) -> None:
        """Change the converter configuration.

        Parameters:
            configuration: The new configuration.
        """

    @api("GET/config")
    def get_config(self) -> ConverterConfiguration:
        """Get the converter configuration."""
