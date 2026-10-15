from typing import Literal

PatchedIncidentRequestScope = Literal["system", "user"]

PATCHED_INCIDENT_REQUEST_SCOPE_VALUES: set[PatchedIncidentRequestScope] = {
    "system",
    "user",
}


def check_patched_incident_request_scope(value: str) -> PatchedIncidentRequestScope:
    if value in PATCHED_INCIDENT_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_INCIDENT_REQUEST_SCOPE_VALUES!r}")
