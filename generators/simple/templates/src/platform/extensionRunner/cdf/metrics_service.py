"""
    - THIS FILE IS GENERATED -

CoveoServices/MetricsService/CoveoMetricsService.jid

"""

from attr import attrs
from typing import Optional as Opt
from .tracking import MetricEntry


@attrs(kw_only=True, auto_attribs=True)
class QueryMetric(MetricEntry, hint="Coveo.MetricsService.QueryMetric"):
    """A structure that represents a query metric."""

    mirror: Opt[str] = None
    user: Opt[str] = None
    query: Opt[str] = None
    nb_results: Opt[int] = None
    duration: Opt[float] = None

    def __init__(
        self,
        *,
        mirror: Opt[str] = None,
        user: Opt[str] = None,
        query: Opt[str] = None,
        nb_results: Opt[int] = None,
        duration: Opt[float] = None,
    ) -> None:
        ...
