from typing import Literal

IncidentListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

INCIDENT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[IncidentListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_incident_list_effective_criticality_type_1(value: str) -> IncidentListEffectiveCriticalityType1:
    if value in INCIDENT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
