from typing import Literal

LoadbalancerInstanceListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

LOADBALANCER_INSTANCE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[
    LoadbalancerInstanceListEffectiveCriticalityType1
] = {
    "high",
    "low",
    "medium",
}


def check_loadbalancer_instance_list_effective_criticality_type_1(
    value: str,
) -> LoadbalancerInstanceListEffectiveCriticalityType1:
    if value in LOADBALANCER_INSTANCE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
