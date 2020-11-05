"""
    - THIS FILE IS GENERATED -

dependencies/CDF/Cpp/BladeSyncher/CDFBladeBackup.jid

"""

from attr import attrs
from typing import Dict
from .root import CoveoInterface, ExceptionBase, api


@attrs(kw_only=True, auto_attribs=True)
class BladeBackupException(ExceptionBase, hint="CDF.BladeBackupException"):
    """Base exception for all BladeBackup exceptions."""

    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class BackupFailedException(BladeBackupException, hint="CDF.BackupFailedException"):
    """The backup operation has failed."""

    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class RestoreFailedException(BladeBackupException, hint="CDF.RestoreFailedException"):
    """The restore operation has failed."""

    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class OperationCanceledException(BladeBackupException, hint="CDF.OperationCanceledException"):
    """The operation was canceled before completing."""

    def __init__(self) -> None:
        ...


class IBladeBackup(CoveoInterface):
    """The BladeBackup interface."""

    @api("POST/backup")
    def backup(self, *, backup_id: str, params: Dict[str, str]) -> None:
        """Backup the contents of a blade.

        Parameters:
            backup_id: A unique ID identifying this backup.
            params: Additional parameters. Implementation Dependent.
        """

    @api("POST/restore")
    def restore(self, *, backup_id: str, params: Dict[str, str]) -> None:
        """Restore the contents of a blade.

        Parameters:
            backup_id: The unique ID identifying the backup to restore.
            params: Additional parameters. Implementation Dependent.
        """

    @api("POST/cancel")
    def cancel_operation(self) -> None:
        """Cancel current operation."""
