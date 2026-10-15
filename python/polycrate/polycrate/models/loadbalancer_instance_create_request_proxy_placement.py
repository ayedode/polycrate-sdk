from typing import Literal

LoadbalancerInstanceCreateRequestProxyPlacement = Literal["dedicated", "shared"]

LOADBALANCER_INSTANCE_CREATE_REQUEST_PROXY_PLACEMENT_VALUES: set[LoadbalancerInstanceCreateRequestProxyPlacement] = {
    "dedicated",
    "shared",
}


def check_loadbalancer_instance_create_request_proxy_placement(
    value: str,
) -> LoadbalancerInstanceCreateRequestProxyPlacement:
    if value in LOADBALANCER_INSTANCE_CREATE_REQUEST_PROXY_PLACEMENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_CREATE_REQUEST_PROXY_PLACEMENT_VALUES!r}"
    )
