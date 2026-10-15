from typing import Literal

PopRequestPublicIpv4Status = Literal["no", "planned", "unknown", "yes"]

POP_REQUEST_PUBLIC_IPV_4_STATUS_VALUES: set[PopRequestPublicIpv4Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_request_public_ipv_4_status(value: str) -> PopRequestPublicIpv4Status:
    if value in POP_REQUEST_PUBLIC_IPV_4_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_REQUEST_PUBLIC_IPV_4_STATUS_VALUES!r}")
