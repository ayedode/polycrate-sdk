from typing import Literal

ActivityListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

ACTIVITY_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[ActivityListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_activity_list_effective_criticality_type_2_type_1(value: str) -> ActivityListEffectiveCriticalityType2Type1:
    if value in ACTIVITY_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTIVITY_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
