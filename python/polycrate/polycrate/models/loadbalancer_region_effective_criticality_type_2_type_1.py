from typing import Literal

LoadbalancerRegionEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

LOADBALANCER_REGION_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    LoadbalancerRegionEffectiveCriticalityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_loadbalancer_region_effective_criticality_type_2_type_1(
    value: str,
) -> LoadbalancerRegionEffectiveCriticalityType2Type1:
    if value in LOADBALANCER_REGION_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_REGION_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
