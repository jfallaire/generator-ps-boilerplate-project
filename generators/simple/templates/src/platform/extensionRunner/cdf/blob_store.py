"""
    - THIS FILE IS GENERATED -

dependencies/CDF/Cpp/BlobStoreBlade/CDFBlobStore.jid

"""

from attr import attrib, attrs
from enum import auto
from typing import List, Optional as Opt, Union
from .root import CASING, CoveoInterface, ExceptionBase, JidEnumFlag, JidType, MultiOut, api


@attrs(kw_only=True, auto_attribs=True)
class BlobStoreException(ExceptionBase, hint="Coveo.BlobStoreService.BlobStoreException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidBlobIdException(BlobStoreException, hint="Coveo.BlobStoreService.InvalidBlobIdException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class OutOfRangeException(BlobStoreException, hint="Coveo.BlobStoreService.OutOfRangeException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class BlobIdExistsException(BlobStoreException, hint="Coveo.BlobStoreService.BlobIdExistsException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class IncompleteBlobException(BlobStoreException, hint="Coveo.BlobStoreService.IncompleteBlobException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidChunkSizeException(BlobStoreException, hint="Coveo.BlobStoreService.InvalidChunkSizeException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InternalServerException(BlobStoreException, hint="Coveo.BlobStoreService.InternalServerException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ResendBlobException(BlobStoreException, hint="Coveo.BlobStoreService.ResendBlobException"):
    def __init__(self) -> None:
        ...


class ExpirationPolicyType(JidEnumFlag):
    """Defines garbage collection policy types.

    Attributes:
        Perennial: No expiration. Blob must be deleted explicitly.
        TTLAfterCreation: Blob will be deleted when its lifespan reaches the specified threshold.
    """

    Perennial: int = auto()
    TTLAfterCreation: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class ExpirationPolicy(JidType, hint="Coveo.BlobStoreService.ExpirationPolicy"):
    """Defines a garbage collection policy.

    Attributes:
        type_: Type of expiration policy (See ExpirationPolicyType).
        life_span_s: Desired lifespan of the object based on the policy type (in seconds). Ignored when using 'Perennial' policy type.
    """

    type_: Opt[ExpirationPolicyType] = attrib(default=None, metadata={CASING: "Type"})
    life_span_s: Opt[int] = attrib(default=None, metadata={CASING: "LifeSpan_s"})

    def __init__(
        self,
        *,
        type_: Opt[ExpirationPolicyType] = attrib(default=None, metadata={CASING: "Type"}),
        life_span_s: Opt[int] = attrib(default=None, metadata={CASING: "LifeSpan_s"}),
    ) -> None:
        """

        Parameters:
            type_: Type of expiration policy (See ExpirationPolicyType).
            life_span_s: Desired lifespan of the object based on the policy type (in seconds). Ignored when using 'Perennial' policy type.
        """


class IBlobStore(CoveoInterface):
    """The blob store API exposes methods to interact with this blob store. It can be used to store and retrieve any type of data."""

    @api("POST/blobs")
    def add_blob(
        self,
        *,
        data: Union[str, bytes],
        is_data_complete: bool,
        expiration_policy: ExpirationPolicy,
        total_size: int = 0,
    ) -> str:
        """Adds a new blob (or part of it) to the store.

        Parameters:
            data: The data to store.
            is_data_complete: Indicates if the blob is data complete. When passing false, the 'AppendData' method must be used to complete the data.
            expiration_policy: The expiration policy to use. Passing null is equivalent to passing ExpirationTypePolicy.Perennial.
            total_size: The complete blob size
        """

    @api("PUT/blobs/{blob_id}")
    def add_blob_with_id(
        self,
        *,
        blob_id: str,
        data: Union[str, bytes],
        is_data_complete: bool,
        expiration_policy: ExpirationPolicy,
        total_size: int = 0,
    ) -> None:
        """Adds a new blob (or part of it) to the store using a custom Id.

        Parameters:
            blob_id: A custom and unique Id that identifies the blob.
            data: The data to store.
            is_data_complete: Indicates if the blob is data complete. When passing false, the 'AppendData' method must be used to complete the data.
            expiration_policy: The expiration policy to use. Passing null is equivalent to passing ExpirationTypePolicy.Perennial.
            total_size: The complete blob size
        """

    @api("POST/blobs/{blob_id}/data")
    def append_data(self, *, blob_id: str, data: Union[str, bytes], is_data_complete: bool) -> None:
        """Appends bytes to an existing, incomplete blob.

        Parameters:
            blob_id: The Id of a blob.
            data: The data to append.
            is_data_complete: Indicates if the blob is now data complete.
        """

    @api("GET/blobs/{blob_id}/size")
    def get_blob_size(self, *, blob_id: str) -> int:
        """Returns the current size of a blob from the store.

        Parameters:
            blob_id: The Id of a blob.
        """

    @api("GET/blobs/{blob_id}")
    def get_blob(self, *, blob_id: str, start_pos: int, size: int) -> MultiOut:
        """Returns a blob (or part of it) from the store.

        Parameters:
            blob_id: The Id of a blob.
            start_pos: The byte position where reading should begin.
            size: The amount of bytes to read.
        """

    @api("DELETE/blobs/{blob_id}")
    def delete_blob(self, *, blob_id: str) -> None:
        """Deletes a blob from the store.

        Parameters:
            blob_id: The Id of a blob.
        """

    @api("DELETE/blobs")
    def delete_blobs(self, *, blob_ids: List[str]) -> None:
        """Deletes a batch of blobs from the blob store.

        Parameters:
            blob_ids: A batch of blob Ids.
        """

    @api("DELETE/blobs?prefix={Prefix}")
    def delete_blobs_where_id_starts_with(self, *, prefix: str) -> None:
        """Deletes all blobs where the BlobId starts with 'Prefix'.

        Parameters:
            prefix: A prefix used to locate blobs.
        """

    @api("GET/blobs/{blob_id}?exist}")
    def blob_exists(self, *, blob_id: str) -> bool:
        """Indicates if a blob exists in the store. Remark: A blob exists even when it's not data complete.

        Parameters:
            blob_id: The Id of a blob.
        """

    @api("POST/blobs/duplicate")
    def duplicate_blobs(self, *, original_blob_ids: List[str]) -> List[str]:
        """Duplicates a list of blobs in the store."""
