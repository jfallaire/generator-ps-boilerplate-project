"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/DocumentDefinition/CoveoDocumentDefinition.jid

"""

from attr import attrib, attrs
from enum import auto
from typing import Any, Dict, List, Optional as Opt, Union
from .root import CASING, JidEnumFlag, JidType


class CompressionType(JidEnumFlag):
    """

    Attributes:
        Uncompressed: Document is uncompressed
        ZLib: Data is compressed with zlib
        GZip: Data is compressed with GZip
        LZMA: Data is compressed with LZMA (e.g. 7-zip)
        Deflate: Data is compressed with Zlib (No Header, e.g. DeflateStream from .Net)
    """

    Uncompressed: int = auto()
    ZLib: int = auto()
    GZip: int = auto()
    LZMA: int = auto()
    Deflate: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class BlobEntry(JidType, hint="Coveo.BlobEntry"):
    """A structure that represents a blob entry from a store.

    Attributes:
        id_: The Id of the blob.
        inline_blob: The blob content when inline.
        compression: The compression method on the blob
    """

    id_: Opt[str] = attrib(default=None, metadata={CASING: "Id"})
    inline_blob: Opt[Union[str, bytes]] = None
    compression: Opt[CompressionType] = None

    def __init__(
        self,
        *,
        id_: Opt[str] = attrib(default=None, metadata={CASING: "Id"}),
        inline_blob: Opt[Union[str, bytes]] = None,
        compression: Opt[CompressionType] = None,
    ) -> None:
        """

        Parameters:
            id_: The Id of the blob.
            inline_blob: The blob content when inline.
            compression: The compression method on the blob
        """


@attrs(kw_only=True, auto_attribs=True)
class LocalBlobEntry(BlobEntry, hint="Coveo.LocalBlobEntry"):
    """Blob entry that is stored locally

    Attributes:
        file_name: the local filename to access the blob from
    """

    file_name: Opt[str] = None

    def __init__(self, *, file_name: Opt[str] = None) -> None:
        """

        Parameters:
            file_name: the local filename to access the blob from
        """


class PermissionIdentityType(JidEnumFlag):
    """Defines permission identity types.

    Attributes:
        Unknown: Represents a standard, or undefined identity.
        User: Represents a 'User' identity.
        Group: Represents a 'Group' identity.
        VirtualGroup: Represents a 'VirtualGroup' identity.
    """

    Unknown: int = auto()
    User: int = auto()
    Group: int = auto()
    VirtualGroup: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class Permission(JidType, hint="Coveo.Permission"):
    """A structure that represents a single permission.

    Attributes:
        identity_type: The type of identity.
        security_provider: The name of the security provider.
        identity: The identity, as defined by the specified security provider.
        additional_info: The additional information
    """

    identity_type: Opt[PermissionIdentityType] = None
    security_provider: Opt[str] = None
    identity: Opt[str] = None
    additional_info: Opt[Dict[str, str]] = None

    def __init__(
        self,
        *,
        identity_type: Opt[PermissionIdentityType] = None,
        security_provider: Opt[str] = None,
        identity: Opt[str] = None,
        additional_info: Opt[Dict[str, str]] = None,
    ) -> None:
        """

        Parameters:
            identity_type: The type of identity.
            security_provider: The name of the security provider.
            identity: The identity, as defined by the specified security provider.
            additional_info: The additional information
        """


@attrs(kw_only=True, auto_attribs=True)
class SecurityIdentity(JidType, hint="Coveo.SecurityIdentity"):
    """A structure that represents a single security identity. Also known as a declarator.

    Attributes:
        identity_type: The type of security identity
        provider: Security provider associated with the identity.
        name: Name of the security identity.
        additional_info: Additional information associated with the security identity as key-value pairs.
    """

    identity_type: Opt[PermissionIdentityType] = None
    provider: Opt[str] = None
    name: Opt[str] = None
    additional_info: Opt[Dict[str, str]] = None

    def __init__(
        self,
        *,
        identity_type: Opt[PermissionIdentityType] = None,
        provider: Opt[str] = None,
        name: Opt[str] = None,
        additional_info: Opt[Dict[str, str]] = None,
    ) -> None:
        """

        Parameters:
            identity_type: The type of security identity
            provider: Security provider associated with the identity.
            name: Name of the security identity.
            additional_info: Additional information associated with the security identity as key-value pairs.
        """


@attrs(kw_only=True, auto_attribs=True)
class PermissionSet(JidType, hint="Coveo.PermissionSet"):
    """A structure that represents a collection of allowed and denied permissions.

    Attributes:
        allow_anonymous: Indicates if anonymous users (i.e.: everyone) are allowed.
        allowed_permissions: The list of allowed permissions.
        denied_permissions: The list of denied permissions.
        name: An optional permission set name.
    """

    allow_anonymous: Opt[bool] = None
    allowed_permissions: Opt[List[Permission]] = None
    denied_permissions: Opt[List[Permission]] = None
    name: Opt[str] = None

    def __init__(
        self,
        *,
        allow_anonymous: Opt[bool] = None,
        allowed_permissions: Opt[List[Permission]] = None,
        denied_permissions: Opt[List[Permission]] = None,
        name: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            allow_anonymous: Indicates if anonymous users (i.e.: everyone) are allowed.
            allowed_permissions: The list of allowed permissions.
            denied_permissions: The list of denied permissions.
            name: An optional permission set name.
        """


@attrs(kw_only=True, auto_attribs=True)
class PermissionLevel(JidType, hint="Coveo.PermissionLevel"):
    """A structure that represents a level of permission where multiple permission sets can be specified.

    Attributes:
        name: An optional permission level name.
    """

    permission_sets: Opt[List[PermissionSet]] = None
    name: Opt[str] = None

    def __init__(self, *, permission_sets: Opt[List[PermissionSet]] = None, name: Opt[str] = None) -> None:
        """

        Parameters:
            name: An optional permission level name.
        """


