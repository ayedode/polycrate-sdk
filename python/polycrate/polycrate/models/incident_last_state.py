from typing import Literal

IncidentLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

INCIDENT_LAST_STATE_VALUES: set[IncidentLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_incident_last_state(value: str) -> IncidentLastState:
    if value in INCIDENT_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_LAST_STATE_VALUES!r}")
