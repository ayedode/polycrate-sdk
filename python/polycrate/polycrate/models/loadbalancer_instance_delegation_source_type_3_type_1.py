from typing import Literal

LoadbalancerInstanceDelegationSourceType3Type1 = Literal["loopback_lb", "loopback_object_store"]

LOADBALANCER_INSTANCE_DELEGATION_SOURCE_TYPE_3_TYPE_1_VALUES: set[LoadbalancerInstanceDelegationSourceType3Type1] = {
    "loopback_lb",
    "loopback_object_store",
}


def check_loadbalancer_instance_delegation_source_type_3_type_1(
    value: str,
) -> LoadbalancerInstanceDelegationSourceType3Type1:
    if value in LOADBALANCER_INSTANCE_DELEGATION_SOURCE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_DELEGATION_SOURCE_TYPE_3_TYPE_1_VALUES!r}"
    )
