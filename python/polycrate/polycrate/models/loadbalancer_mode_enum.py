from typing import Literal

LoadbalancerModeEnum = Literal["cluster", "external"]

LOADBALANCER_MODE_ENUM_VALUES: set[LoadbalancerModeEnum] = {
    "cluster",
    "external",
}


def check_loadbalancer_mode_enum(value: str) -> LoadbalancerModeEnum:
    if value in LOADBALANCER_MODE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_MODE_ENUM_VALUES!r}")
