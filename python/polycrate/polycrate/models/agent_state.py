from typing import Literal

AgentState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

AGENT_STATE_VALUES: set[AgentState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_agent_state(value: str) -> AgentState:
    if value in AGENT_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_STATE_VALUES!r}")
