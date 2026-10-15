from typing import Literal

RegionListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

REGION_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[RegionListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_region_list_effective_criticality_type_1(value: str) -> RegionListEffectiveCriticalityType1:
    if value in REGION_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
