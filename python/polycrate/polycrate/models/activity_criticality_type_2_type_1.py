from typing import Literal

ActivityCriticalityType2Type1 = Literal["high", "low", "medium"]

ACTIVITY_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[ActivityCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_activity_criticality_type_2_type_1(value: str) -> ActivityCriticalityType2Type1:
    if value in ACTIVITY_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITY_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
