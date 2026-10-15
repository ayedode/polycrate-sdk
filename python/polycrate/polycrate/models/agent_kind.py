from typing import Literal

AgentKind = Literal["agent", "operator"]

AGENT_KIND_VALUES: set[AgentKind] = {
    "agent",
    "operator",
}


def check_agent_kind(value: str) -> AgentKind:
    if value in AGENT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_KIND_VALUES!r}")
