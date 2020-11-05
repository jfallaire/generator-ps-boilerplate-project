"""
    - THIS FILE IS GENERATED -

dependencies/CDF/Cpp/BladeSyncher/CDFBladeSnapshot.jid

"""

from typing import List
from .root import CoveoInterface, api


class IBladeSnapshot(CoveoInterface):
    @api("GET/snapshots?prefix={prefix}", prefix="prefix")
    def get_snapshots(self, *, prefix: str) -> List[str]:
        """List snapshots matching the specified prefix.

        Parameters:
            prefix: The required prefix for snapshots.
        """

    @api("POST/snapshots/{snapshot_id}?directory={directory}", snapshot_id="snapshot_id", directory="directory")
    def create_snapshot(self, *, snapshot_id: str, directory: str) -> None:
        """Create a snapshot for a particular directory.

        Parameters:
            snapshot_id: The id to give to the snapshot.
            directory: If unspecified, will be assumed to be the node agent directory.
        """

    @api("DELETE/snapshots/{snapshot_id}", snapshot_id="snapshot_id")
    def delete_snapshot(self, *, snapshot_id: str) -> None:
        """Delete the specified snapshot. Idempotent operation, will do nothing if the snapshot does not exist.

        Parameters:
            snapshot_id: The id of the snapshot to delete.
        """
