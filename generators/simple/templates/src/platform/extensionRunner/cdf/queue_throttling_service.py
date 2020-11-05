"""
    - THIS FILE IS GENERATED -

dependencies/CMF.Net/Cmf/QueueThrottling/QueueThrottlingService.jid

"""

from attr import attrib, attrs
from enum import auto
from typing import Optional as Opt
from .root import CASING, CoveoInterface, JidEnumFlag, JidType, api


class QueueType(JidEnumFlag):
    rabbitmq: int = auto()
    sqs: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class Queue(JidType, hint="Coveo.QueueThrottlingService.Queue"):
    """

    Attributes:
        name: The name of the queue to work
        duration: How long to consume from the queue
        server_uri: Where the queue is locate
        use_message_routing_service: Whether to use the queue service with queues from the same org
        type_: The queue type
    """

    name: Opt[str] = attrib(default=None, metadata={CASING: "name"})
    duration: Opt[int] = attrib(default=None, metadata={CASING: "duration"})
    server_uri: Opt[str] = attrib(default=None, metadata={CASING: "server_uri"})
    use_message_routing_service: Opt[bool] = attrib(default=None, metadata={CASING: "use_message_routing_service"})
    type_: Opt[QueueType] = attrib(default=None, metadata={CASING: "type"})

    def __init__(
        self,
        *,
        name: Opt[str] = attrib(default=None, metadata={CASING: "name"}),
        duration: Opt[int] = attrib(default=None, metadata={CASING: "duration"}),
        server_uri: Opt[str] = attrib(default=None, metadata={CASING: "server_uri"}),
        use_message_routing_service: Opt[bool] = attrib(default=None, metadata={CASING: "use_message_routing_service"}),
        type_: Opt[QueueType] = attrib(default=None, metadata={CASING: "type"}),
    ) -> None:
        """

        Parameters:
            name: The name of the queue to work
            duration: How long to consume from the queue
            server_uri: Where the queue is locate
            use_message_routing_service: Whether to use the queue service with queues from the same org
            type_: The queue type
        """


class IQueueThrottling(CoveoInterface):
    @api("GET/random_queue/{vhost}/{type}", vhost="vhost", type_="Type")
    def get_random_queue(self, *, vhost: str, type_: str) -> Queue:
        """Return a random non empty DPM queue that is not being throttled.

        Parameters:
            vhost: The name of a virtual host.
            type_: The type of random queue to get, ex: dpm
        """
