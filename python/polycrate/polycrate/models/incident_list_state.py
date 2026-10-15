from typing import Literal

IncidentListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

INCIDENT_LIST_STATE_VALUES: set[IncidentListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_incident_list_state(value: str) -> IncidentListState:
    if value in INCIDENT_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_LIST_STATE_VALUES!r}")
