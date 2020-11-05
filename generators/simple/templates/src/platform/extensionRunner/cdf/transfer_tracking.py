"""
    - THIS FILE IS GENERATED -

dependencies/CDF/Cpp/BladeSyncher/TransferTracking.jid

"""

from attr import attrs
from enum import auto
from typing import Optional as Opt
from .root import JidEnumFlag
from .tracking import StatusEntry


@attrs(kw_only=True, auto_attribs=True)
class FileTransferStatus(StatusEntry, hint="Coveo.TransferTracking.FileTransferStatus"):
    """File transfer status entry.

    Attributes:
        current_file_name: The name of the file that is currently being transferred.
        current_file_number: The number of file that is currently being transferred.
        total_number_of_files: The total number of files to transfer.
        transferred_size: The amount of data that has been transferred.
        total_size: The total amount of data to transfer.
    """

    current_file_name: Opt[str] = None
    current_file_number: Opt[int] = None
    total_number_of_files: Opt[int] = None
    transferred_size: Opt[int] = None
    total_size: Opt[int] = None

    def __init__(
        self,
        *,
        current_file_name: Opt[str] = None,
        current_file_number: Opt[int] = None,
        total_number_of_files: Opt[int] = None,
        transferred_size: Opt[int] = None,
        total_size: Opt[int] = None,
    ) -> None:
        """

        Parameters:
            current_file_name: The name of the file that is currently being transferred.
            current_file_number: The number of file that is currently being transferred.
            total_number_of_files: The total number of files to transfer.
            transferred_size: The amount of data that has been transferred.
            total_size: The total amount of data to transfer.
        """


@attrs(kw_only=True, auto_attribs=True)
class SynchronizationStatus(FileTransferStatus, hint="Coveo.TransferTracking.SynchronizationStatus"):
    """Synchronization status entry.

    Attributes:
        current_sync_token: The token representing the current synchronization operation.
    """

    current_sync_token: Opt[str] = None

    def __init__(self, *, current_sync_token: Opt[str] = None) -> None:
        """

        Parameters:
            current_sync_token: The token representing the current synchronization operation.
        """


class BackupOperation(JidEnumFlag):
    """Type of operation being executed."""

    Backup: int = auto()
    Restore: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class BackupStatus(FileTransferStatus, hint="Coveo.TransferTracking.BackupStatus"):
    """Backup status entry.

    Attributes:
        operation: Operation that is currently being executed.
    """

    operation: Opt[BackupOperation] = None

    def __init__(self, *, operation: Opt[BackupOperation] = None) -> None:
        """

        Parameters:
            operation: Operation that is currently being executed.
        """
