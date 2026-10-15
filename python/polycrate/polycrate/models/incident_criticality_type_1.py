from typing import Literal

IncidentCriticalityType1 = Literal["", "high", "low", "medium"]

INCIDENT_CRITICALITY_TYPE_1_VALUES: set[IncidentCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_incident_criticality_type_1(value: str) -> IncidentCriticalityType1:
    if value in INCIDENT_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_CRITICALITY_TYPE_1_VALUES!r}")
