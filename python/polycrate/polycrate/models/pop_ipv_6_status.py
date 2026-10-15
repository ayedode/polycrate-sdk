from typing import Literal

PopIpv6Status = Literal["no", "planned", "unknown", "yes"]

POP_IPV_6_STATUS_VALUES: set[PopIpv6Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_ipv_6_status(value: str) -> PopIpv6Status:
    if value in POP_IPV_6_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_IPV_6_STATUS_VALUES!r}")
