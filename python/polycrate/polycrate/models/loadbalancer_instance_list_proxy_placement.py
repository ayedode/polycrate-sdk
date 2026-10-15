from typing import Literal

LoadbalancerInstanceListProxyPlacement = Literal["dedicated", "shared"]

LOADBALANCER_INSTANCE_LIST_PROXY_PLACEMENT_VALUES: set[LoadbalancerInstanceListProxyPlacement] = {
    "dedicated",
    "shared",
}


def check_loadbalancer_instance_list_proxy_placement(value: str) -> LoadbalancerInstanceListProxyPlacement:
    if value in LOADBALANCER_INSTANCE_LIST_PROXY_PLACEMENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_LIST_PROXY_PLACEMENT_VALUES!r}"
    )
