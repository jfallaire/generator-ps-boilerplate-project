"""
    - THIS FILE IS GENERATED -

dependencies/CMF.Net/Cmf/QueueRabbit/CoveoQueueRabbitAdminService.jid

"""

from attr import attrib, attrs
from datetime import datetime
from enum import auto
from typing import Any, Dict, List, Optional as Opt
from .root import CASING, CoveoInterface, JidEnumFlag, JidType, api


@attrs(kw_only=True, auto_attribs=True)
class ExchangeType(JidType, hint="Coveo.QueueRabbitAdmin.ExchangeType"):
    """A structure that represents an exchange type.

    Attributes:
        name: The exchange type's name. Used as Id.
        description: The description of the exchange.
        enabled: Indicates if the exchange type is enabled.
    """

    name: Opt[str] = attrib(default=None, metadata={CASING: "name"})
    description: Opt[str] = attrib(default=None, metadata={CASING: "description"})
    enabled: Opt[bool] = attrib(default=None, metadata={CASING: "enabled"})

    def __init__(
        self,
        *,
        name: Opt[str] = attrib(default=None, metadata={CASING: "name"}),
        description: Opt[str] = attrib(default=None, metadata={CASING: "description"}),
        enabled: Opt[bool] = attrib(default=None, metadata={CASING: "enabled"}),
    ) -> None:
        """

        Parameters:
            name: The exchange type's name. Used as Id.
            description: The description of the exchange.
            enabled: Indicates if the exchange type is enabled.
        """


class NodeType(JidEnumFlag):
    """Defines the various types of node."""

    ram: int = auto()
    disc: int = auto()


class DestinationType(JidEnumFlag):
    """Defines the destinations available to a binding."""

    queue: int = auto()
    exchange: int = auto()


class StatisticsLevel(JidEnumFlag):
    """Defines the granularity of statistics events.

    Attributes:
        none: Do not emit statistics events.
        coarse: Emit per-queue / per-channel / per-connection statistics events.
        fine: Also emit per-message statistics events.
    """

    none: int = auto()
    coarse: int = auto()
    fine: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class MessagesDetails(JidType, hint="Coveo.QueueRabbitAdmin.MessagesDetails"):
    """A structure that contains a snapshot of the current message activity.

    Attributes:
        rate: Indicates the amount of messages since the last 'Interval' passed.
        interval: The interval used to calculate the 'Rate'.
        last_event: The time elapsed since the last message.
    """

    rate: Opt[float] = attrib(default=None, metadata={CASING: "rate"})
    interval: Opt[int] = attrib(default=None, metadata={CASING: "interval"})
    last_event: Opt[int] = attrib(default=None, metadata={CASING: "last_event"})

    def __init__(
        self,
        *,
        rate: Opt[float] = attrib(default=None, metadata={CASING: "rate"}),
        interval: Opt[int] = attrib(default=None, metadata={CASING: "interval"}),
        last_event: Opt[int] = attrib(default=None, metadata={CASING: "last_event"}),
    ) -> None:
        """

        Parameters:
            rate: Indicates the amount of messages since the last 'Interval' passed.
            interval: The interval used to calculate the 'Rate'.
            last_event: The time elapsed since the last message.
        """


@attrs(kw_only=True, auto_attribs=True)
class MessageStats(JidType, hint="Coveo.QueueRabbitAdmin.MessageStats"):
    """A structure that contains statistics about message activity."""

    ack: Opt[int] = attrib(default=None, metadata={CASING: "ack"})
    ack_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "ack_details"})
    confirm: Opt[int] = attrib(default=None, metadata={CASING: "confirm"})
    confirm_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "confirm_details"})
    deliver: Opt[int] = attrib(default=None, metadata={CASING: "deliver"})
    deliver_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "deliver_details"})
    deliver_get: Opt[int] = attrib(default=None, metadata={CASING: "deliver_get"})
    deliver_get_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "deliver_get_details"})
    deliver_no_ack: Opt[int] = attrib(default=None, metadata={CASING: "deliver_no_ack"})
    deliver_no_ack_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "deliver_no_ack_details"})
    get: Opt[int] = None
    get_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "get_details"})
    get_no_ack: Opt[int] = attrib(default=None, metadata={CASING: "get_no_ack"})
    get_no_ack_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "get_no_ack_details"})
    publish: Opt[int] = attrib(default=None, metadata={CASING: "publish"})
    publish_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "publish_details"})
    publish_in: Opt[int] = attrib(default=None, metadata={CASING: "publish_in"})
    publish_in_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "publish_in_details"})
    publish_out: Opt[int] = attrib(default=None, metadata={CASING: "publish_out"})
    publish_out_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "publish_out_details"})
    redeliver: Opt[int] = attrib(default=None, metadata={CASING: "redeliver"})
    redeliver_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "redeliverDetails"})
    return_unroutable: Opt[int] = attrib(default=None, metadata={CASING: "return_unroutable"})
    return_unroutable_details: Opt[MessagesDetails] = attrib(
        default=None, metadata={CASING: "return_unroutable_details"}
    )

    def __init__(
        self,
        *,
        ack: Opt[int] = attrib(default=None, metadata={CASING: "ack"}),
        ack_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "ack_details"}),
        confirm: Opt[int] = attrib(default=None, metadata={CASING: "confirm"}),
        confirm_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "confirm_details"}),
        deliver: Opt[int] = attrib(default=None, metadata={CASING: "deliver"}),
        deliver_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "deliver_details"}),
        deliver_get: Opt[int] = attrib(default=None, metadata={CASING: "deliver_get"}),
        deliver_get_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "deliver_get_details"}),
        deliver_no_ack: Opt[int] = attrib(default=None, metadata={CASING: "deliver_no_ack"}),
        deliver_no_ack_details: Opt[MessagesDetails] = attrib(
            default=None, metadata={CASING: "deliver_no_ack_details"}
        ),
        get: Opt[int] = None,
        get_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "get_details"}),
        get_no_ack: Opt[int] = attrib(default=None, metadata={CASING: "get_no_ack"}),
        get_no_ack_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "get_no_ack_details"}),
        publish: Opt[int] = attrib(default=None, metadata={CASING: "publish"}),
        publish_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "publish_details"}),
        publish_in: Opt[int] = attrib(default=None, metadata={CASING: "publish_in"}),
        publish_in_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "publish_in_details"}),
        publish_out: Opt[int] = attrib(default=None, metadata={CASING: "publish_out"}),
        publish_out_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "publish_out_details"}),
        redeliver: Opt[int] = attrib(default=None, metadata={CASING: "redeliver"}),
        redeliver_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "redeliverDetails"}),
        return_unroutable: Opt[int] = attrib(default=None, metadata={CASING: "return_unroutable"}),
        return_unroutable_details: Opt[MessagesDetails] = attrib(
            default=None, metadata={CASING: "return_unroutable_details"}
        ),
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class Listener(JidType, hint="Coveo.QueueRabbitAdmin.Listener"):
    """A structure that contains information about a listener.

    Attributes:
        node: The name of the node being listened.
        protocol: The name of the protocol used.
        ip_address: The IP address of the listener.
        port: The port of the listener.
    """

    node: Opt[str] = attrib(default=None, metadata={CASING: "node"})
    protocol: Opt[str] = attrib(default=None, metadata={CASING: "protocol"})
    ip_address: Opt[str] = attrib(default=None, metadata={CASING: "ip_address"})
    port: Opt[int] = attrib(default=None, metadata={CASING: "port"})

    def __init__(
        self,
        *,
        node: Opt[str] = attrib(default=None, metadata={CASING: "node"}),
        protocol: Opt[str] = attrib(default=None, metadata={CASING: "protocol"}),
        ip_address: Opt[str] = attrib(default=None, metadata={CASING: "ip_address"}),
        port: Opt[int] = attrib(default=None, metadata={CASING: "port"}),
    ) -> None:
        """

        Parameters:
            node: The name of the node being listened.
            protocol: The name of the protocol used.
            ip_address: The IP address of the listener.
            port: The port of the listener.
        """


