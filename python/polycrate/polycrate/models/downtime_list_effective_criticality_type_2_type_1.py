from typing import Literal

DowntimeListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

DOWNTIME_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[DowntimeListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_downtime_list_effective_criticality_type_2_type_1(value: str) -> DowntimeListEffectiveCriticalityType2Type1:
    if value in DOWNTIME_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOWNTIME_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
