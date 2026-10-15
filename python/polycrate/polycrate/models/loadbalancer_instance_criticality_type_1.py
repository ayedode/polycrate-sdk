from typing import Literal

LoadbalancerInstanceCriticalityType1 = Literal["", "high", "low", "medium"]

LOADBALANCER_INSTANCE_CRITICALITY_TYPE_1_VALUES: set[LoadbalancerInstanceCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_loadbalancer_instance_criticality_type_1(value: str) -> LoadbalancerInstanceCriticalityType1:
    if value in LOADBALANCER_INSTANCE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_CRITICALITY_TYPE_1_VALUES!r}")
