from typing import Literal

AgentHealthDataStatusEnum = Literal["critical", "degraded", "healthy", "unhealthy"]

AGENT_HEALTH_DATA_STATUS_ENUM_VALUES: set[AgentHealthDataStatusEnum] = {
    "critical",
    "degraded",
    "healthy",
    "unhealthy",
}


def check_agent_health_data_status_enum(value: str) -> AgentHealthDataStatusEnum:
    if value in AGENT_HEALTH_DATA_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_HEALTH_DATA_STATUS_ENUM_VALUES!r}")
