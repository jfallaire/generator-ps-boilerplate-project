"""

    -- this whole module is NOT generated! --

                                                """

from typing import Set

from corepyutils.casing import flexcase

# the imports below are here to simplify the generated code and let us move things around in a transparent manner.
from .enum import JidEnumFlag
from .exception import QuitException, ExceptionBase
from .interface import CoveoInterface, api, MultiOut
from .jid_type import ExceptionBase
from .jid_type import JidType, CASING


def get_dependencies() -> Set[str]:
    """Returns the list of dependencies from the root module to include in generated modules."""
    deps = {cls.__name__ for cls in (CoveoInterface, api, JidType, flexcase,  # type: ignore
                                     ExceptionBase, QuitException, ExceptionBase, JidEnumFlag)}
    # refactor guards... these shouldn't be renamed/etc.
    assert 'CASING' in globals()
    assert CASING == 'CASING'
    assert 'MultiOut' in globals()
    deps.add(CASING)
    deps.add('MultiOut')
    return deps


# QuitException is missing so we'll invent the
ROOT_JID = """
{Type:Database, Deltas:[
    {Type:Delta, Changes:[
        {Type:Module, Name:cdf.root, Children:[
            {Type:Namespace, Name:root, Children:[
                {Type:Exception, Name:CDFException},
                {Type:Exception, Name:QuitException, Ancestor:CDFException}
            ]}
        ]}
    ]}
]}
"""
