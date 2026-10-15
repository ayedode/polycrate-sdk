from typing import Literal

IncidentRequestScope = Literal["system", "user"]

INCIDENT_REQUEST_SCOPE_VALUES: set[IncidentRequestScope] = {
    "system",
    "user",
}


def check_incident_request_scope(value: str) -> IncidentRequestScope:
    if value in INCIDENT_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_REQUEST_SCOPE_VALUES!r}")
