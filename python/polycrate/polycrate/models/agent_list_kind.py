from typing import Literal

AgentListKind = Literal["agent", "operator"]

AGENT_LIST_KIND_VALUES: set[AgentListKind] = {
    "agent",
    "operator",
}


def check_agent_list_kind(value: str) -> AgentListKind:
    if value in AGENT_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_LIST_KIND_VALUES!r}")
