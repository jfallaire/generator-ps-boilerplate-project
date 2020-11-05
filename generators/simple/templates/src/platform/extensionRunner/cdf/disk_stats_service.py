"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/DiskStatsService.jid

"""

from attr import attrib, attrs
from typing import Optional as Opt
from .root import CASING, CoveoInterface, JidType, api


@attrs(kw_only=True, auto_attribs=True)
class DiskSpaceStats(JidType, hint="Coveo.DiskSpaceStats"):
    remaining_bytes: Opt[int] = attrib(default=None, metadata={CASING: "remaining_bytes"})
    total_bytes: Opt[int] = attrib(default=None, metadata={CASING: "total_bytes"})

    def __init__(
        self,
        *,
        remaining_bytes: Opt[int] = attrib(default=None, metadata={CASING: "remaining_bytes"}),
        total_bytes: Opt[int] = attrib(default=None, metadata={CASING: "total_bytes"}),
    ) -> None:
        ...


class IDiskStatsService(CoveoInterface):
    """Interface used to retrieve disk space statistics"""

    @api("GET/disk_space_stats")
    def get_disk_space_stats(self) -> DiskSpaceStats:
        """Get the disk space statistics."""

    @api("GET/maximum_throughput", throughput_bytes="throughput_bytes")
    def get_maximum_throughput(self, *, throughput_bytes: int) -> None:
        """Get the maximum throughput.

        Parameters:
            throughput_bytes: The maximum throughput in bytes.
        """
