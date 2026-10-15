from typing import Literal

ActivityCriticalityType1 = Literal["high", "low", "medium"]

ACTIVITY_CRITICALITY_TYPE_1_VALUES: set[ActivityCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_activity_criticality_type_1(value: str) -> ActivityCriticalityType1:
    if value in ACTIVITY_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITY_CRITICALITY_TYPE_1_VALUES!r}")
