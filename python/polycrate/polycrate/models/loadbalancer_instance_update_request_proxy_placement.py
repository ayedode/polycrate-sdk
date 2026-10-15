from typing import Literal

LoadbalancerInstanceUpdateRequestProxyPlacement = Literal["dedicated", "shared"]

LOADBALANCER_INSTANCE_UPDATE_REQUEST_PROXY_PLACEMENT_VALUES: set[LoadbalancerInstanceUpdateRequestProxyPlacement] = {
    "dedicated",
    "shared",
}


def check_loadbalancer_instance_update_request_proxy_placement(
    value: str,
) -> LoadbalancerInstanceUpdateRequestProxyPlacement:
    if value in LOADBALANCER_INSTANCE_UPDATE_REQUEST_PROXY_PLACEMENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_UPDATE_REQUEST_PROXY_PLACEMENT_VALUES!r}"
    )
