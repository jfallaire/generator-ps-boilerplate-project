"""
    - THIS FILE IS GENERATED -

dependencies/CMF.Net/Cmf/FeatureFlagService/FeatureFlagService.jid

"""

from typing import Dict
from .root import CoveoInterface, api


class IFeatureFlags(CoveoInterface):
    """The FeatureFlags interface"""

    @api("GET/bool_flag")
    def get_bool_flag(self, *, name: str, component: str, tags: Dict[str, str]) -> bool:
        """

        Parameters:
            name: Name of the flag to get. Ex: 'dpm-perform-ipp'.
            component: Name of the component asking for the flag. Ex: 'dpm'.
            tags: Additional <tag,value> pairs. Ex: <'license', 'trial'>.
        """
