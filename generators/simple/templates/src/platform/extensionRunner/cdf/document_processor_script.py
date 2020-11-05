"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/CoveoDocumentProcessorScript.jid

"""

from attr import attrs
from typing import Any, Dict, List, Optional as Opt, Union
from .root import CoveoInterface, JidType, api
from .document_processor import DocumentProcessorException
from .document_definition import BlobEntry, CompressionType, DataStreamValue, MetaDataValue, PermissionLevel
from .script_store import ScriptPackage
from .logger import LogEntry
from .document_config_definition import DocumentProcessorScriptParameters


@attrs(kw_only=True, auto_attribs=True)
class DocumentProcessorScriptException(DocumentProcessorException, hint="Coveo.DocumentProcessorScriptException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class MissingDocumentProcessorConfigException(
    DocumentProcessorScriptException, hint="Coveo.MissingDocumentProcessorConfigException"
):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidDocumentProcessorParametersException(
    DocumentProcessorScriptException, hint="Coveo.InvalidDocumentProcessorParametersException"
):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class UnknownScriptLanguageException(DocumentProcessorScriptException, hint="Coveo.UnknownScriptLanguageException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ScriptCompilationException(DocumentProcessorScriptException, hint="Coveo.ScriptCompilationException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class UnknownIdException(DocumentProcessorScriptException, hint="Coveo.UnknownIdException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ScriptingEngineReturnedErrorException(
    DocumentProcessorScriptException, hint="Coveo.ScriptingEngineReturnedErrorException"
):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ScriptIsDisabledException(DocumentProcessorScriptException, hint="Coveo.ScriptIsDisabledException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class PythonScriptException(DocumentProcessorScriptException, hint="Coveo.PythonScriptException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class PythonPackageException(DocumentProcessorScriptException, hint="Coveo.PythonPackageException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ScriptSkippedException(DocumentProcessorScriptException, hint="Coveo.ScriptSkippedException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class RejectedFromScriptException(DocumentProcessorScriptException, hint="Coveo.RejectedFromScriptException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ScriptingEngine(JidType, hint="Coveo.ScriptingEngine"):
    """

    Attributes:
        executable: The program to execute
        command_line: The command line to pass to the executable
        stream_data_path: Where the engine will save the stream created by the script
        recycle_interval: Number of scripts to execute before recycling the engine
        environment_variables: Additional environment variables for the script engine process
        number_to_keep_hot: Number of engine to keep ready for execution
        connection_string: Connection string to the engine
        org_isolation: Whether or not to have an engine for each organisation
        number_in_standby: Number of engine to keep in standby for execution
    """

    executable: Opt[str] = None
    command_line: Opt[str] = None
    stream_data_path: Opt[str] = None
    recycle_interval: Opt[int] = None
    environment_variables: Opt[List[str]] = None
    number_to_keep_hot: int = 10
    connection_string: Opt[str] = None
    org_isolation: bool = True
    number_in_standby: int = 2

    def __init__(
        self,
        *,
        executable: Opt[str] = None,
        command_line: Opt[str] = None,
        stream_data_path: Opt[str] = None,
        recycle_interval: Opt[int] = None,
        environment_variables: Opt[List[str]] = None,
        number_to_keep_hot: int = 10,
        connection_string: Opt[str] = None,
        org_isolation: bool = True,
        number_in_standby: int = 2,
    ) -> None:
        """

        Parameters:
            executable: The program to execute
            command_line: The command line to pass to the executable
            stream_data_path: Where the engine will save the stream created by the script
            recycle_interval: Number of scripts to execute before recycling the engine
            environment_variables: Additional environment variables for the script engine process
            number_to_keep_hot: Number of engine to keep ready for execution
            connection_string: Connection string to the engine
            org_isolation: Whether or not to have an engine for each organisation
            number_in_standby: Number of engine to keep in standby for execution
        """


@attrs(kw_only=True, auto_attribs=True)
class DocumentProcessorScriptConfiguration(JidType, hint="Coveo.DocumentProcessorScriptConfiguration"):
    """

    Attributes:
        engines: The engine definitons
        maximum_blob_size_to_return: Maximum inline stream size (in mb) that we can send to the engine
        compiled_code_cache_size: The size of compiled code to keep in cache
        compiled_code_cache_expiration_millis: The time in millis to keep a compiled code blob cached
        output_engine_logs_to_own_log: Whether to output the logs produced by the engines to our log
        blob_compression_type: The compression type to use when compressing output blobs
    """

    engines: Opt[Dict[str, ScriptingEngine]] = None
    maximum_blob_size_to_return: int = 10
    compiled_code_cache_size: int = 10485760
    compiled_code_cache_expiration_millis: int = 30000
    output_engine_logs_to_own_log: Opt[bool] = None
    blob_compression_type: CompressionType = CompressionType.ZLib

    def __init__(
        self,
        *,
        engines: Opt[Dict[str, ScriptingEngine]] = None,
        maximum_blob_size_to_return: int = 10,
        compiled_code_cache_size: int = 10485760,
        compiled_code_cache_expiration_millis: int = 30000,
        output_engine_logs_to_own_log: Opt[bool] = None,
        blob_compression_type: CompressionType = CompressionType.ZLib,
    ) -> None:
        """

        Parameters:
            engines: The engine definitons
            maximum_blob_size_to_return: Maximum inline stream size (in mb) that we can send to the engine
            compiled_code_cache_size: The size of compiled code to keep in cache
            compiled_code_cache_expiration_millis: The time in millis to keep a compiled code blob cached
            output_engine_logs_to_own_log: Whether to output the logs produced by the engines to our log
            blob_compression_type: The compression type to use when compressing output blobs
        """


class IScriptAdmin(CoveoInterface):
    """The API to change a script blade configuration."""

    @api("POST/config")
    def set_config(self, *, config: DocumentProcessorScriptConfiguration) -> None:
        """Change the script configuration.

        Parameters:
            config: The new configuration.
        """

    @api("GET/config")
    def get_config(self) -> DocumentProcessorScriptConfiguration:
        """Get the script blade configuration."""

    @api("POST/prepare")
    def prepare_packages(
        self, *, organization_id: str, packages: List[str], language: str, location: str, merge: bool
    ) -> List[ScriptPackage]:
        """

        Parameters:
            organization_id: The organization identifier.
            packages: The list of packages to prepare
            language: The language of the packages, ex: python
            location: Where to put the zip package in S3.
            merge: Whether to merge all packages together in one zip.
        """

    @api("POST/resume")
    def resume_scripting_engines(self) -> None:
        """Resume all paused scripting engines and disables all future pausing."""


@attrs(kw_only=True, auto_attribs=True)
class ScriptExecutionResult(JidType, hint="Coveo.ScriptExecutionResult"):
    """

    Attributes:
        meta_data: The meta data to update the document with
        permissions: The new permissions for document.
        log_entries: The logs entries we got while executing the script
        data_streams: The new data streams to add on the document
        system_log_entries: The system related logs entries we got while executing the script
    """

    meta_data: Opt[Dict[str, List[Any]]] = None
    permissions: Opt[List[PermissionLevel]] = None
    log_entries: Opt[List[LogEntry]] = None
    data_streams: Opt[Dict[str, BlobEntry]] = None
    system_log_entries: Opt[List[LogEntry]] = None

    def __init__(
        self,
        *,
        meta_data: Opt[Dict[str, List[Any]]] = None,
        permissions: Opt[List[PermissionLevel]] = None,
        log_entries: Opt[List[LogEntry]] = None,
        data_streams: Opt[Dict[str, BlobEntry]] = None,
        system_log_entries: Opt[List[LogEntry]] = None,
    ) -> None:
        """

        Parameters:
            meta_data: The meta data to update the document with
            permissions: The new permissions for document.
            log_entries: The logs entries we got while executing the script
            data_streams: The new data streams to add on the document
            system_log_entries: The system related logs entries we got while executing the script
        """


class IScriptingEngine(CoveoInterface):
    @api("POST/compile")
    def compile(self, *, script_id: str, code: str) -> Union[str, bytes]:
        """

        Parameters:
            script_id: The id of the script to compile
            code: The code to compile
        """

    @api("POST/execute", id_="Id")
    def execute(
        self,
        *,
        parameters: DocumentProcessorScriptParameters,
        id_: str,
        meta_data: List[MetaDataValue],
        meta_data_file: str,
        permissions: List[PermissionLevel],
        data_streams: Dict[str, List[DataStreamValue]],
        package_paths: List[str],
    ) -> ScriptExecutionResult:
        """

        Parameters:
            parameters: The script parameters.
            id_: The Id of this document.
            meta_data: The meta data values pertaining to this document.
            meta_data_file: File containing the document meta data
            permissions: The permissions of this document.
            data_streams: The requested data streams
            package_paths: Additional folders to load packages from.
        """

    @api("POST/prepare")
    def prepare_packages(self, *, packages: List[str], working_path: str, merge: bool) -> List[ScriptPackage]:
        """

        Parameters:
            packages: The list of packages to prepare
            working_path: The working path
            merge: Whether to merge all packages together in one zip.
        """

    @api("GET/logs")
    def get_last_log_entries(self) -> List[LogEntry]:
        ...
