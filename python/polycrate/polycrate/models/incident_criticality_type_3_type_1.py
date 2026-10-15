from typing import Literal

IncidentCriticalityType3Type1 = Literal["", "high", "low", "medium"]

INCIDENT_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[IncidentCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_incident_criticality_type_3_type_1(value: str) -> IncidentCriticalityType3Type1:
    if value in INCIDENT_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
