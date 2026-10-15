from typing import Literal

LoadbalancerInstanceScope = Literal["system", "user"]

LOADBALANCER_INSTANCE_SCOPE_VALUES: set[LoadbalancerInstanceScope] = {
    "system",
    "user",
}


def check_loadbalancer_instance_scope(value: str) -> LoadbalancerInstanceScope:
    if value in LOADBALANCER_INSTANCE_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_SCOPE_VALUES!r}")
