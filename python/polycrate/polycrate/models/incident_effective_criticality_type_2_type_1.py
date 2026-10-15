from typing import Literal

IncidentEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

INCIDENT_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[IncidentEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_incident_effective_criticality_type_2_type_1(value: str) -> IncidentEffectiveCriticalityType2Type1:
    if value in INCIDENT_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
