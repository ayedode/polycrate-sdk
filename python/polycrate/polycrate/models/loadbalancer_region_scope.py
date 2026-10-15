from typing import Literal

LoadbalancerRegionScope = Literal["system", "user"]

LOADBALANCER_REGION_SCOPE_VALUES: set[LoadbalancerRegionScope] = {
    "system",
    "user",
}


def check_loadbalancer_region_scope(value: str) -> LoadbalancerRegionScope:
    if value in LOADBALANCER_REGION_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_REGION_SCOPE_VALUES!r}")
