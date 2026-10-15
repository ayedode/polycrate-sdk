from typing import Literal

LoadbalancerInstanceListDelegationSourceType1 = Literal["loopback_lb", "loopback_object_store"]

LOADBALANCER_INSTANCE_LIST_DELEGATION_SOURCE_TYPE_1_VALUES: set[LoadbalancerInstanceListDelegationSourceType1] = {
    "loopback_lb",
    "loopback_object_store",
}


def check_loadbalancer_instance_list_delegation_source_type_1(
    value: str,
) -> LoadbalancerInstanceListDelegationSourceType1:
    if value in LOADBALANCER_INSTANCE_LIST_DELEGATION_SOURCE_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_LIST_DELEGATION_SOURCE_TYPE_1_VALUES!r}"
    )
