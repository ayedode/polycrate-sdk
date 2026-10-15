from typing import Literal

IncidentStatus = Literal["contained", "investigating", "reported", "resolved", "reviewed"]

INCIDENT_STATUS_VALUES: set[IncidentStatus] = {
    "contained",
    "investigating",
    "reported",
    "resolved",
    "reviewed",
}


def check_incident_status(value: str) -> IncidentStatus:
    if value in INCIDENT_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_STATUS_VALUES!r}")
