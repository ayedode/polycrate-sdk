from typing import Literal

PopRequestIpv6Status = Literal["no", "planned", "unknown", "yes"]

POP_REQUEST_IPV_6_STATUS_VALUES: set[PopRequestIpv6Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_request_ipv_6_status(value: str) -> PopRequestIpv6Status:
    if value in POP_REQUEST_IPV_6_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_REQUEST_IPV_6_STATUS_VALUES!r}")
