from typing import Literal

ActivityEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

ACTIVITY_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[ActivityEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_activity_effective_criticality_type_2_type_1(value: str) -> ActivityEffectiveCriticalityType2Type1:
    if value in ACTIVITY_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTIVITY_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
