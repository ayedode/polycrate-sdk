from typing import Literal

IncidentCriticalityType2Type1 = Literal["", "high", "low", "medium"]

INCIDENT_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[IncidentCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_incident_criticality_type_2_type_1(value: str) -> IncidentCriticalityType2Type1:
    if value in INCIDENT_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
