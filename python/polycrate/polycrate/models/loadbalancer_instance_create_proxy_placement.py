from typing import Literal

LoadbalancerInstanceCreateProxyPlacement = Literal["dedicated", "shared"]

LOADBALANCER_INSTANCE_CREATE_PROXY_PLACEMENT_VALUES: set[LoadbalancerInstanceCreateProxyPlacement] = {
    "dedicated",
    "shared",
}


def check_loadbalancer_instance_create_proxy_placement(value: str) -> LoadbalancerInstanceCreateProxyPlacement:
    if value in LOADBALANCER_INSTANCE_CREATE_PROXY_PLACEMENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_CREATE_PROXY_PLACEMENT_VALUES!r}"
    )
