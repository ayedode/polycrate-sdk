from typing import Literal

OverallStatusEnum = Literal["DEGRADED", "HEALTHY", "UNHEALTHY", "UNKNOWN"]

OVERALL_STATUS_ENUM_VALUES: set[OverallStatusEnum] = {
    "DEGRADED",
    "HEALTHY",
    "UNHEALTHY",
    "UNKNOWN",
}


def check_overall_status_enum(value: str) -> OverallStatusEnum:
    if value in OVERALL_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OVERALL_STATUS_ENUM_VALUES!r}")
