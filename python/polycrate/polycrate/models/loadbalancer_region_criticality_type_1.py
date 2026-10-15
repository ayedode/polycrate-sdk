from typing import Literal

LoadbalancerRegionCriticalityType1 = Literal["", "high", "low", "medium"]

LOADBALANCER_REGION_CRITICALITY_TYPE_1_VALUES: set[LoadbalancerRegionCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_loadbalancer_region_criticality_type_1(value: str) -> LoadbalancerRegionCriticalityType1:
    if value in LOADBALANCER_REGION_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_REGION_CRITICALITY_TYPE_1_VALUES!r}")
