from typing import Literal

LoadbalancerRegionRequestKind = Literal["cilium", "metallb"]

LOADBALANCER_REGION_REQUEST_KIND_VALUES: set[LoadbalancerRegionRequestKind] = {
    "cilium",
    "metallb",
}


def check_loadbalancer_region_request_kind(value: str) -> LoadbalancerRegionRequestKind:
    if value in LOADBALANCER_REGION_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_REGION_REQUEST_KIND_VALUES!r}")
