from typing import Literal

IncidentState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

INCIDENT_STATE_VALUES: set[IncidentState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_incident_state(value: str) -> IncidentState:
    if value in INCIDENT_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_STATE_VALUES!r}")
