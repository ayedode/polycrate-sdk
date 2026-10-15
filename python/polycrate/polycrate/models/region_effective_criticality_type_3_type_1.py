from typing import Literal

RegionEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

REGION_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[RegionEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_region_effective_criticality_type_3_type_1(value: str) -> RegionEffectiveCriticalityType3Type1:
    if value in REGION_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REGION_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