@attrs(kw_only=True, auto_attribs=True)
class Context(JidType, hint="Coveo.QueueRabbitAdmin.Context"):
    node: Opt[str] = attrib(default=None, metadata={CASING: "node"})
    description: Opt[str] = attrib(default=None, metadata={CASING: "description"})
    path: Opt[str] = attrib(default=None, metadata={CASING: "path"})
    port: Opt[int] = attrib(default=None, metadata={CASING: "port"})
    ignore_in_use: Opt[bool] = attrib(default=None, metadata={CASING: "ignore_in_use"})

    def __init__(
        self,
        *,
        node: Opt[str] = attrib(default=None, metadata={CASING: "node"}),
        description: Opt[str] = attrib(default=None, metadata={CASING: "description"}),
        path: Opt[str] = attrib(default=None, metadata={CASING: "path"}),
        port: Opt[int] = attrib(default=None, metadata={CASING: "port"}),
        ignore_in_use: Opt[bool] = attrib(default=None, metadata={CASING: "ignore_in_use"}),
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class AuthMechanism(JidType, hint="Coveo.QueueRabbitAdmin.AuthMechanism"):
    """A structure that contains information about an authentication mechanism.

    Attributes:
        name: The name of the authentication mechanism to use. Built-in mechanisms are PLAIN, AMQPLAIN and RABBIT-CR-DEMO. EXTERNAL is also available and defines a mechanism that is implemented by a plugin. See http://www.rabbitmq.com/authentication.html
    """

    name: Opt[str] = attrib(default=None, metadata={CASING: "name"})
    description: Opt[str] = attrib(default=None, metadata={CASING: "description"})
    enabled: Opt[bool] = attrib(default=None, metadata={CASING: "enabled"})

    def __init__(
        self,
        *,
        name: Opt[str] = attrib(default=None, metadata={CASING: "name"}),
        description: Opt[str] = attrib(default=None, metadata={CASING: "description"}),
        enabled: Opt[bool] = attrib(default=None, metadata={CASING: "enabled"}),
    ) -> None:
        """

        Parameters:
            name: The name of the authentication mechanism to use. Built-in mechanisms are PLAIN, AMQPLAIN and RABBIT-CR-DEMO. EXTERNAL is also available and defines a mechanism that is implemented by a plugin. See http://www.rabbitmq.com/authentication.html
        """


@attrs(kw_only=True, auto_attribs=True)
class Application(JidType, hint="Coveo.QueueRabbitAdmin.Application"):
    name: Opt[str] = attrib(default=None, metadata={CASING: "name"})
    description: Opt[str] = attrib(default=None, metadata={CASING: "description"})
    version: Opt[str] = attrib(default=None, metadata={CASING: "version"})

    def __init__(
        self,
        *,
        name: Opt[str] = attrib(default=None, metadata={CASING: "name"}),
        description: Opt[str] = attrib(default=None, metadata={CASING: "description"}),
        version: Opt[str] = attrib(default=None, metadata={CASING: "version"}),
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class QueueTotals(JidType, hint="Coveo.QueueRabbitAdmin.QueueTotals"):
    """A structure that contains statistics about the state of queued messages."""

    messages: Opt[int] = attrib(default=None, metadata={CASING: "messages"})
    messages_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "messages_details"})
    messages_ready: Opt[int] = attrib(default=None, metadata={CASING: "messages_ready"})
    messages_ready_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "messages_ready_details"})
    messages_unacknowledged: Opt[int] = attrib(default=None, metadata={CASING: "messages_unacknowledged"})
    messages_unacknowledged_details: Opt[MessagesDetails] = attrib(
        default=None, metadata={CASING: "messages_unacknowledged_details"}
    )

    def __init__(
        self,
        *,
        messages: Opt[int] = attrib(default=None, metadata={CASING: "messages"}),
        messages_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "messages_details"}),
        messages_ready: Opt[int] = attrib(default=None, metadata={CASING: "messages_ready"}),
        messages_ready_details: Opt[MessagesDetails] = attrib(
            default=None, metadata={CASING: "messages_ready_details"}
        ),
        messages_unacknowledged: Opt[int] = attrib(default=None, metadata={CASING: "messages_unacknowledged"}),
        messages_unacknowledged_details: Opt[MessagesDetails] = attrib(
            default=None, metadata={CASING: "messages_unacknowledged_details"}
        ),
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ObjectTotals(JidType, hint="Coveo.QueueRabbitAdmin.ObjectTotals"):
    """A structure that contains various high-level totals."""

    consumers: Opt[int] = attrib(default=None, metadata={CASING: "consumers"})
    queues: Opt[int] = attrib(default=None, metadata={CASING: "queues"})
    exchanges: Opt[int] = attrib(default=None, metadata={CASING: "exchanges"})
    connections: Opt[int] = attrib(default=None, metadata={CASING: "connections"})
    channels: Opt[int] = attrib(default=None, metadata={CASING: "channels"})

    def __init__(
        self,
        *,
        consumers: Opt[int] = attrib(default=None, metadata={CASING: "consumers"}),
        queues: Opt[int] = attrib(default=None, metadata={CASING: "queues"}),
        exchanges: Opt[int] = attrib(default=None, metadata={CASING: "exchanges"}),
        connections: Opt[int] = attrib(default=None, metadata={CASING: "connections"}),
        channels: Opt[int] = attrib(default=None, metadata={CASING: "channels"}),
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class Overview(JidType, hint="Coveo.QueueRabbitAdmin.Overview"):
    """A structure that represents a top-down overview of a server, which includes information about its configuration and state as well as statistics about message activity.

    Attributes:
        management_version: The version of the management plugin.
        statistics_level: The granularity of statistics.
        message_stats: Contains statistics about server-wide message activity. Totals are cumulative, much like what can be seen in RabbitMQ's HTML admin.
        queue_totals: Contains a server-wide snapshot of the state of queued messages.
        object_totals: Contains the current total of various RabbitMQ objects.
        node: This node's name.
        statistics_db_node: The name of the statistics database node.
    """

    management_version: Opt[str] = attrib(default=None, metadata={CASING: "management_version"})
    statistics_level: Opt[StatisticsLevel] = attrib(default=None, metadata={CASING: "statistics_level"})
    exchange_types: Opt[List[ExchangeType]] = attrib(default=None, metadata={CASING: "exchange_types"})
    rabbitmq_version: Opt[str] = attrib(default=None, metadata={CASING: "rabbitmq_version"})
    erlang_version: Opt[str] = attrib(default=None, metadata={CASING: "erlang_version"})
    erlang_full_version: Opt[str] = attrib(default=None, metadata={CASING: "erlang_full_version"})
    message_stats: Opt[MessageStats] = attrib(default=None, metadata={CASING: "message_stats"})
    queue_totals: Opt[QueueTotals] = attrib(default=None, metadata={CASING: "queue_totals"})
    object_totals: Opt[ObjectTotals] = attrib(default=None, metadata={CASING: "object_totals"})
    node: Opt[str] = attrib(default=None, metadata={CASING: "node"})
    statistics_db_node: Opt[str] = attrib(default=None, metadata={CASING: "statistics_db_node"})
    listeners: Opt[List[Listener]] = attrib(default=None, metadata={CASING: "listeners"})
    contexts: Opt[List[Context]] = attrib(default=None, metadata={CASING: "contexts"})

    def __init__(
        self,
        *,
        management_version: Opt[str] = attrib(default=None, metadata={CASING: "management_version"}),
        statistics_level: Opt[StatisticsLevel] = attrib(default=None, metadata={CASING: "statistics_level"}),
        exchange_types: Opt[List[ExchangeType]] = attrib(default=None, metadata={CASING: "exchange_types"}),
        rabbitmq_version: Opt[str] = attrib(default=None, metadata={CASING: "rabbitmq_version"}),
        erlang_version: Opt[str] = attrib(default=None, metadata={CASING: "erlang_version"}),
        erlang_full_version: Opt[str] = attrib(default=None, metadata={CASING: "erlang_full_version"}),
        message_stats: Opt[MessageStats] = attrib(default=None, metadata={CASING: "message_stats"}),
        queue_totals: Opt[QueueTotals] = attrib(default=None, metadata={CASING: "queue_totals"}),
        object_totals: Opt[ObjectTotals] = attrib(default=None, metadata={CASING: "object_totals"}),
        node: Opt[str] = attrib(default=None, metadata={CASING: "node"}),
        statistics_db_node: Opt[str] = attrib(default=None, metadata={CASING: "statistics_db_node"}),
        listeners: Opt[List[Listener]] = attrib(default=None, metadata={CASING: "listeners"}),
        contexts: Opt[List[Context]] = attrib(default=None, metadata={CASING: "contexts"}),
    ) -> None:
        """

        Parameters:
            management_version: The version of the management plugin.
            statistics_level: The granularity of statistics.
            message_stats: Contains statistics about server-wide message activity. Totals are cumulative, much like what can be seen in RabbitMQ's HTML admin.
            queue_totals: Contains a server-wide snapshot of the state of queued messages.
            object_totals: Contains the current total of various RabbitMQ objects.
            node: This node's name.
            statistics_db_node: The name of the statistics database node.
        """


@attrs(kw_only=True, auto_attribs=True)
class Partition(JidType, hint="Coveo.QueueRabbitAdmin.Partition"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class Node(JidType, hint="Coveo.QueueRabbitAdmin.Node"):
    """A structure that contains information about a node.

    Attributes:
        name: The name of the node. Used as Id.
    """

    name: Opt[str] = attrib(default=None, metadata={CASING: "name"})
    type_: Opt[NodeType] = attrib(default=None, metadata={CASING: "type"})
    running: Opt[bool] = attrib(default=None, metadata={CASING: "running"})
    os_pid: Opt[int] = attrib(default=None, metadata={CASING: "os_pid"})
    mem_ets: Opt[int] = attrib(default=None, metadata={CASING: "mem_ets"})
    mem_binary: Opt[int] = attrib(default=None, metadata={CASING: "mem_binary"})
    mem_proc: Opt[int] = attrib(default=None, metadata={CASING: "mem_proc"})
    mem_proc_used: Opt[int] = attrib(default=None, metadata={CASING: "mem_procUsed"})
    mem_atom: Opt[int] = attrib(default=None, metadata={CASING: "mem_atom"})
    mem_atom_used: Opt[int] = attrib(default=None, metadata={CASING: "mem_atomUsed"})
    mem_code: Opt[int] = attrib(default=None, metadata={CASING: "mem_code"})
    fd_used: Opt[str] = attrib(default=None, metadata={CASING: "fd_used"})
    fd_total: Opt[int] = attrib(default=None, metadata={CASING: "fd_total"})
    sockets_used: Opt[int] = attrib(default=None, metadata={CASING: "sockets_used"})
    sockets_total: Opt[int] = attrib(default=None, metadata={CASING: "sockets_total"})
    mem_used: Opt[int] = attrib(default=None, metadata={CASING: "mem_used"})
    mem_limit: Opt[int] = attrib(default=None, metadata={CASING: "mem_limit"})
    mem_alarm: Opt[bool] = attrib(default=None, metadata={CASING: "mem_alarm"})
    disk_free_limit: Opt[int] = attrib(default=None, metadata={CASING: "disk_free_limit"})
    disk_free: Opt[int] = attrib(default=None, metadata={CASING: "disk_free"})
    disk_free_alarm: Opt[bool] = attrib(default=None, metadata={CASING: "disk_free_alarm"})
    proc_used: Opt[int] = attrib(default=None, metadata={CASING: "proc_used"})
    proc_total: Opt[int] = attrib(default=None, metadata={CASING: "proc_total"})
    statistics_level: Opt[StatisticsLevel] = attrib(default=None, metadata={CASING: "statistics_level"})
    erlang_version: Opt[str] = attrib(default=None, metadata={CASING: "erlang_version"})
    uptime: Opt[int] = attrib(default=None, metadata={CASING: "uptime"})
    run_queue: Opt[int] = attrib(default=None, metadata={CASING: "run_queue"})
    processors: Opt[int] = attrib(default=None, metadata={CASING: "processors"})
    partitions: Opt[List[Partition]] = attrib(default=None, metadata={CASING: "partitions"})
    exchange_types: Opt[List[ExchangeType]] = attrib(default=None, metadata={CASING: "exchange_types"})
    auth_mechanisms: Opt[List[AuthMechanism]] = attrib(default=None, metadata={CASING: "auth_mechanisms"})
    applications: Opt[List[Application]] = attrib(default=None, metadata={CASING: "applications"})
    contexts: Opt[List[Context]] = attrib(default=None, metadata={CASING: "contexts"})
    external_stats_not_running: Opt[bool] = attrib(default=None, metadata={CASING: "external_stats_not_running"})

    def __init__(
        self,
        *,
        name: Opt[str] = attrib(default=None, metadata={CASING: "name"}),
        type_: Opt[NodeType] = attrib(default=None, metadata={CASING: "type"}),
        running: Opt[bool] = attrib(default=None, metadata={CASING: "running"}),
        os_pid: Opt[int] = attrib(default=None, metadata={CASING: "os_pid"}),
        mem_ets: Opt[int] = attrib(default=None, metadata={CASING: "mem_ets"}),
        mem_binary: Opt[int] = attrib(default=None, metadata={CASING: "mem_binary"}),
        mem_proc: Opt[int] = attrib(default=None, metadata={CASING: "mem_proc"}),
        mem_proc_used: Opt[int] = attrib(default=None, metadata={CASING: "mem_procUsed"}),
        mem_atom: Opt[int] = attrib(default=None, metadata={CASING: "mem_atom"}),
        mem_atom_used: Opt[int] = attrib(default=None, metadata={CASING: "mem_atomUsed"}),
        mem_code: Opt[int] = attrib(default=None, metadata={CASING: "mem_code"}),
        fd_used: Opt[str] = attrib(default=None, metadata={CASING: "fd_used"}),
        fd_total: Opt[int] = attrib(default=None, metadata={CASING: "fd_total"}),
        sockets_used: Opt[int] = attrib(default=None, metadata={CASING: "sockets_used"}),
        sockets_total: Opt[int] = attrib(default=None, metadata={CASING: "sockets_total"}),
        mem_used: Opt[int] = attrib(default=None, metadata={CASING: "mem_used"}),
        mem_limit: Opt[int] = attrib(default=None, metadata={CASING: "mem_limit"}),
        mem_alarm: Opt[bool] = attrib(default=None, metadata={CASING: "mem_alarm"}),
        disk_free_limit: Opt[int] = attrib(default=None, metadata={CASING: "disk_free_limit"}),
        disk_free: Opt[int] = attrib(default=None, metadata={CASING: "disk_free"}),
        disk_free_alarm: Opt[bool] = attrib(default=None, metadata={CASING: "disk_free_alarm"}),
        proc_used: Opt[int] = attrib(default=None, metadata={CASING: "proc_used"}),
        proc_total: Opt[int] = attrib(default=None, metadata={CASING: "proc_total"}),
        statistics_level: Opt[StatisticsLevel] = attrib(default=None, metadata={CASING: "statistics_level"}),
        erlang_version: Opt[str] = attrib(default=None, metadata={CASING: "erlang_version"}),
        uptime: Opt[int] = attrib(default=None, metadata={CASING: "uptime"}),
        run_queue: Opt[int] = attrib(default=None, metadata={CASING: "run_queue"}),
        processors: Opt[int] = attrib(default=None, metadata={CASING: "processors"}),
        partitions: Opt[List[Partition]] = attrib(default=None, metadata={CASING: "partitions"}),
        exchange_types: Opt[List[ExchangeType]] = attrib(default=None, metadata={CASING: "exchange_types"}),
        auth_mechanisms: Opt[List[AuthMechanism]] = attrib(default=None, metadata={CASING: "auth_mechanisms"}),
        applications: Opt[List[Application]] = attrib(default=None, metadata={CASING: "applications"}),
        contexts: Opt[List[Context]] = attrib(default=None, metadata={CASING: "contexts"}),
        external_stats_not_running: Opt[bool] = attrib(default=None, metadata={CASING: "external_stats_not_running"}),
    ) -> None:
        """

        Parameters:
            name: The name of the node. Used as Id.
        """


@attrs(kw_only=True, auto_attribs=True)
class Permission(JidType, hint="Coveo.QueueRabbitAdmin.Permission"):
    """A structure that represents a user permission. See http://www.rabbitmq.com/access-control.html for detailed information.

    Attributes:
        vhost: The name of the virtual host.
        user: The name of the user.
        configure: A regex used to identify queues and exchanges that can be configured by the user.
        write: A regex used to identify queues and exchanges that the user is allowed to inject messages into.
        read: A regex used to identify queues and exchanges that can be read (i.e.: message get) by the user.
    """

    vhost: Opt[str] = attrib(default=None, metadata={CASING: "vhost"})
    user: Opt[str] = attrib(default=None, metadata={CASING: "user"})
    configure: Opt[str] = attrib(default=None, metadata={CASING: "configure"})
    write: Opt[str] = attrib(default=None, metadata={CASING: "write"})
    read: Opt[str] = attrib(default=None, metadata={CASING: "read"})

    def __init__(
        self,
        *,
        vhost: Opt[str] = attrib(default=None, metadata={CASING: "vhost"}),
        user: Opt[str] = attrib(default=None, metadata={CASING: "user"}),
        configure: Opt[str] = attrib(default=None, metadata={CASING: "configure"}),
        write: Opt[str] = attrib(default=None, metadata={CASING: "write"}),
        read: Opt[str] = attrib(default=None, metadata={CASING: "read"}),
    ) -> None:
        """

        Parameters:
            vhost: The name of the virtual host.
            user: The name of the user.
            configure: A regex used to identify queues and exchanges that can be configured by the user.
            write: A regex used to identify queues and exchanges that the user is allowed to inject messages into.
            read: A regex used to identify queues and exchanges that can be read (i.e.: message get) by the user.
        """


@attrs(kw_only=True, auto_attribs=True)
class Capabilities(JidType, hint="Coveo.QueueRabbitAdmin.Capabilities"):
    """A structure that declares the capabilities of a client."""

    publisher_confirms: Opt[bool] = attrib(default=None, metadata={CASING: "publisher_confirms"})
    exchange_exchange_bindings: Opt[bool] = attrib(default=None, metadata={CASING: "exchange_exchange_bindings"})
    consumer_cancel_notify: Opt[bool] = attrib(default=None, metadata={CASING: "consumer_cancel_notify"})
    basic_nack: Opt[bool] = attrib(default=None, metadata={CASING: "basic_nack"})

    def __init__(
        self,
        *,
        publisher_confirms: Opt[bool] = attrib(default=None, metadata={CASING: "publisher_confirms"}),
        exchange_exchange_bindings: Opt[bool] = attrib(default=None, metadata={CASING: "exchange_exchange_bindings"}),
        consumer_cancel_notify: Opt[bool] = attrib(default=None, metadata={CASING: "consumer_cancel_notify"}),
        basic_nack: Opt[bool] = attrib(default=None, metadata={CASING: "basic_nack"}),
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ClientProperties(JidType, hint="Coveo.QueueRabbitAdmin.ClientProperties"):
    """A structure that contains identification information about a client."""

    platform: Opt[str] = attrib(default=None, metadata={CASING: "platform"})
    product: Opt[str] = attrib(default=None, metadata={CASING: "product"})
    capabilities: Opt[Capabilities] = attrib(default=None, metadata={CASING: "capabilities"})
    copyright_: Opt[str] = attrib(default=None, metadata={CASING: "copyright"})
    information: Opt[str] = attrib(default=None, metadata={CASING: "information"})
    version: Opt[str] = attrib(default=None, metadata={CASING: "version"})

    def __init__(
        self,
        *,
        platform: Opt[str] = attrib(default=None, metadata={CASING: "platform"}),
        product: Opt[str] = attrib(default=None, metadata={CASING: "product"}),
        capabilities: Opt[Capabilities] = attrib(default=None, metadata={CASING: "capabilities"}),
        copyright_: Opt[str] = attrib(default=None, metadata={CASING: "copyright"}),
        information: Opt[str] = attrib(default=None, metadata={CASING: "information"}),
        version: Opt[str] = attrib(default=None, metadata={CASING: "version"}),
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class Connection(JidType, hint="Coveo.QueueRabbitAdmin.Connection"):
    """A structure that contains information and statistics about an open connection.

    Attributes:
        name: The name of the connection. Used as Id.
    """

    recv_oct: Opt[int] = attrib(default=None, metadata={CASING: "recv_oct"})
    recv_oct_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "recv_oct_details"})
    recv_cnt: Opt[int] = attrib(default=None, metadata={CASING: "recv_cnt"})
    send_oct: Opt[int] = attrib(default=None, metadata={CASING: "send_oct"})
    send_oct_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "send_oct_details"})
    send_cnt: Opt[int] = attrib(default=None, metadata={CASING: "send_cnt"})
    send_pend: Opt[int] = attrib(default=None, metadata={CASING: "send_pend"})
    state: Opt[str] = attrib(default=None, metadata={CASING: "state"})
    last_blocked_by: Opt[str] = attrib(default=None, metadata={CASING: "last_blocked_by"})
    last_blocked_age: Opt[str] = attrib(default=None, metadata={CASING: "last_blocked_age"})
    channels: Opt[int] = attrib(default=None, metadata={CASING: "channels"})
    type_: Opt[str] = attrib(default=None, metadata={CASING: "type"})
    node: Opt[str] = attrib(default=None, metadata={CASING: "node"})
    name: Opt[str] = attrib(default=None, metadata={CASING: "name"})
    host: Opt[str] = attrib(default=None, metadata={CASING: "host"})
    port: Opt[int] = attrib(default=None, metadata={CASING: "port"})
    peer_host: Opt[str] = attrib(default=None, metadata={CASING: "peer_host"})
    peer_port: Opt[int] = attrib(default=None, metadata={CASING: "peer_port"})
    ssl: Opt[bool] = attrib(default=None, metadata={CASING: "ssl"})
    peer_cert_subject: Opt[str] = attrib(default=None, metadata={CASING: "peer_cert_subject"})
    peer_cert_issuer: Opt[str] = attrib(default=None, metadata={CASING: "peer_cert_issuer"})
    peer_cert_validity: Opt[str] = attrib(default=None, metadata={CASING: "peer_cert_validity"})
    auth_mechanism: Opt[str] = attrib(default=None, metadata={CASING: "auth_mechanism"})
    ssl_protocol: Opt[str] = attrib(default=None, metadata={CASING: "ssl_protocol"})
    ssl_key_exchange: Opt[str] = attrib(default=None, metadata={CASING: "ssl_key_exchange"})
    ssl_cipher: Opt[str] = attrib(default=None, metadata={CASING: "ssl_cipher"})
    ssl_hash: Opt[str] = attrib(default=None, metadata={CASING: "ssl_hash"})
    protocol: Opt[str] = attrib(default=None, metadata={CASING: "protocol"})
    user: Opt[str] = attrib(default=None, metadata={CASING: "user"})
    vhost: Opt[str] = attrib(default=None, metadata={CASING: "vhost"})
    timeout: Opt[int] = attrib(default=None, metadata={CASING: "timeout"})
    frame_max: Opt[int] = attrib(default=None, metadata={CASING: "frame_max"})
    client_properties: Opt[ClientProperties] = attrib(default=None, metadata={CASING: "client_properties"})

    def __init__(
        self,
        *,
        recv_oct: Opt[int] = attrib(default=None, metadata={CASING: "recv_oct"}),
        recv_oct_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "recv_oct_details"}),
        recv_cnt: Opt[int] = attrib(default=None, metadata={CASING: "recv_cnt"}),
        send_oct: Opt[int] = attrib(default=None, metadata={CASING: "send_oct"}),
        send_oct_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "send_oct_details"}),
        send_cnt: Opt[int] = attrib(default=None, metadata={CASING: "send_cnt"}),
        send_pend: Opt[int] = attrib(default=None, metadata={CASING: "send_pend"}),
        state: Opt[str] = attrib(default=None, metadata={CASING: "state"}),
        last_blocked_by: Opt[str] = attrib(default=None, metadata={CASING: "last_blocked_by"}),
        last_blocked_age: Opt[str] = attrib(default=None, metadata={CASING: "last_blocked_age"}),
        channels: Opt[int] = attrib(default=None, metadata={CASING: "channels"}),
        type_: Opt[str] = attrib(default=None, metadata={CASING: "type"}),
        node: Opt[str] = attrib(default=None, metadata={CASING: "node"}),
        name: Opt[str] = attrib(default=None, metadata={CASING: "name"}),
        host: Opt[str] = attrib(default=None, metadata={CASING: "host"}),
        port: Opt[int] = attrib(default=None, metadata={CASING: "port"}),
        peer_host: Opt[str] = attrib(default=None, metadata={CASING: "peer_host"}),
        peer_port: Opt[int] = attrib(default=None, metadata={CASING: "peer_port"}),
        ssl: Opt[bool] = attrib(default=None, metadata={CASING: "ssl"}),
        peer_cert_subject: Opt[str] = attrib(default=None, metadata={CASING: "peer_cert_subject"}),
        peer_cert_issuer: Opt[str] = attrib(default=None, metadata={CASING: "peer_cert_issuer"}),
        peer_cert_validity: Opt[str] = attrib(default=None, metadata={CASING: "peer_cert_validity"}),
        auth_mechanism: Opt[str] = attrib(default=None, metadata={CASING: "auth_mechanism"}),
        ssl_protocol: Opt[str] = attrib(default=None, metadata={CASING: "ssl_protocol"}),
        ssl_key_exchange: Opt[str] = attrib(default=None, metadata={CASING: "ssl_key_exchange"}),
        ssl_cipher: Opt[str] = attrib(default=None, metadata={CASING: "ssl_cipher"}),
        ssl_hash: Opt[str] = attrib(default=None, metadata={CASING: "ssl_hash"}),
        protocol: Opt[str] = attrib(default=None, metadata={CASING: "protocol"}),
        user: Opt[str] = attrib(default=None, metadata={CASING: "user"}),
        vhost: Opt[str] = attrib(default=None, metadata={CASING: "vhost"}),
        timeout: Opt[int] = attrib(default=None, metadata={CASING: "timeout"}),
        frame_max: Opt[int] = attrib(default=None, metadata={CASING: "frame_max"}),
        client_properties: Opt[ClientProperties] = attrib(default=None, metadata={CASING: "client_properties"}),
    ) -> None:
        """

        Parameters:
            name: The name of the connection. Used as Id.
        """


