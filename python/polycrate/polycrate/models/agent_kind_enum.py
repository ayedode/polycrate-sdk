from typing import Literal

AgentKindEnum = Literal["agent", "operator"]

AGENT_KIND_ENUM_VALUES: set[AgentKindEnum] = {
    "agent",
    "operator",
}


def check_agent_kind_enum(value: str) -> AgentKindEnum:
    if value in AGENT_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_KIND_ENUM_VALUES!r}")
