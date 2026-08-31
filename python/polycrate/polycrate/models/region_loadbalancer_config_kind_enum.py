from typing import Literal

RegionLoadbalancerConfigKindEnum = Literal["cilium", "metallb"]

REGION_LOADBALANCER_CONFIG_KIND_ENUM_VALUES: set[RegionLoadbalancerConfigKindEnum] = {
    "cilium",
    "metallb",
}


def check_region_loadbalancer_config_kind_enum(value: str) -> RegionLoadbalancerConfigKindEnum:
    if value in REGION_LOADBALANCER_CONFIG_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_LOADBALANCER_CONFIG_KIND_ENUM_VALUES!r}")
