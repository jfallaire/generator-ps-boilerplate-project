"""
    - THIS FILE IS GENERATED -

dependencies/CMF.Net/Cmf/MessageRouting/MessageRoutingService.jid

"""

from attr import attrs
from typing import Optional as Opt, Union
from .root import CoveoInterface, JidType, api


@attrs(kw_only=True, auto_attribs=True)
class Message(JidType, hint="Coveo.MessageRoutingService.Message"):
    """

    Attributes:
        stream_name: The stream name
        payload: The payload
    """

    stream_name: Opt[str] = None
    payload: Opt[Union[str, bytes]] = None

    def __init__(self, *, stream_name: Opt[str] = None, payload: Opt[Union[str, bytes]] = None) -> None:
        """

        Parameters:
            stream_name: The stream name
            payload: The payload
        """


class IMessageRouter(CoveoInterface):
    @api("POST/streams/{stream_name}/publish,in:*")
    def send_message(self, *, message: Message) -> None:
        ...
