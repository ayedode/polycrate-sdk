from typing import Literal

LoadbalancerRegionEffectiveCriticalityType1 = Literal["high", "low", "medium"]

LOADBALANCER_REGION_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[LoadbalancerRegionEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_loadbalancer_region_effective_criticality_type_1(value: str) -> LoadbalancerRegionEffectiveCriticalityType1:
    if value in LOADBALANCER_REGION_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_REGION_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
