from typing import Literal

PatchedLoadbalancerInstanceUpdateRequestProxyPlacement = Literal["dedicated", "shared"]

PATCHED_LOADBALANCER_INSTANCE_UPDATE_REQUEST_PROXY_PLACEMENT_VALUES: set[
    PatchedLoadbalancerInstanceUpdateRequestProxyPlacement
] = {
    "dedicated",
    "shared",
}


def check_patched_loadbalancer_instance_update_request_proxy_placement(
    value: str,
) -> PatchedLoadbalancerInstanceUpdateRequestProxyPlacement:
    if value in PATCHED_LOADBALANCER_INSTANCE_UPDATE_REQUEST_PROXY_PLACEMENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_LOADBALANCER_INSTANCE_UPDATE_REQUEST_PROXY_PLACEMENT_VALUES!r}"
    )
