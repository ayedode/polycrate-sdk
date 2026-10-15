from typing import Literal

LoadbalancerInstanceUpdateProxyPlacement = Literal["dedicated", "shared"]

LOADBALANCER_INSTANCE_UPDATE_PROXY_PLACEMENT_VALUES: set[LoadbalancerInstanceUpdateProxyPlacement] = {
    "dedicated",
    "shared",
}


def check_loadbalancer_instance_update_proxy_placement(value: str) -> LoadbalancerInstanceUpdateProxyPlacement:
    if value in LOADBALANCER_INSTANCE_UPDATE_PROXY_PLACEMENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_UPDATE_PROXY_PLACEMENT_VALUES!r}"
    )
