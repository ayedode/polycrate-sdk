from typing import Literal

LoadbalancerInstanceRequestKind = Literal["generic"]

LOADBALANCER_INSTANCE_REQUEST_KIND_VALUES: set[LoadbalancerInstanceRequestKind] = {
    "generic",
}


def check_loadbalancer_instance_request_kind(value: str) -> LoadbalancerInstanceRequestKind:
    if value in LOADBALANCER_INSTANCE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_REQUEST_KIND_VALUES!r}")
