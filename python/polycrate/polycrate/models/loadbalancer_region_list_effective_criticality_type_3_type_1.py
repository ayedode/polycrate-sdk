from typing import Literal

LoadbalancerRegionListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

LOADBALANCER_REGION_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    LoadbalancerRegionListEffectiveCriticalityType3Type1
] = {
    "high",
    "low",
    "medium",
}


def check_loadbalancer_region_list_effective_criticality_type_3_type_1(
    value: str,
) -> LoadbalancerRegionListEffectiveCriticalityType3Type1:
    if value in LOADBALANCER_REGION_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_REGION_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
