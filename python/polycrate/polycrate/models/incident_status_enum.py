from typing import Literal

IncidentStatusEnum = Literal["contained", "investigating", "reported", "resolved", "reviewed"]

INCIDENT_STATUS_ENUM_VALUES: set[IncidentStatusEnum] = {
    "contained",
    "investigating",
    "reported",
    "resolved",
    "reviewed",
}


def check_incident_status_enum(value: str) -> IncidentStatusEnum:
    if value in INCIDENT_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_STATUS_ENUM_VALUES!r}")
