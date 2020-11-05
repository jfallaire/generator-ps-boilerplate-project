"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/CoveoDocumentConsumer.jid

"""

from attr import attrib, attrs
from typing import Dict, Optional as Opt
from .root import CASING, CoveoInterface, ExceptionBase, JidType, api
from .document_definition import Document
from .document_config_definition import DocumentConfig


@attrs(kw_only=True, auto_attribs=True)
class DocumentConsumerException(ExceptionBase, hint="Coveo.DocumentConsumerException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ThrottlingException(DocumentConsumerException, hint="Coveo.ThrottlingException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InternalServerException(DocumentConsumerException, hint="Coveo.InternalServerException"):
    def __init__(self) -> None:
        ...


class IDocumentConsumer(CoveoInterface):
    @api("POST/process_document")
    def process(self, *, document: Document, config: DocumentConfig) -> None:
        ...

    @api("POST/process_document_from_s3")
    def process_from_blob_store(self, *, blob_id: str) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class DPMConfiguration(JidType, hint="Coveo.DPMConfiguration"):
    """Configuration for the DPM.

    Attributes:
        document_processor_uris: The URI for each type of DocumentProcessor
        metric_interval: The query metric interval in seconds
        nb_threads: Number of threads to use for the DPM.
        field_service_uri: Uri for the fields service
        create_ipp_stream: Whether the DPM should perform the IndexPreProcessing
        source_service_uri: Uri for the source service
    """

    document_processor_uris: Opt[Dict[str, str]] = None
    metric_interval: int = 300
    nb_threads: int = 1
    field_service_uri: Opt[str] = None
    create_ipp_stream: Opt[bool] = attrib(default=None, metadata={CASING: "CreateIPPStream"})
    source_service_uri: Opt[str] = None

    def __init__(
        self,
        *,
        document_processor_uris: Opt[Dict[str, str]] = None,
        metric_interval: int = 300,
        nb_threads: int = 1,
        field_service_uri: Opt[str] = None,
        create_ipp_stream: Opt[bool] = attrib(default=None, metadata={CASING: "CreateIPPStream"}),
        source_service_uri: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            document_processor_uris: The URI for each type of DocumentProcessor
            metric_interval: The query metric interval in seconds
            nb_threads: Number of threads to use for the DPM.
            field_service_uri: Uri for the fields service
            create_ipp_stream: Whether the DPM should perform the IndexPreProcessing
            source_service_uri: Uri for the source service
        """


class IDocumentProcessorManager(CoveoInterface):
    """The DPM API exposes methods to interact with the DPM."""

    @api("POST/config")
    def set_config(self, *, configuration: DPMConfiguration) -> None:
        """Change the DPM's configuration.

        Parameters:
            configuration: The new configuration.
        """

    @api("GET/config")
    def get_config(self) -> DPMConfiguration:
        """Get the DPM's configuration."""

    @api("POST/start")
    def start_document_consumer(self) -> None:
        ...

    @api("POST/stop")
    def stop_document_consumer(self) -> None:
        ...


class IDocumentProcessorCallback(CoveoInterface):
    @api("POST/add_attachment")
    def add_attachment(
        self,
        *,
        attachment: Document,
        parent_id: str,
        organization_id: str,
        index_identifier_id: str,
        operation_id: int,
        source_key: str,
    ) -> None:
        """

        Parameters:
            attachment: The attachment.
            parent_id: The Id of the top parent document.
            organization_id: The organization for this parent
            index_identifier_id: The index identifier for this parent
            operation_id: The operationid that the parent comes from
            source_key: The Id of the source that contains this document.
        """
