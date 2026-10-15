from typing import Literal

LoadbalancerInstanceRequestProxyPlacement = Literal["dedicated", "shared"]

LOADBALANCER_INSTANCE_REQUEST_PROXY_PLACEMENT_VALUES: set[LoadbalancerInstanceRequestProxyPlacement] = {
    "dedicated",
    "shared",
}


def check_loadbalancer_instance_request_proxy_placement(value: str) -> LoadbalancerInstanceRequestProxyPlacement:
    if value in LOADBALANCER_INSTANCE_REQUEST_PROXY_PLACEMENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_REQUEST_PROXY_PLACEMENT_VALUES!r}"
    )
