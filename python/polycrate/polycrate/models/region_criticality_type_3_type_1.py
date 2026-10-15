from typing import Literal

RegionCriticalityType3Type1 = Literal["", "high", "low", "medium"]

REGION_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[RegionCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_region_criticality_type_3_type_1(value: str) -> RegionCriticalityType3Type1:
    if value in REGION_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
