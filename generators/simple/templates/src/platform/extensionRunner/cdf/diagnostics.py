"""
    - THIS FILE IS GENERATED -

dependencies/CDF/Cpp/NodeManager/CDFDiagnostics.jid

"""

from enum import auto
from .root import CoveoInterface, JidEnumFlag, api


class DumpType(JidEnumFlag):
    """Defines dump types."""

    Mini: int = auto()
    Normal: int = auto()
    Full: int = auto()


class IDiagnostics(CoveoInterface):
    @api("POST/dump")
    def dump_by_name(self, *, name: str, user_name: str, dump_type: DumpType = DumpType.Full) -> None:
        """Dumps a process identified by a name.

        Parameters:
            name: The name used to identify the process.
            user_name: The user that made the request.
            dump_type: The type of dump.
        """

    @api("POST/dump_pid/{process_id}")
    def dump_by_pid(self, *, process_id: int, user_name: str, dump_type: DumpType = DumpType.Full) -> None:
        """Dumps a process identified by a PID.

        Parameters:
            process_id: The process id.
            user_name: The user that made the request.
            dump_type: The type of dump.
        """

    @api("POST/crash")
    def crash(self) -> None:
        ...


class IAgentDiagnosticsManager(CoveoInterface):
    """The diagnostics API for agents."""

    @api("POST/agents/{agent_name}/dump")
    def dump_agent(self, *, agent_name: str, user_name: str, dump_type: DumpType = DumpType.Full) -> None:
        """Dumps an agent process.

        Parameters:
            agent_name: The id of the agent.
            user_name: The user that made the request.
            dump_type: The type of dump.
        """

    @api("POST/agents/{agent_name}/dump_instance/{instance_id}")
    def dump_instance(
        self, *, agent_name: str, instance_id: str, user_name: str, dump_type: DumpType = DumpType.Full
    ) -> None:
        """Dumps an instance process.

        Parameters:
            agent_name: The id of the agent.
            instance_id: The id of the instance.
            user_name: The user that made the request.
            dump_type: The type of dump.
        """
