from typing import Literal

PatchedPopRequestIpv6Status = Literal["no", "planned", "unknown", "yes"]

PATCHED_POP_REQUEST_IPV_6_STATUS_VALUES: set[PatchedPopRequestIpv6Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_patched_pop_request_ipv_6_status(value: str) -> PatchedPopRequestIpv6Status:
    if value in PATCHED_POP_REQUEST_IPV_6_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POP_REQUEST_IPV_6_STATUS_VALUES!r}")
