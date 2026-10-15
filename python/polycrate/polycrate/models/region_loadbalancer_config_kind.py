from typing import Literal

RegionLoadbalancerConfigKind = Literal["cilium", "metallb"]

REGION_LOADBALANCER_CONFIG_KIND_VALUES: set[RegionLoadbalancerConfigKind] = {
    "cilium",
    "metallb",
}


def check_region_loadbalancer_config_kind(value: str) -> RegionLoadbalancerConfigKind:
    if value in REGION_LOADBALANCER_CONFIG_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_LOADBALANCER_CONFIG_KIND_VALUES!r}")
