from typing import Literal

PatchedIncidentRequestStatus = Literal["contained", "investigating", "reported", "resolved", "reviewed"]

PATCHED_INCIDENT_REQUEST_STATUS_VALUES: set[PatchedIncidentRequestStatus] = {
    "contained",
    "investigating",
    "reported",
    "resolved",
    "reviewed",
}


def check_patched_incident_request_status(value: str) -> PatchedIncidentRequestStatus:
    if value in PATCHED_INCIDENT_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_INCIDENT_REQUEST_STATUS_VALUES!r}")
