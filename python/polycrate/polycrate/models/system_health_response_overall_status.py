from typing import Literal

SystemHealthResponseOverallStatus = Literal["DEGRADED", "HEALTHY", "UNHEALTHY", "UNKNOWN"]

SYSTEM_HEALTH_RESPONSE_OVERALL_STATUS_VALUES: set[SystemHealthResponseOverallStatus] = {
    "DEGRADED",
    "HEALTHY",
    "UNHEALTHY",
    "UNKNOWN",
}


def check_system_health_response_overall_status(value: str) -> SystemHealthResponseOverallStatus:
    if value in SYSTEM_HEALTH_RESPONSE_OVERALL_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SYSTEM_HEALTH_RESPONSE_OVERALL_STATUS_VALUES!r}")
