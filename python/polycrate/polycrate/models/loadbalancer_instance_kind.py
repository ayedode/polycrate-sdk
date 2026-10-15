from typing import Literal

LoadbalancerInstanceKind = Literal["generic"]

LOADBALANCER_INSTANCE_KIND_VALUES: set[LoadbalancerInstanceKind] = {
    "generic",
}


def check_loadbalancer_instance_kind(value: str) -> LoadbalancerInstanceKind:
    if value in LOADBALANCER_INSTANCE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_KIND_VALUES!r}")
