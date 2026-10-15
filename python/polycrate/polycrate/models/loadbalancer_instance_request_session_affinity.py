from typing import Literal

LoadbalancerInstanceRequestSessionAffinity = Literal["cookie", "ip", "none"]

LOADBALANCER_INSTANCE_REQUEST_SESSION_AFFINITY_VALUES: set[LoadbalancerInstanceRequestSessionAffinity] = {
    "cookie",
    "ip",
    "none",
}


def check_loadbalancer_instance_request_session_affinity(value: str) -> LoadbalancerInstanceRequestSessionAffinity:
    if value in LOADBALANCER_INSTANCE_REQUEST_SESSION_AFFINITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_REQUEST_SESSION_AFFINITY_VALUES!r}"
    )
