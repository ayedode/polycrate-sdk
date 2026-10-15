from typing import Literal

AgentListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

AGENT_LIST_STATE_VALUES: set[AgentListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_agent_list_state(value: str) -> AgentListState:
    if value in AGENT_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_LIST_STATE_VALUES!r}")
