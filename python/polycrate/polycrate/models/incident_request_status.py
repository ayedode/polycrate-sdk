from typing import Literal

IncidentRequestStatus = Literal["contained", "investigating", "reported", "resolved", "reviewed"]

INCIDENT_REQUEST_STATUS_VALUES: set[IncidentRequestStatus] = {
    "contained",
    "investigating",
    "reported",
    "resolved",
    "reviewed",
}


def check_incident_request_status(value: str) -> IncidentRequestStatus:
    if value in INCIDENT_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_REQUEST_STATUS_VALUES!r}")