@attrs(kw_only=True, auto_attribs=True)
class PermissionModel(JidType, hint="Coveo.PermissionModel"):
    """A structure that represent a permissions model that contains one or many permission levels."""

    permission_levels: Opt[List[PermissionLevel]] = None

    def __init__(self, *, permission_levels: Opt[List[PermissionLevel]] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SummarySentence(JidType, hint="Coveo.SummarySentence"):
    """

    Attributes:
        text: The summary sentence text.
        word_count: The number of words in the summary sentence.
        score: The score of the sentence.
    """

    text: Opt[str] = None
    word_count: Opt[int] = None
    score: Opt[int] = None

    def __init__(self, *, text: Opt[str] = None, word_count: Opt[int] = None, score: Opt[int] = None) -> None:
        """

        Parameters:
            text: The summary sentence text.
            word_count: The number of words in the summary sentence.
            score: The score of the sentence.
        """


@attrs(kw_only=True, auto_attribs=True)
class DataStreamValue(JidType, hint="Coveo.DataStreamValue"):
    """A structure that represents a data stream.

    Attributes:
        value: The blob entry containing the data.
        origin: The name of the component that created this data.
    """

    value: Opt[BlobEntry] = None
    origin: Opt[str] = None

    def __init__(self, *, value: Opt[BlobEntry] = None, origin: Opt[str] = None) -> None:
        """

        Parameters:
            value: The blob entry containing the data.
            origin: The name of the component that created this data.
        """


@attrs(kw_only=True, auto_attribs=True)
class MetaDataValue(JidType, hint="Coveo.MetaDataValue"):
    """A structure that represents a collection of meta data from the same origin

    Attributes:
        values: The map of meta data.
        origin: The origin of the meta data.
    """

    values: Opt[Dict[str, List[Any]]] = None
    origin: Opt[str] = None

    def __init__(self, *, values: Opt[Dict[str, List[Any]]] = None, origin: Opt[str] = None) -> None:
        """

        Parameters:
            values: The map of meta data.
            origin: The origin of the meta data.
        """


class OperationType(JidEnumFlag):
    """Defines document operation types.

    Attributes:
        Add: Add the document.
        Delete: Delete a specific document.
        DeleteOlderThan: Delete documents that are older than /OperationId/.
        DeleteAndChildren: Delete the document and its children.
    """

    Add: int = auto()
    Delete: int = auto()
    DeleteOlderThan: int = auto()
    DeleteAndChildren: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class Document(JidType, hint="Coveo.Document"):
    """A structure that represents a document.

    Attributes:
        operation_id: An Id used to order operations.
        index_identifier: An identifier used to identify the index this document should go to.
        source_operation_id: The Id of the source operation that last processed this document.
        type_: The operation to perform on this document.
        source_key: The Id of the source that contains this document.
        source_id: The unique Id of the source that contains this document.
        organization_id: The Id of the organization to which this document belong.
        id_: The Id of this document.
        parent_id: The Id of the parent document.
        top_parent_id: The Id of the top parent document.
        permissions: The permissions of this document.
        meta_data: The meta data values pertaining to this document.
        data_streams: The data streams (blobs) associated with this document.
        attachments: The collection of children documents.
        attachment_ids: The collection of children ids.
    """

    operation_id: Opt[int] = None
    index_identifier: Opt[str] = None
    source_operation_id: Opt[str] = None
    type_: Opt[OperationType] = attrib(default=None, metadata={CASING: "Type"})
    source_key: Opt[str] = None
    source_id: Opt[str] = None
    organization_id: Opt[str] = None
    id_: Opt[str] = attrib(default=None, metadata={CASING: "Id"})
    parent_id: Opt[str] = None
    top_parent_id: Opt[str] = None
    permissions: Opt[List[PermissionLevel]] = None
    meta_data: Opt[List[MetaDataValue]] = None
    data_streams: Opt[Dict[str, List[DataStreamValue]]] = None
    attachments: "Opt[List[Document]]" = None
    attachment_ids: Opt[List[str]] = None

    def __init__(
        self,
        *,
        operation_id: Opt[int] = None,
        index_identifier: Opt[str] = None,
        source_operation_id: Opt[str] = None,
        type_: Opt[OperationType] = attrib(default=None, metadata={CASING: "Type"}),
        source_key: Opt[str] = None,
        source_id: Opt[str] = None,
        organization_id: Opt[str] = None,
        id_: Opt[str] = attrib(default=None, metadata={CASING: "Id"}),
        parent_id: Opt[str] = None,
        top_parent_id: Opt[str] = None,
        permissions: Opt[List[PermissionLevel]] = None,
        meta_data: Opt[List[MetaDataValue]] = None,
        data_streams: Opt[Dict[str, List[DataStreamValue]]] = None,
        attachments: "Opt[List[Document]]" = None,
        attachment_ids: Opt[List[str]] = None,
    ) -> None:
        """

        Parameters:
            operation_id: An Id used to order operations.
            index_identifier: An identifier used to identify the index this document should go to.
            source_operation_id: The Id of the source operation that last processed this document.
            type_: The operation to perform on this document.
            source_key: The Id of the source that contains this document.
            source_id: The unique Id of the source that contains this document.
            organization_id: The Id of the organization to which this document belong.
            id_: The Id of this document.
            parent_id: The Id of the parent document.
            top_parent_id: The Id of the top parent document.
            permissions: The permissions of this document.
            meta_data: The meta data values pertaining to this document.
            data_streams: The data streams (blobs) associated with this document.
            attachments: The collection of children documents.
            attachment_ids: The collection of children ids.
        """
