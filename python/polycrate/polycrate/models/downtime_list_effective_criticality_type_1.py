from typing import Literal

DowntimeListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

DOWNTIME_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[DowntimeListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_downtime_list_effective_criticality_type_1(value: str) -> DowntimeListEffectiveCriticalityType1:
    if value in DOWNTIME_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOWNTIME_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
