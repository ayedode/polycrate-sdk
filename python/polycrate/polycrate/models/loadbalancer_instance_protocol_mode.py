from typing import Literal

LoadbalancerInstanceProtocolMode = Literal["http", "tcp"]

LOADBALANCER_INSTANCE_PROTOCOL_MODE_VALUES: set[LoadbalancerInstanceProtocolMode] = {
    "http",
    "tcp",
}


def check_loadbalancer_instance_protocol_mode(value: str) -> LoadbalancerInstanceProtocolMode:
    if value in LOADBALANCER_INSTANCE_PROTOCOL_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_PROTOCOL_MODE_VALUES!r}")
