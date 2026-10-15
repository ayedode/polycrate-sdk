from typing import Literal

LoadbalancerInstanceSessionAffinity = Literal["cookie", "ip", "none"]

LOADBALANCER_INSTANCE_SESSION_AFFINITY_VALUES: set[LoadbalancerInstanceSessionAffinity] = {
    "cookie",
    "ip",
    "none",
}


def check_loadbalancer_instance_session_affinity(value: str) -> LoadbalancerInstanceSessionAffinity:
    if value in LOADBALANCER_INSTANCE_SESSION_AFFINITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_SESSION_AFFINITY_VALUES!r}")
