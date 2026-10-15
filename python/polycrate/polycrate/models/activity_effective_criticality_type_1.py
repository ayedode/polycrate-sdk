from typing import Literal

ActivityEffectiveCriticalityType1 = Literal["high", "low", "medium"]

ACTIVITY_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[ActivityEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_activity_effective_criticality_type_1(value: str) -> ActivityEffectiveCriticalityType1:
    if value in ACTIVITY_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITY_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
