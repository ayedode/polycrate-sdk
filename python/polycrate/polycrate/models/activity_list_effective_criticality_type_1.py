from typing import Literal

ActivityListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

ACTIVITY_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[ActivityListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_activity_list_effective_criticality_type_1(value: str) -> ActivityListEffectiveCriticalityType1:
    if value in ACTIVITY_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTIVITY_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
