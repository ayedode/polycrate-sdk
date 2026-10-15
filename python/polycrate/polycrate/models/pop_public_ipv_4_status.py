from typing import Literal

PopPublicIpv4Status = Literal["no", "planned", "unknown", "yes"]

POP_PUBLIC_IPV_4_STATUS_VALUES: set[PopPublicIpv4Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_public_ipv_4_status(value: str) -> PopPublicIpv4Status:
    if value in POP_PUBLIC_IPV_4_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_PUBLIC_IPV_4_STATUS_VALUES!r}")
