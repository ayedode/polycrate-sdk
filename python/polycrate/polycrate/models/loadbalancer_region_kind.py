from typing import Literal

LoadbalancerRegionKind = Literal["cilium", "metallb"]

LOADBALANCER_REGION_KIND_VALUES: set[LoadbalancerRegionKind] = {
    "cilium",
    "metallb",
}


def check_loadbalancer_region_kind(value: str) -> LoadbalancerRegionKind:
    if value in LOADBALANCER_REGION_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_REGION_KIND_VALUES!r}")
