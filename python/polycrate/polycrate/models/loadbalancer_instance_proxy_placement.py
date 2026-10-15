from typing import Literal

LoadbalancerInstanceProxyPlacement = Literal["dedicated", "shared"]

LOADBALANCER_INSTANCE_PROXY_PLACEMENT_VALUES: set[LoadbalancerInstanceProxyPlacement] = {
    "dedicated",
    "shared",
}


def check_loadbalancer_instance_proxy_placement(value: str) -> LoadbalancerInstanceProxyPlacement:
    if value in LOADBALANCER_INSTANCE_PROXY_PLACEMENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_PROXY_PLACEMENT_VALUES!r}")
