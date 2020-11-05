"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/Prometheus.jid

"""

from .root import CoveoInterface, api


class IPrometheus(CoveoInterface):
    """The Prometheus interface"""

    @api("GET/metrics")
    def generate_metrics(self) -> str:
        """Returns the metrics"""
