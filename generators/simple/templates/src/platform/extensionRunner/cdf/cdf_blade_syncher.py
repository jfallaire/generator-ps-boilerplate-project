"""
    - THIS FILE IS GENERATED -

dependencies/CDF/Cpp/BladeSyncher/CDFBladeSyncher.jid

"""

from attr import attrs
from enum import auto
from typing import List, Optional as Opt
from .root import CoveoInterface, ExceptionBase, JidEnumFlag, JidType, MultiOut, api


@attrs(kw_only=True, auto_attribs=True)
class BladeSyncherException(ExceptionBase, hint="CDF.BladeSyncherException"):
    """Base exception for all BladeSyncher exceptions."""

    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidSynchronizationTokenException(BladeSyncherException, hint="CDF.InvalidSynchronizationTokenException"):
    """This synchronization is no longer valid."""

    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class CannotBeginSynchronizationException(BladeSyncherException, hint="CDF.CannotBeginSynchronizationException"):
    """The blade cannot start a synchronization in its current state."""

    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SynchronizationCanceledException(BladeSyncherException, hint="CDF.SynchronizationCanceledException"):
    """Synchronization was canceled."""

    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class SynchronizationException(BladeSyncherException, hint="CDF.SynchronizationException"):
    """Unable to complete synchronization."""

    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class FileInfo(JidType, hint="CDF.FileInfo"):
    name: Opt[str] = None
    size: Opt[int] = None

    def __init__(self, *, name: Opt[str] = None, size: Opt[int] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class CompressionParameters(JidType, hint="CDF.CompressionParameters"):
    """Compression parameters to use for a synchronization."""

    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ZlibCompression(CompressionParameters, hint="CDF.ZlibCompression"):
    """Zlib compression definition"""

    def __init__(self) -> None:
        ...


class BloscCompressor(JidEnumFlag):
    BloscLZ: int = auto()
    LZ4: int = auto()
    LZ4HC: int = auto()
    Snappy: int = auto()
    Zlib: int = auto()
    Zstd: int = auto()


class BloscShuffleMode(JidEnumFlag):
    NoShuffle: int = auto()
    ByteShuffle: int = auto()
    BitShuffle: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class BloscCompression(CompressionParameters, hint="CDF.BloscCompression"):
    """Blosc compression definition"""

    compressor: BloscCompressor = BloscCompressor.LZ4
    compression_level: int = 1
    shuffle_mode: BloscShuffleMode = BloscShuffleMode.NoShuffle

    def __init__(
        self,
        *,
        compressor: BloscCompressor = BloscCompressor.LZ4,
        compression_level: int = 1,
        shuffle_mode: BloscShuffleMode = BloscShuffleMode.NoShuffle,
    ) -> None:
        ...


class IBladeSyncher(CoveoInterface):
    """The BladeSyncher interface."""

    @api("POST/synchronize?is_source={Source}")
    def begin_synchronize(self, *, source: bool, compression_parameters: CompressionParameters) -> str:
        """Start to synchronize this blade.

        Parameters:
            source: True for the source blade, false for the destination blade.
            compression_parameters: Compression parameters to use for the sync session.
        """

    @api("POST/synchronize/{synchronization_token}/end")
    def end_synchronize(self, *, source: bool, synchronization_token: str, in_synch: bool) -> None:
        """End to synchronize.

        Parameters:
            source: True for the source blade, false for the destination blade.
            synchronization_token: Synchronization token.
            in_synch: Whether or not the blade is synchronized.
        """

    @api("GET/file_list/{synchronization_token}")
    def get_file_list(self, *, synchronization_token: str) -> MultiOut:
        """Get the list of files to synchronize.

        Parameters:
            synchronization_token: Synchronization token.
        """

    @api("GET/file_info_list/{synchronization_token}")
    def get_file_info_list(self, *, synchronization_token: str) -> List[FileInfo]:
        """Get the list of file info to synchronize.

        Parameters:
            synchronization_token: Synchronization token.
        """

    @api("POST/get_file_data/{synchronization_token}")
    def get_file_data(self, *, synchronization_token: str, file_path: str, offset: int, size: int) -> MultiOut:
        """Returns information about a file.

        Parameters:
            synchronization_token: Synchronization token.
            file_path: Path and filename. Path is relative to working directory.
            offset: Offset of data block with the file.
            size: Size of data block.
        """

    @api("POST/get_file_data2/{synchronization_token}")
    def get_file_data2(self, *, synchronization_token: str, file_path: str, offset: int, size: int) -> MultiOut:
        """Returns information about a file.

        Parameters:
            synchronization_token: Synchronization token.
            file_path: Path and filename. Path is relative to working directory.
            offset: Offset of data block with the file.
            size: Size of data block.
        """

    @api("POST/synchronize", source_uri="SourceURI")
    def synchronize(
        self, *, source_uri: str, compress_data: bool, compression_parameters: CompressionParameters
    ) -> None:
        """Synchronize this blade with the data of another blade.

        Parameters:
            source_uri: URI of the source blade.
            compress_data: Whether to compress the transfered data.
            compression_parameters: Compression parameters to use for the sync session.
        """

    @api("GET/synchronize?is_source={Source}")
    def can_synchronize(self, *, source: bool) -> bool:
        """Verify if we can do the synchronization now.

        Parameters:
            source: True for the source blade, false for the destination blade.
        """

    @api("GET/synchronize?synchronization_token={SynchronizationToken}")
    def check_synchronization_token(self, *, synchronization_token: str) -> None:
        """Check if the synchronization token is still valid.

        Parameters:
            synchronization_token: Synchronization token.
        """

    @api("POST/synchronize?cancel")
    def cancel_synchronization(self) -> None:
        """Cancel current synchronization."""


class IBladeSyncherTokenProcessor(CoveoInterface):
    """A BladeSyncher token processor (internal use only)"""


class IBladeSyncherNotification(CoveoInterface):
    """The interface used to receive the outcome of a synchronization operation."""

    @api("POST/notifications/end_synchronize")
    def end_synchronize(self, *, in_synch: bool) -> None:
        """End to synchronize.

        Parameters:
            in_synch: Whether or not the blade is synchronized.
        """

    @api("POST/notifications/{progress}")
    def on_progress(self, *, progress: float) -> None:
        """Called to notify progression.

        Parameters:
            progress: The progress (from 0 to 1).
        """

    @api("POST/notifications/start_synchronize")
    def start_synchronize(self) -> None:
        """Called to notify that the synchronization is about to start."""

    @api("POST/notifications/start_transfer")
    def start_transfer(self) -> None:
        """Called to notify that the transfer of files is about to start."""
