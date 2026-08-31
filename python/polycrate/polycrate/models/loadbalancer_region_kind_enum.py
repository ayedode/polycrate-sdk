from typing import Literal

LoadbalancerRegionKindEnum = Literal["cilium", "metallb"]

LOADBALANCER_REGION_KIND_ENUM_VALUES: set[LoadbalancerRegionKindEnum] = {
    "cilium",
    "metallb",
}


def check_loadbalancer_region_kind_enum(value: str) -> LoadbalancerRegionKindEnum:
    if value in LOADBALANCER_REGION_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_REGION_KIND_ENUM_VALUES!r}")