@attrs(kw_only=True, auto_attribs=True)
class ConnectionDetails(JidType, hint="Coveo.QueueRabbitAdmin.ConnectionDetails"):
    """A structure that contains the name and address of a connection."""

    name: Opt[str] = attrib(default=None, metadata={CASING: "name"})
    peer_host: Opt[str] = attrib(default=None, metadata={CASING: "peer_host"})
    peer_port: Opt[int] = attrib(default=None, metadata={CASING: "peer_port"})

    def __init__(
        self,
        *,
        name: Opt[str] = attrib(default=None, metadata={CASING: "name"}),
        peer_host: Opt[str] = attrib(default=None, metadata={CASING: "peer_host"}),
        peer_port: Opt[int] = attrib(default=None, metadata={CASING: "peer_port"}),
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class Channel(JidType, hint="Coveo.QueueRabbitAdmin.Channel"):
    """A structure that contains information about a channel."""

    connection_details: Opt[ConnectionDetails] = attrib(default=None, metadata={CASING: "connection_details"})
    message_stats: Opt[MessageStats] = attrib(default=None, metadata={CASING: "message_stats"})
    idle_since: Opt[datetime] = attrib(default=None, metadata={CASING: "idle_since"})
    transactional: Opt[bool] = attrib(default=None, metadata={CASING: "transactional"})
    confirm: Opt[bool] = attrib(default=None, metadata={CASING: "confirm"})
    consumer_count: Opt[int] = attrib(default=None, metadata={CASING: "consumer_count"})
    messages_unacknowledged: Opt[int] = attrib(default=None, metadata={CASING: "messages_unacknowledged"})
    messages_unconfirmed: Opt[int] = attrib(default=None, metadata={CASING: "messages_unconfirmed"})
    messages_uncommitted: Opt[int] = attrib(default=None, metadata={CASING: "messages_uncommitted"})
    acks_uncommitted: Opt[int] = attrib(default=None, metadata={CASING: "acks_uncommitted"})
    prefetch_count: Opt[int] = attrib(default=None, metadata={CASING: "prefetch_count"})
    client_flow_blocked: Opt[bool] = attrib(default=None, metadata={CASING: "client_flow_blocked"})
    node: Opt[str] = attrib(default=None, metadata={CASING: "node"})
    name: Opt[str] = attrib(default=None, metadata={CASING: "name"})
    number: Opt[int] = attrib(default=None, metadata={CASING: "number"})
    user: Opt[str] = attrib(default=None, metadata={CASING: "user"})
    vhost: Opt[str] = attrib(default=None, metadata={CASING: "vhost"})

    def __init__(
        self,
        *,
        connection_details: Opt[ConnectionDetails] = attrib(default=None, metadata={CASING: "connection_details"}),
        message_stats: Opt[MessageStats] = attrib(default=None, metadata={CASING: "message_stats"}),
        idle_since: Opt[datetime] = attrib(default=None, metadata={CASING: "idle_since"}),
        transactional: Opt[bool] = attrib(default=None, metadata={CASING: "transactional"}),
        confirm: Opt[bool] = attrib(default=None, metadata={CASING: "confirm"}),
        consumer_count: Opt[int] = attrib(default=None, metadata={CASING: "consumer_count"}),
        messages_unacknowledged: Opt[int] = attrib(default=None, metadata={CASING: "messages_unacknowledged"}),
        messages_unconfirmed: Opt[int] = attrib(default=None, metadata={CASING: "messages_unconfirmed"}),
        messages_uncommitted: Opt[int] = attrib(default=None, metadata={CASING: "messages_uncommitted"}),
        acks_uncommitted: Opt[int] = attrib(default=None, metadata={CASING: "acks_uncommitted"}),
        prefetch_count: Opt[int] = attrib(default=None, metadata={CASING: "prefetch_count"}),
        client_flow_blocked: Opt[bool] = attrib(default=None, metadata={CASING: "client_flow_blocked"}),
        node: Opt[str] = attrib(default=None, metadata={CASING: "node"}),
        name: Opt[str] = attrib(default=None, metadata={CASING: "name"}),
        number: Opt[int] = attrib(default=None, metadata={CASING: "number"}),
        user: Opt[str] = attrib(default=None, metadata={CASING: "user"}),
        vhost: Opt[str] = attrib(default=None, metadata={CASING: "vhost"}),
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExchangeDef(JidType, hint="Coveo.QueueRabbitAdmin.ExchangeDef"):
    """A structure that represents an exchange definition, which can be used to create an exchange.

    Attributes:
        name: The name of the exchange. Used as Id.
        auto_delete: Indicates if the exchange will deleted automatically once all queues have finished using it.
    """

    vhost: str = attrib(default="/", metadata={CASING: "vhost"})
    name: Opt[str] = attrib(default=None, metadata={CASING: "name"})
    type_: Opt[str] = attrib(default=None, metadata={CASING: "type"})
    durable: bool = attrib(default=True, metadata={CASING: "durable"})
    auto_delete: Opt[bool] = attrib(default=None, metadata={CASING: "auto_delete"})
    internal: Opt[bool] = None
    arguments: Opt[Dict[str, Any]] = attrib(default=None, metadata={CASING: "arguments"})

    def __init__(
        self,
        *,
        vhost: str = attrib(default="/", metadata={CASING: "vhost"}),
        name: Opt[str] = attrib(default=None, metadata={CASING: "name"}),
        type_: Opt[str] = attrib(default=None, metadata={CASING: "type"}),
        durable: bool = attrib(default=True, metadata={CASING: "durable"}),
        auto_delete: Opt[bool] = attrib(default=None, metadata={CASING: "auto_delete"}),
        internal: Opt[bool] = None,
        arguments: Opt[Dict[str, Any]] = attrib(default=None, metadata={CASING: "arguments"}),
    ) -> None:
        """

        Parameters:
            name: The name of the exchange. Used as Id.
            auto_delete: Indicates if the exchange will deleted automatically once all queues have finished using it.
        """


@attrs(kw_only=True, auto_attribs=True)
class Exchange(ExchangeDef, hint="Coveo.QueueRabbitAdmin.Exchange"):
    """A structure that represents an exchange."""

    message_stats: Opt[MessageStats] = attrib(default=None, metadata={CASING: "message_stats"})

    def __init__(
        self, *, message_stats: Opt[MessageStats] = attrib(default=None, metadata={CASING: "message_stats"})
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class BindingDef(JidType, hint="Coveo.QueueRabbitAdmin.BindingDef"):
    """A structure that represents a binding definition, which can be used to create a binding.

    Attributes:
        source: The name of the source exchange.
        destination: The name of the destination exchange.
    """

    vhost: str = attrib(default="/", metadata={CASING: "vhost"})
    source: Opt[str] = attrib(default=None, metadata={CASING: "source"})
    destination: Opt[str] = attrib(default=None, metadata={CASING: "destination"})
    destination_type: Opt[DestinationType] = attrib(default=None, metadata={CASING: "destination_type"})
    routing_key: Opt[str] = attrib(default=None, metadata={CASING: "routing_key"})
    arguments: Opt[Dict[str, Any]] = attrib(default=None, metadata={CASING: "arguments"})

    def __init__(
        self,
        *,
        vhost: str = attrib(default="/", metadata={CASING: "vhost"}),
        source: Opt[str] = attrib(default=None, metadata={CASING: "source"}),
        destination: Opt[str] = attrib(default=None, metadata={CASING: "destination"}),
        destination_type: Opt[DestinationType] = attrib(default=None, metadata={CASING: "destination_type"}),
        routing_key: Opt[str] = attrib(default=None, metadata={CASING: "routing_key"}),
        arguments: Opt[Dict[str, Any]] = attrib(default=None, metadata={CASING: "arguments"}),
    ) -> None:
        """

        Parameters:
            source: The name of the source exchange.
            destination: The name of the destination exchange.
        """


@attrs(kw_only=True, auto_attribs=True)
class Binding(BindingDef, hint="Coveo.QueueRabbitAdmin.Binding"):
    """A structure that represents a binding."""

    properties_key: Opt[str] = attrib(default=None, metadata={CASING: "properties_key"})

    def __init__(self, *, properties_key: Opt[str] = attrib(default=None, metadata={CASING: "properties_key"})) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class BackingQueueStatus(JidType, hint="Coveo.QueueRabbitAdmin.BackingQueueStatus"):
    """A structure that contains information and statistics about a backing queue."""

    q1: Opt[int] = attrib(default=None, metadata={CASING: "q1"})
    q2: Opt[int] = attrib(default=None, metadata={CASING: "q2"})
    delta: Opt[List[Any]] = attrib(default=None, metadata={CASING: "delta"})
    q3: Opt[int] = attrib(default=None, metadata={CASING: "q3"})
    q4: Opt[int] = attrib(default=None, metadata={CASING: "q4"})
    len_: Opt[int] = attrib(default=None, metadata={CASING: "len"})
    pending_acks: Opt[int] = attrib(default=None, metadata={CASING: "pending_acks"})
    target_ram_count: Opt[str] = attrib(default=None, metadata={CASING: "target_ram_count"})
    ram_msg_count: Opt[int] = attrib(default=None, metadata={CASING: "ram_msg_count"})
    ram_ack_count: Opt[int] = attrib(default=None, metadata={CASING: "ram_ack_count"})
    next_seq_id: Opt[int] = attrib(default=None, metadata={CASING: "next_seq_id"})
    persistent_count: Opt[int] = attrib(default=None, metadata={CASING: "persistent_count"})
    avg_ingress_rate: Opt[float] = attrib(default=None, metadata={CASING: "avg_ingress_rate"})
    avg_egress_rate: Opt[float] = attrib(default=None, metadata={CASING: "avg_egress_rate"})
    avg_ack_ingress_rate: Opt[float] = attrib(default=None, metadata={CASING: "avg_ack_ingress_rate"})
    avg_ack_egress_rate: Opt[float] = attrib(default=None, metadata={CASING: "avg_ack_egress_rate"})
    mirror_seen: Opt[int] = attrib(default=None, metadata={CASING: "mirror_seen"})
    mirror_senders: Opt[int] = attrib(default=None, metadata={CASING: "mirror_senders"})

    def __init__(
        self,
        *,
        q1: Opt[int] = attrib(default=None, metadata={CASING: "q1"}),
        q2: Opt[int] = attrib(default=None, metadata={CASING: "q2"}),
        delta: Opt[List[Any]] = attrib(default=None, metadata={CASING: "delta"}),
        q3: Opt[int] = attrib(default=None, metadata={CASING: "q3"}),
        q4: Opt[int] = attrib(default=None, metadata={CASING: "q4"}),
        len_: Opt[int] = attrib(default=None, metadata={CASING: "len"}),
        pending_acks: Opt[int] = attrib(default=None, metadata={CASING: "pending_acks"}),
        target_ram_count: Opt[str] = attrib(default=None, metadata={CASING: "target_ram_count"}),
        ram_msg_count: Opt[int] = attrib(default=None, metadata={CASING: "ram_msg_count"}),
        ram_ack_count: Opt[int] = attrib(default=None, metadata={CASING: "ram_ack_count"}),
        next_seq_id: Opt[int] = attrib(default=None, metadata={CASING: "next_seq_id"}),
        persistent_count: Opt[int] = attrib(default=None, metadata={CASING: "persistent_count"}),
        avg_ingress_rate: Opt[float] = attrib(default=None, metadata={CASING: "avg_ingress_rate"}),
        avg_egress_rate: Opt[float] = attrib(default=None, metadata={CASING: "avg_egress_rate"}),
        avg_ack_ingress_rate: Opt[float] = attrib(default=None, metadata={CASING: "avg_ack_ingress_rate"}),
        avg_ack_egress_rate: Opt[float] = attrib(default=None, metadata={CASING: "avg_ack_egress_rate"}),
        mirror_seen: Opt[int] = attrib(default=None, metadata={CASING: "mirror_seen"}),
        mirror_senders: Opt[int] = attrib(default=None, metadata={CASING: "mirror_senders"}),
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ChannelDetails(JidType, hint="Coveo.QueueRabbitAdmin.ChannelDetails"):
    """A structure that contains information about a channel.

    Attributes:
        name: The name of the channel. Used as Id.
        connection_name: The name of the connection used by this channel.
    """

    name: Opt[str] = attrib(default=None, metadata={CASING: "name"})
    number: Opt[int] = attrib(default=None, metadata={CASING: "number"})
    connection_name: Opt[str] = attrib(default=None, metadata={CASING: "connection_name"})
    peer_host: Opt[str] = attrib(default=None, metadata={CASING: "peer_host"})
    peer_port: Opt[int] = attrib(default=None, metadata={CASING: "peer_port"})

    def __init__(
        self,
        *,
        name: Opt[str] = attrib(default=None, metadata={CASING: "name"}),
        number: Opt[int] = attrib(default=None, metadata={CASING: "number"}),
        connection_name: Opt[str] = attrib(default=None, metadata={CASING: "connection_name"}),
        peer_host: Opt[str] = attrib(default=None, metadata={CASING: "peer_host"}),
        peer_port: Opt[int] = attrib(default=None, metadata={CASING: "peer_port"}),
    ) -> None:
        """

        Parameters:
            name: The name of the channel. Used as Id.
            connection_name: The name of the connection used by this channel.
        """


@attrs(kw_only=True, auto_attribs=True)
class NameVhostDetails(JidType, hint="Coveo.QueueRabbitAdmin.NameVhostDetails"):
    """A structure that identifies a named resource on a vhost.

    Attributes:
        name: The named resource.
        vhost: The virtual host where the resource is located.
    """

    name: Opt[str] = attrib(default=None, metadata={CASING: "name"})
    vhost: Opt[str] = attrib(default=None, metadata={CASING: "vhost"})

    def __init__(
        self,
        *,
        name: Opt[str] = attrib(default=None, metadata={CASING: "name"}),
        vhost: Opt[str] = attrib(default=None, metadata={CASING: "vhost"}),
    ) -> None:
        """

        Parameters:
            name: The named resource.
            vhost: The virtual host where the resource is located.
        """


@attrs(kw_only=True, auto_attribs=True)
class ConsumerDetails(JidType, hint="Coveo.QueueRabbitAdmin.ConsumerDetails"):
    """A structure that contains details about a consumer."""

    channel_details: Opt[ChannelDetails] = attrib(default=None, metadata={CASING: "channel_details"})
    queue_details: Opt[NameVhostDetails] = attrib(default=None, metadata={CASING: "queue_details"})
    consumer_tag: Opt[str] = attrib(default=None, metadata={CASING: "consumer_tag"})
    exclusive: Opt[bool] = attrib(default=None, metadata={CASING: "exclusive"})
    ack_required: Opt[bool] = attrib(default=None, metadata={CASING: "ack_required"})

    def __init__(
        self,
        *,
        channel_details: Opt[ChannelDetails] = attrib(default=None, metadata={CASING: "channel_details"}),
        queue_details: Opt[NameVhostDetails] = attrib(default=None, metadata={CASING: "queue_details"}),
        consumer_tag: Opt[str] = attrib(default=None, metadata={CASING: "consumer_tag"}),
        exclusive: Opt[bool] = attrib(default=None, metadata={CASING: "exclusive"}),
        ack_required: Opt[bool] = attrib(default=None, metadata={CASING: "ack_required"}),
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class IncomingDetails(JidType, hint="Coveo.QueueRabbitAdmin.IncomingDetails"):
    """A structure that contains information and statistics about incoming messages."""

    stats: Opt[MessageStats] = attrib(default=None, metadata={CASING: "stats"})
    exchange: Opt[NameVhostDetails] = attrib(default=None, metadata={CASING: "exchange"})

    def __init__(
        self,
        *,
        stats: Opt[MessageStats] = attrib(default=None, metadata={CASING: "stats"}),
        exchange: Opt[NameVhostDetails] = attrib(default=None, metadata={CASING: "exchange"}),
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class DeliveriesDetails(JidType, hint="Coveo.QueueRabbitAdmin.DeliveriesDetails"):
    """A structure that contains information and statistics about delivered messages."""

    stats: Opt[MessageStats] = attrib(default=None, metadata={CASING: "stats"})
    channel_details: Opt[ChannelDetails] = attrib(default=None, metadata={CASING: "channel_details"})

    def __init__(
        self,
        *,
        stats: Opt[MessageStats] = attrib(default=None, metadata={CASING: "stats"}),
        channel_details: Opt[ChannelDetails] = attrib(default=None, metadata={CASING: "channel_details"}),
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class QueueDef(JidType, hint="Coveo.QueueRabbitAdmin.QueueDef"):
    """A structure that represents a queue definition, which can be used to create a queue.

    Attributes:
        name: The name of the queue. Used as Id.
        durable: Indicates if the queue is durable. Durable queues are not lost when RabbitMQ is shutdown. This setting has no impact on individual message durability which is set on a per-message basis. Default is true.
        auto_delete: Indicates if the queue is to be deleted automatically once the last consumer unsubscribes.
    """

    vhost: str = attrib(default="/", metadata={CASING: "vhost"})
    name: Opt[str] = attrib(default=None, metadata={CASING: "name"})
    durable: bool = attrib(default=True, metadata={CASING: "durable"})
    auto_delete: Opt[bool] = attrib(default=None, metadata={CASING: "auto_delete"})
    arguments: Opt[Dict[str, Any]] = attrib(default=None, metadata={CASING: "arguments"})
    node: Opt[str] = attrib(default=None, metadata={CASING: "node"})

    def __init__(
        self,
        *,
        vhost: str = attrib(default="/", metadata={CASING: "vhost"}),
        name: Opt[str] = attrib(default=None, metadata={CASING: "name"}),
        durable: bool = attrib(default=True, metadata={CASING: "durable"}),
        auto_delete: Opt[bool] = attrib(default=None, metadata={CASING: "auto_delete"}),
        arguments: Opt[Dict[str, Any]] = attrib(default=None, metadata={CASING: "arguments"}),
        node: Opt[str] = attrib(default=None, metadata={CASING: "node"}),
    ) -> None:
        """

        Parameters:
            name: The name of the queue. Used as Id.
            durable: Indicates if the queue is durable. Durable queues are not lost when RabbitMQ is shutdown. This setting has no impact on individual message durability which is set on a per-message basis. Default is true.
            auto_delete: Indicates if the queue is to be deleted automatically once the last consumer unsubscribes.
        """


@attrs(kw_only=True, auto_attribs=True)
class Queue(QueueDef, hint="Coveo.QueueRabbitAdmin.Queue"):
    """A structure that contains information and statistics about a queue."""

    memory: Opt[int] = attrib(default=None, metadata={CASING: "memory"})
    owner_pid_details: Opt[ConnectionDetails] = attrib(default=None, metadata={CASING: "owner_pid_details"})
    idle_since: Opt[datetime] = attrib(default=None, metadata={CASING: "idle_since"})
    policy: Opt[str] = attrib(default=None, metadata={CASING: "policy"})
    exclusive_consumer_tag: Opt[str] = attrib(default=None, metadata={CASING: "exclusive_consumer_tag"})
    messages: Opt[int] = attrib(default=None, metadata={CASING: "messages"})
    messages_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "messages_details"})
    messages_ready: Opt[int] = attrib(default=None, metadata={CASING: "messages_ready"})
    messages_ready_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "messages_ready_details"})
    messages_unacknowledged: Opt[int] = attrib(default=None, metadata={CASING: "messages_unacknowledged"})
    messages_unacknowledged_details: Opt[MessagesDetails] = attrib(
        default=None, metadata={CASING: "messages_unacknowledged_details"}
    )
    consumers: Opt[int] = attrib(default=None, metadata={CASING: "consumers"})
    active_consumers: Opt[int] = attrib(default=None, metadata={CASING: "active_consumers"})
    slave_nodes: Opt[List[str]] = attrib(default=None, metadata={CASING: "slave_nodes"})
    synchronised_slave_nodes: Opt[List[str]] = attrib(default=None, metadata={CASING: "synchronised_slave_nodes"})
    backing_queue_status: Opt[BackingQueueStatus] = attrib(default=None, metadata={CASING: "backing_queue_status"})
    incoming: Opt[List[IncomingDetails]] = attrib(default=None, metadata={CASING: "incoming"})
    deliveries: Opt[List[DeliveriesDetails]] = attrib(default=None, metadata={CASING: "deliveries"})
    message_stats: Opt[MessageStats] = attrib(default=None, metadata={CASING: "message_stats"})
    consumer_details: Opt[List[ConsumerDetails]] = attrib(default=None, metadata={CASING: "consumer_details"})
    status: Opt[str] = attrib(default=None, metadata={CASING: "status"})
    sync_messages: Opt[int] = attrib(default=None, metadata={CASING: "sync_messages"})
    effective_policy_definition: Opt[Dict[str, Any]] = attrib(
        default=None, metadata={CASING: "effective_policy_definition"}
    )

    def __init__(
        self,
        *,
        memory: Opt[int] = attrib(default=None, metadata={CASING: "memory"}),
        owner_pid_details: Opt[ConnectionDetails] = attrib(default=None, metadata={CASING: "owner_pid_details"}),
        idle_since: Opt[datetime] = attrib(default=None, metadata={CASING: "idle_since"}),
        policy: Opt[str] = attrib(default=None, metadata={CASING: "policy"}),
        exclusive_consumer_tag: Opt[str] = attrib(default=None, metadata={CASING: "exclusive_consumer_tag"}),
        messages: Opt[int] = attrib(default=None, metadata={CASING: "messages"}),
        messages_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "messages_details"}),
        messages_ready: Opt[int] = attrib(default=None, metadata={CASING: "messages_ready"}),
        messages_ready_details: Opt[MessagesDetails] = attrib(
            default=None, metadata={CASING: "messages_ready_details"}
        ),
        messages_unacknowledged: Opt[int] = attrib(default=None, metadata={CASING: "messages_unacknowledged"}),
        messages_unacknowledged_details: Opt[MessagesDetails] = attrib(
            default=None, metadata={CASING: "messages_unacknowledged_details"}
        ),
        consumers: Opt[int] = attrib(default=None, metadata={CASING: "consumers"}),
        active_consumers: Opt[int] = attrib(default=None, metadata={CASING: "active_consumers"}),
        slave_nodes: Opt[List[str]] = attrib(default=None, metadata={CASING: "slave_nodes"}),
        synchronised_slave_nodes: Opt[List[str]] = attrib(default=None, metadata={CASING: "synchronised_slave_nodes"}),
        backing_queue_status: Opt[BackingQueueStatus] = attrib(default=None, metadata={CASING: "backing_queue_status"}),
        incoming: Opt[List[IncomingDetails]] = attrib(default=None, metadata={CASING: "incoming"}),
        deliveries: Opt[List[DeliveriesDetails]] = attrib(default=None, metadata={CASING: "deliveries"}),
        message_stats: Opt[MessageStats] = attrib(default=None, metadata={CASING: "message_stats"}),
        consumer_details: Opt[List[ConsumerDetails]] = attrib(default=None, metadata={CASING: "consumer_details"}),
        status: Opt[str] = attrib(default=None, metadata={CASING: "status"}),
        sync_messages: Opt[int] = attrib(default=None, metadata={CASING: "sync_messages"}),
        effective_policy_definition: Opt[Dict[str, Any]] = attrib(
            default=None, metadata={CASING: "effective_policy_definition"}
        ),
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class VhostDef(JidType, hint="Coveo.QueueRabbitAdmin.VhostDef"):
    """A structure that represents a virtual host definition, which can be used to create a virtual host."""

    name: Opt[str] = attrib(default=None, metadata={CASING: "name"})

    def __init__(self, *, name: Opt[str] = attrib(default=None, metadata={CASING: "name"})) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class Vhost(VhostDef, hint="Coveo.QueueRabbitAdmin.Vhost"):
    """A structure that contains information and statistics about a virtual host.

    Attributes:
        tracing: Enables tracing, for debugging purposes. See http://www.rabbitmq.com/firehose.html
    """

    message_stats: Opt[MessageStats] = attrib(default=None, metadata={CASING: "message_stats"})
    messages: Opt[int] = attrib(default=None, metadata={CASING: "messages"})
    messages_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "messagesDetails"})
    messages_ready: Opt[int] = attrib(default=None, metadata={CASING: "messages_ready"})
    messages_ready_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "messages_ready_details"})
    messages_unacknowledged: Opt[int] = attrib(default=None, metadata={CASING: "messages_unacknowledged"})
    messages_unacknowledged_details: Opt[MessagesDetails] = attrib(
        default=None, metadata={CASING: "messages_unacknowledged_details"}
    )
    tracing: Opt[bool] = attrib(default=None, metadata={CASING: "tracing"})

    def __init__(
        self,
        *,
        message_stats: Opt[MessageStats] = attrib(default=None, metadata={CASING: "message_stats"}),
        messages: Opt[int] = attrib(default=None, metadata={CASING: "messages"}),
        messages_details: Opt[MessagesDetails] = attrib(default=None, metadata={CASING: "messagesDetails"}),
        messages_ready: Opt[int] = attrib(default=None, metadata={CASING: "messages_ready"}),
        messages_ready_details: Opt[MessagesDetails] = attrib(
            default=None, metadata={CASING: "messages_ready_details"}
        ),
        messages_unacknowledged: Opt[int] = attrib(default=None, metadata={CASING: "messages_unacknowledged"}),
        messages_unacknowledged_details: Opt[MessagesDetails] = attrib(
            default=None, metadata={CASING: "messages_unacknowledged_details"}
        ),
        tracing: Opt[bool] = attrib(default=None, metadata={CASING: "tracing"}),
    ) -> None:
        """

        Parameters:
            tracing: Enables tracing, for debugging purposes. See http://www.rabbitmq.com/firehose.html
        """


