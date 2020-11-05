"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/ScriptStore.jid

"""

from attr import attrs
from typing import Optional as Opt
from .root import CoveoInterface, ExceptionBase, JidType, api


@attrs(kw_only=True, auto_attribs=True)
class ScriptStoreException(ExceptionBase, hint="Coveo.ScriptStoreException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ScriptNotFoundException(ScriptStoreException, hint="Coveo.ScriptNotFoundException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class InvalidVersionException(ScriptStoreException, hint="Coveo.InvalidVersionException"):
    def __init__(self) -> None:
        ...


class IScriptStore(CoveoInterface):
    """The script store API exposes methods to interact with this script store."""

    @api("GET/scripts/{id}/{version}", id_="Id")
    def get(self, *, id_: str, version: str) -> str:
        """Returns a script from the store.

        Parameters:
            id_: The script id.
            version: The script version.
        """

    @api("GET/enabled/{id}", id_="Id")
    def is_enabled(self, *, id_: str) -> bool:
        """Returns whether a script is enabled.

        Parameters:
            id_: The script id.
        """

    @api("GET/last_version_id/{id}", id_="Id")
    def get_last_version_id(self, *, id_: str) -> str:
        """Returns the id of the last version of a script.

        Parameters:
            id_: The script id.
        """


@attrs(kw_only=True, auto_attribs=True)
class ScriptPackage(JidType, hint="Coveo.ScriptPackage"):
    """

    Attributes:
        name: The package name
        location: The package location
        version: The package version
    """

    name: Opt[str] = None
    location: Opt[str] = None
    version: Opt[str] = None

    def __init__(self, *, name: Opt[str] = None, location: Opt[str] = None, version: Opt[str] = None) -> None:
        """

        Parameters:
            name: The package name
            location: The package location
            version: The package version
        """
