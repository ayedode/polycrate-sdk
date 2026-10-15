from typing import Literal

AgentHealthDataRequestKind = Literal["agent", "operator"]

AGENT_HEALTH_DATA_REQUEST_KIND_VALUES: set[AgentHealthDataRequestKind] = {
    "agent",
    "operator",
}


def check_agent_health_data_request_kind(value: str) -> AgentHealthDataRequestKind:
    if value in AGENT_HEALTH_DATA_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_HEALTH_DATA_REQUEST_KIND_VALUES!r}")
