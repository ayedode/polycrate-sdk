from typing import Literal

AgentHealthDataRequestStatus = Literal["critical", "degraded", "healthy", "unhealthy"]

AGENT_HEALTH_DATA_REQUEST_STATUS_VALUES: set[AgentHealthDataRequestStatus] = {
    "critical",
    "degraded",
    "healthy",
    "unhealthy",
}


def check_agent_health_data_request_status(value: str) -> AgentHealthDataRequestStatus:
    if value in AGENT_HEALTH_DATA_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_HEALTH_DATA_REQUEST_STATUS_VALUES!r}")
