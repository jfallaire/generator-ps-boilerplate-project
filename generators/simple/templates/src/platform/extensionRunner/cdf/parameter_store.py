"""
    - THIS FILE IS GENERATED -

dependencies/CMF.Net/Cmf/ParameterStore/ParameterStore.jid

"""

from attr import attrs
from typing import List, Optional as Opt
from .root import CoveoInterface, JidType, api


@attrs(kw_only=True, auto_attribs=True)
class Credential(JidType, hint="Coveo.Credential"):
    user: Opt[str] = None
    password: Opt[str] = None

    def __init__(self, *, user: Opt[str] = None, password: Opt[str] = None) -> None:
        ...


class IParameterStore(CoveoInterface):
    """The CredentialsManager interface"""

    @api("GET/parameter")
    def get_parameter(self, *, name: str) -> str:
        """

        Parameters:
            name: Name of the parameter to get
        """

    @api("GET/parameters")
    def get_parameters(self, *, names: List[str]) -> List[str]:
        """

        Parameters:
            names: Name of the parameters to get
        """
