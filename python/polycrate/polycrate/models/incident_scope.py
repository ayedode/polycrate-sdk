from typing import Literal

IncidentScope = Literal["system", "user"]

INCIDENT_SCOPE_VALUES: set[IncidentScope] = {
    "system",
    "user",
}


def check_incident_scope(value: str) -> IncidentScope:
    if value in INCIDENT_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_SCOPE_VALUES!r}")