@attrs(kw_only=True, auto_attribs=True)
class UserDef(JidType, hint="Coveo.QueueRabbitAdmin.UserDef"):
    """A structure that represents a user definition, which can be used to create a user."""

    name: Opt[str] = attrib(default=None, metadata={CASING: "name"})
    password: Opt[str] = attrib(default=None, metadata={CASING: "password"})
    password_hash: Opt[str] = attrib(default=None, metadata={CASING: "password_hash"})
    tags: Opt[str] = attrib(default=None, metadata={CASING: "tags"})

    def __init__(
        self,
        *,
        name: Opt[str] = attrib(default=None, metadata={CASING: "name"}),
        password: Opt[str] = attrib(default=None, metadata={CASING: "password"}),
        password_hash: Opt[str] = attrib(default=None, metadata={CASING: "password_hash"}),
        tags: Opt[str] = attrib(default=None, metadata={CASING: "tags"}),
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class User(UserDef, hint="Coveo.QueueRabbitAdmin.User"):
    """A structure that represents a user."""

    auth_backend: Opt[str] = attrib(default=None, metadata={CASING: "auth_backend"})

    def __init__(self, *, auth_backend: Opt[str] = attrib(default=None, metadata={CASING: "auth_backend"})) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class PolicyDef(JidType, hint="Coveo.QueueRabbitAdmin.PolicyDef"):
    """A structure that represents a policy.

    Attributes:
        name: The name of the policy. Used as Id.
    """

    vhost: str = attrib(default="/", metadata={CASING: "vhost"})
    name: Opt[str] = attrib(default=None, metadata={CASING: "name"})
    pattern: Opt[str] = attrib(default=None, metadata={CASING: "pattern"})
    definition: Opt[Dict[str, Any]] = attrib(default=None, metadata={CASING: "definition"})
    priority: Opt[int] = attrib(default=None, metadata={CASING: "priority"})

    def __init__(
        self,
        *,
        vhost: str = attrib(default="/", metadata={CASING: "vhost"}),
        name: Opt[str] = attrib(default=None, metadata={CASING: "name"}),
        pattern: Opt[str] = attrib(default=None, metadata={CASING: "pattern"}),
        definition: Opt[Dict[str, Any]] = attrib(default=None, metadata={CASING: "definition"}),
        priority: Opt[int] = attrib(default=None, metadata={CASING: "priority"}),
    ) -> None:
        """

        Parameters:
            name: The name of the policy. Used as Id.
        """


@attrs(kw_only=True, auto_attribs=True)
class ParameterDef(JidType, hint="Coveo.QueueRabbitAdmin.ParameterDef"):
    """A structure that represents a parameter definition.

    Attributes:
        component: The name of the component to which this parameter applies.
        name: The name of the parameter. Used as Id.
    """

    vhost: str = attrib(default="/", metadata={CASING: "vhost"})
    component: Opt[str] = attrib(default=None, metadata={CASING: "component"})
    name: Opt[str] = attrib(default=None, metadata={CASING: "name"})
    value: Opt[str] = attrib(default=None, metadata={CASING: "value"})

    def __init__(
        self,
        *,
        vhost: str = attrib(default="/", metadata={CASING: "vhost"}),
        component: Opt[str] = attrib(default=None, metadata={CASING: "component"}),
        name: Opt[str] = attrib(default=None, metadata={CASING: "name"}),
        value: Opt[str] = attrib(default=None, metadata={CASING: "value"}),
    ) -> None:
        """

        Parameters:
            component: The name of the component to which this parameter applies.
            name: The name of the parameter. Used as Id.
        """


@attrs(kw_only=True, auto_attribs=True)
class Definitions(JidType, hint="Coveo.QueueRabbitAdmin.Definitions"):
    """A structure that contains various resource definitions."""

    rabbit_version: Opt[str] = attrib(default=None, metadata={CASING: "rabbit_version"})
    users: Opt[List[UserDef]] = attrib(default=None, metadata={CASING: "users"})
    vhosts: Opt[List[VhostDef]] = attrib(default=None, metadata={CASING: "vhosts"})
    permissions: Opt[List[Permission]] = attrib(default=None, metadata={CASING: "permissions"})
    queues: Opt[List[QueueDef]] = attrib(default=None, metadata={CASING: "queues"})
    exchanges: Opt[List[ExchangeDef]] = attrib(default=None, metadata={CASING: "exchanges"})
    bindings: Opt[List[BindingDef]] = attrib(default=None, metadata={CASING: "bindings"})
    policies: Opt[List[PolicyDef]] = attrib(default=None, metadata={CASING: "policies"})
    parameters: Opt[List[PolicyDef]] = attrib(default=None, metadata={CASING: "parameters"})

    def __init__(
        self,
        *,
        rabbit_version: Opt[str] = attrib(default=None, metadata={CASING: "rabbit_version"}),
        users: Opt[List[UserDef]] = attrib(default=None, metadata={CASING: "users"}),
        vhosts: Opt[List[VhostDef]] = attrib(default=None, metadata={CASING: "vhosts"}),
        permissions: Opt[List[Permission]] = attrib(default=None, metadata={CASING: "permissions"}),
        queues: Opt[List[QueueDef]] = attrib(default=None, metadata={CASING: "queues"}),
        exchanges: Opt[List[ExchangeDef]] = attrib(default=None, metadata={CASING: "exchanges"}),
        bindings: Opt[List[BindingDef]] = attrib(default=None, metadata={CASING: "bindings"}),
        policies: Opt[List[PolicyDef]] = attrib(default=None, metadata={CASING: "policies"}),
        parameters: Opt[List[PolicyDef]] = attrib(default=None, metadata={CASING: "parameters"}),
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class NodeDef(JidType, hint="Coveo.QueueRabbitAdmin.NodeDef"):
    """A structure that represents a node definition."""

    name: Opt[str] = attrib(default=None, metadata={CASING: "name"})
    machine: Opt[str] = attrib(default=None, metadata={CASING: "machine"})
    type_: NodeType = attrib(default=NodeType.disc, metadata={CASING: "type"})
    port: Opt[int] = attrib(default=None, metadata={CASING: "port"})
    base_path: Opt[str] = attrib(default=None, metadata={CASING: "base_path"})
    rabbit_server_path: Opt[str] = attrib(default=None, metadata={CASING: "rabbit_server_path"})
    erlang_home: Opt[str] = attrib(default=None, metadata={CASING: "erlang_home"})

    def __init__(
        self,
        *,
        name: Opt[str] = attrib(default=None, metadata={CASING: "name"}),
        machine: Opt[str] = attrib(default=None, metadata={CASING: "machine"}),
        type_: NodeType = attrib(default=NodeType.disc, metadata={CASING: "type"}),
        port: Opt[int] = attrib(default=None, metadata={CASING: "port"}),
        base_path: Opt[str] = attrib(default=None, metadata={CASING: "base_path"}),
        rabbit_server_path: Opt[str] = attrib(default=None, metadata={CASING: "rabbit_server_path"}),
        erlang_home: Opt[str] = attrib(default=None, metadata={CASING: "erlang_home"}),
    ) -> None:
        ...


class IQueueAdmin(CoveoInterface):
    """The QueueAdmin API exposes methods used to simplify the interaction between a client application and a RabbitMQ server. Detailed documentation can be found on RabbitMQ's website, and a quick reference is also available by accessing http://localhost:15672/api"""

    @api("GET/overview")
    def get_overview(self) -> Overview:
        """Returns the overview of a server, which includes various information about its configuration and state, as well as statistics about message activity."""

    @api("GET/nodes")
    def get_nodes(self) -> List[Node]:
        """Returns all nodes."""

    @api("GET/nodes/{name}", name="name")
    def get_node(self, *, name: str) -> Node:
        """Returns a specific node.

        Parameters:
            name: The name of a node.
        """

    @api("GET/extensions")
    def get_extensions(self) -> List[Dict[str, str]]:
        """Returns the extensions to the management plugin."""

    @api("GET/definitions")
    def get_definitions(self) -> Definitions:
        """Returns the definitions of the objects on a server - exchanges, queues, bindings, users, virtual hosts and permissions. (i.e.: everything apart from messages.)"""

    @api("POST/definitions", definitions="definitions")
    def merge_definitions(self, *, definitions: Definitions) -> None:
        """Merges a new/updated set of definitions to a server. Existing definitions are left untouched unless they're redefined in the new/updated set.

        Parameters:
            definitions: A set of new or updated definitions.
        """

    @api("GET/connections")
    def get_connections(self) -> List[Connection]:
        """Returns all open connections."""

    @api("GET/connections/{name}", name="name")
    def get_connection(self, *, name: str) -> Connection:
        """Returns an open connection.

        Parameters:
            name: The name of an open connection.
        """

    @api("DELETE/connections/{name}", name="name")
    def delete_connection(self, *, name: str) -> None:
        """Closes a connection.

        Parameters:
            name: The name of an open connection.
        """

    @api("GET/channels")
    def get_channels(self) -> List[Channel]:
        """Returns all open channels."""

    @api("GET/channels/{name}", name="name")
    def get_channel(self, *, name: str) -> Channel:
        """Returns a specific channel.

        Parameters:
            name: The name of a channel.
        """

    @api("GET/exchanges")
    def get_exchanges(self) -> List[Exchange]:
        """Returns all exchanges."""

    @api("GET/exchanges/{vhost}", vhost="vhost")
    def get_exchanges_for_vhost(self, *, vhost: str) -> List[Exchange]:
        """Returns all exchanges from a virtual host.

        Parameters:
            vhost: The name of a virtual host.
        """

    @api("GET/exchanges/{vhost}/{name},out:404}", vhost="vhost", name="name")
    def get_exchange(self, *, vhost: str, name: str) -> Exchange:
        """Returns an exchange.

        Parameters:
            vhost: The name of a virtual host.
            name: The name of an exchange.
        """

    @api("PUT/exchanges/{vhost}/{name},in:*,out:204}")
    def add_exchange(self, *, exchange_def: ExchangeDef) -> None:
        """Adds a new exchange."""

    @api("DELETE/exchanges/{vhost}/{name},out:404>false,out:204>tru}", vhost="vhost", name="name")
    def delete_exchange(self, *, vhost: str, name: str) -> bool:
        """Deletes an exchange.

        Parameters:
            vhost: The name of a virtual host.
            name: The name of an exchange.
        """

    @api("GET/exchanges/{vhost}/{name}/bindings/source", vhost="vhost", name="name")
    def get_exchange_bindings_when_source(self, *, vhost: str, name: str) -> List[Binding]:
        """Returns all bindings that use a specific exchange as the source.

        Parameters:
            vhost: The name of a virtual host.
            name: The name of an exchange.
        """

    @api("GET/exchanges/{vhost}/{name}/bindings/destination", vhost="vhost", name="name")
    def get_exchange_bindings_when_destination(self, *, vhost: str, name: str) -> List[Binding]:
        """Returns all bindings that use a specific exchange as the destination.

        Parameters:
            vhost: The name of a virtual host.
            name: The name of an exchange.
        """

    @api("GET/queues")
    def get_queues(self) -> List[Queue]:
        """Returns all queues."""

    @api("GET/queues?columns={Columns}")
    def get_queues_ex(self, *, columns: str) -> List[Queue]:
        """Returns all queues.

        Parameters:
            columns: The list of comma seperated columns to get
        """

    @api("GET/queues/{vhost}", vhost="vhost")
    def get_queues_for_vhost(self, *, vhost: str) -> List[Queue]:
        """Returns all queues from a virtual host.

        Parameters:
            vhost: The name of a virtual host.
        """

    @api("GET/queues/{vhost}/{name},out:404}", vhost="vhost", name="name")
    def get_queue(self, *, vhost: str, name: str) -> Queue:
        """Returns a specific queue.

        Parameters:
            vhost: The name of a virtual host.
            name: The name of a queue.
        """

    @api("PUT/queues/{vhost}/{name},in:*,out:204}")
    def add_queue(self, *, queue_def: QueueDef) -> None:
        """Adds a new queue."""

    @api("DELETE/queues/{vhost}/{name},out:404>false,out:204>tru}", vhost="vhost", name="name")
    def delete_queue(self, *, vhost: str, name: str) -> bool:
        """Deletes a queue.

        Parameters:
            vhost: The name of a virtual host.
            name: The name of a queue.
        """

    @api("GET/queues/{vhost}/{name}/bindings", vhost="vhost", name="name")
    def get_queue_bindings(self, *, vhost: str, name: str) -> List[Binding]:
        """Returns all bindings on a queue.

        Parameters:
            vhost: The name of a virtual host.
            name: The name of a queue.
        """

    @api("DELETE/queues/{vhost}/{name}/contents", vhost="vhost", name="name")
    def delete_queue_contents(self, *, vhost: str, name: str) -> None:
        """Purges all messages within a queue.

        Parameters:
            vhost: The name of a virtual host.
            name: The name of a queue.
        """

    @api("GET/bindings")
    def get_bindings(self) -> List[Binding]:
        """Returns all bindings."""

    @api("GET/bindings/{vhost}", vhost="vhost")
    def get_bindings_for_vhost(self, *, vhost: str) -> List[Binding]:
        """Returns all bindings from a virtual host.

        Parameters:
            vhost: The name of a virtual host.
        """

    @api("GET/bindings/{vhost}/e/{exchange}/q/{queue}", vhost="vhost", exchange="exchange", queue="queue")
    def get_bindings_for_exchange_and_queue(self, *, vhost: str, exchange: str, queue: str) -> List[Binding]:
        """Returns all bindings between an exchange and a queue. Remark: an exchange and a queue can be bound together multiple times.

        Parameters:
            vhost: The name of a virtual host.
            exchange: The name of an exchange.
            queue: The name of a queue.
        """

    @api("GET/bindings/{vhost}/e/{exchange}/q/{queue}/~,out:404->", vhost="vhost", exchange="exchange", queue="queue")
    def get_binding_for_exchange_and_queue(self, *, vhost: str, exchange: str, queue: str) -> Binding:
        """Returns the binding between an exchange and a queue with specific properties. Remark: an exchange and a queue can be bound together multiple times.

        Parameters:
            vhost: The name of a virtual host.
            exchange: The name of an exchange.
            queue: The name of a queue.
        """

    @api("POST/bindings/{vhost}/e/{source}/q/{destination},in:}")
    def add_binding(self, *, binding_def: BindingDef) -> None:
        """Adds a new binding."""

    @api("DELETE/bindings/{vhost}/e/{exchange}/q/{queue}/~", vhost="vhost", exchange="exchange", queue="queue")
    def delete_binding(self, *, vhost: str, exchange: str, queue: str) -> None:
        """Deletes a binding.

        Parameters:
            vhost: The name of a virtual host.
            exchange: The name of an exchange.
            queue: The name of a queue.
        """

    @api("GET/vhosts")
    def get_vhosts(self) -> List[Vhost]:
        """Returns all virtual hosts."""

    @api("GET/vhosts/{name},out:404}", name="name")
    def get_vhost(self, *, name: str) -> Vhost:
        """Returns a specific virtual host.

        Parameters:
            name: The name of a virtual host.
        """

    @api("DELETE/vhosts/{name}", name="name")
    def delete_vhost(self, *, name: str) -> None:
        """Deletes a virtual host.

        Parameters:
            name: The name of a virtual host.
        """

    @api("GET/vhosts/{name}/permissions", name="name")
    def get_vhost_permissions(self, *, name: str) -> List[Permission]:
        """Returns all permissions from a virtual host.

        Parameters:
            name: The name of a virtual host.
        """

    @api("GET/users")
    def get_users(self) -> List[User]:
        """Returns all users."""

    @api("GET/users/{name}", name="name")
    def get_user(self, *, name: str) -> User:
        """Returns a specific user.

        Parameters:
            name: The name of a user.
        """

    @api("PUT/users/{name},in:}")
    def add_user(self, *, user_def: UserDef) -> None:
        """Adds a new user."""

    @api("DELETE/users/{name}", name="name")
    def delete_user(self, *, name: str) -> None:
        """Deletes a user.

        Parameters:
            name: The name of a user.
        """

    @api("GET/users/{name}/permissions", name="name")
    def get_user_permissions(self, *, name: str) -> List[Permission]:
        """Returns all permissions for a specific user.

        Parameters:
            name: The name of a user.
        """

    @api("GET/whoami")
    def get_who_am_i(self) -> User:
        """Returns the currently authenticated user."""

    @api("GET/permissions")
    def get_permissions(self) -> List[Permission]:
        """Returns all permissions."""

    @api("GET/permissions/{vhost}/{user}", vhost="vhost", user="user")
    def get_vhost_user_permission(self, *, vhost: str, user: str) -> Permission:
        """Returns the permission of a user from a virtual host.

        Parameters:
            vhost: The name of a virtual host.
            user: The name of a user.
        """

    @api("PUT/permissions/{vhost}/{user}", vhost="vhost", user="user")
    def add_vhost_user_permission(self, *, vhost: str, user: str, permission: Permission) -> None:
        """Adds a new permission.

        Parameters:
            vhost: The name of the virtual host.
            user: The name of the user.
        """

    @api("DELETE/permissions/{vhost}/{user}", vhost="vhost", user="user")
    def delete_vhost_user_permission(self, *, vhost: str, user: str) -> None:
        """Deletes a permission.

        Parameters:
            vhost: The name of a virtual host.
            user: The name of a user.
        """

    @api("GET/policies")
    def get_policies(self) -> List[PolicyDef]:
        """Returns all policies."""

    @api("GET/policies/{vhost}", vhost="vhost")
    def get_policies_for_vhost(self, *, vhost: str) -> List[PolicyDef]:
        """Returns all policies from a virtual host.

        Parameters:
            vhost: The name of a virtual host.
        """

    @api("GET/policies/{vhost}/{name}", vhost="vhost", name="name")
    def get_policy(self, *, vhost: str, name: str) -> PolicyDef:
        """Returns a specific policy.

        Parameters:
            vhost: The name of a virtual host.
            name: The name of a policy.
        """

    @api("PUT/policies/{vhost}/{name},in:}")
    def add_policy(self, *, policy: PolicyDef) -> None:
        """Adds a new policy."""

    @api("DELETE/policies/{vhost}/{name}", vhost="vhost", name="name")
    def delete_policy(self, *, vhost: str, name: str) -> None:
        """Deletes a policy.

        Parameters:
            vhost: The name of a virtual host.
            name: The name of a policy.
        """

    @api("GET/parameters")
    def get_parameters(self) -> List[ParameterDef]:
        """Returns the parameters of all components."""

    @api("GET/parameters/{component}", component="component")
    def get_parameters_for_component(self, *, component: str) -> List[ParameterDef]:
        """Returns the parameters of a component.

        Parameters:
            component: The name of a component.
        """

    @api("GET/parameters/{component}/{vhost}", component="component", vhost="vhost")
    def get_parameters_for_component_and_vhost(self, *, component: str, vhost: str) -> List[ParameterDef]:
        """Returns the parameters of a component from a virtual host.

        Parameters:
            component: The name of a component.
            vhost: The name of a virtual host.
        """

    @api("GET/parameters/{component}/{vhost}/{name}", component="component", vhost="vhost", name="name")
    def get_parameter(self, *, component: str, vhost: str, name: str) -> ParameterDef:
        """Returns a component parameter.

        Parameters:
            component: The name of a component.
            vhost: The name of a virtual host.
            name: The name of a parameter.
        """

    @api("PUT/parameters/{component}/{vhost}/{name},in:}")
    def add_parameter(self, *, parameter: ParameterDef) -> None:
        """Adds a new parameter."""

    @api("DELETE/parameters/{component}/{vhost}/{name}", component="component", vhost="vhost", name="name")
    def delete_parameter(self, *, component: str, vhost: str, name: str) -> None:
        """Deletes a parameter.

        Parameters:
            component: The name of a component.
            vhost: The name of a virtual host.
            name: The name of a parameter.
        """


@attrs(kw_only=True, auto_attribs=True)
class ClusterDef(JidType, hint="Coveo.QueueRabbitAdmin.ClusterDef"):
    """A structure that represents a cluster definition."""

    nodes: Opt[List[NodeDef]] = None
    queues: Opt[List[QueueDef]] = None
    cookie: Opt[str] = None

    def __init__(
        self, *, nodes: Opt[List[NodeDef]] = None, queues: Opt[List[QueueDef]] = None, cookie: Opt[str] = None
    ) -> None:
        ...


class IClusterAdmin(CoveoInterface):
    """The QueueAdmin API exposes methods used to simplify setup of a RabbitMQ cluster"""
