from typing import Literal

IncidentEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

INCIDENT_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[IncidentEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_incident_effective_criticality_type_3_type_1(value: str) -> IncidentEffectiveCriticalityType3Type1:
    if value in INCIDENT_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
