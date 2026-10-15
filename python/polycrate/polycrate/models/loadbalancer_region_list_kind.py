from typing import Literal

LoadbalancerRegionListKind = Literal["cilium", "metallb"]

LOADBALANCER_REGION_LIST_KIND_VALUES: set[LoadbalancerRegionListKind] = {
    "cilium",
    "metallb",
}


def check_loadbalancer_region_list_kind(value: str) -> LoadbalancerRegionListKind:
    if value in LOADBALANCER_REGION_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_REGION_LIST_KIND_VALUES!r}")
