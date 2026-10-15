from typing import Literal

IncidentEffectiveCriticalityType1 = Literal["high", "low", "medium"]

INCIDENT_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[IncidentEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_incident_effective_criticality_type_1(value: str) -> IncidentEffectiveCriticalityType1:
    if value in INCIDENT_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
