"""CDF exceptions found in responses are wrapped into this object base."""

import attr

from .jid_type import ExceptionBase


# required alias.
@attr.s(auto_attribs=True, kw_only=True)
class QuitException(ExceptionBase, hint='QuitException'):
    """QuitException"""
