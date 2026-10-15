from typing import Literal

RegionLoadbalancerConfigRequestKind = Literal["cilium", "metallb"]

REGION_LOADBALANCER_CONFIG_REQUEST_KIND_VALUES: set[RegionLoadbalancerConfigRequestKind] = {
    "cilium",
    "metallb",
}


def check_region_loadbalancer_config_request_kind(value: str) -> RegionLoadbalancerConfigRequestKind:
    if value in REGION_LOADBALANCER_CONFIG_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_LOADBALANCER_CONFIG_REQUEST_KIND_VALUES!r}")
