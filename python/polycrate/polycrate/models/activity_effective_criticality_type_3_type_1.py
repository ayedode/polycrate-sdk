from typing import Literal

ActivityEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

ACTIVITY_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[ActivityEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_activity_effective_criticality_type_3_type_1(value: str) -> ActivityEffectiveCriticalityType3Type1:
    if value in ACTIVITY_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTIVITY_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
