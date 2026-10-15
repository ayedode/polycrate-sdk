from typing import Literal

DowntimeListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

DOWNTIME_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[DowntimeListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_downtime_list_effective_criticality_type_3_type_1(value: str) -> DowntimeListEffectiveCriticalityType3Type1:
    if value in DOWNTIME_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOWNTIME_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
