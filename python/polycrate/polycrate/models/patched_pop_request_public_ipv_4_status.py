from typing import Literal

PatchedPopRequestPublicIpv4Status = Literal["no", "planned", "unknown", "yes"]

PATCHED_POP_REQUEST_PUBLIC_IPV_4_STATUS_VALUES: set[PatchedPopRequestPublicIpv4Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_patched_pop_request_public_ipv_4_status(value: str) -> PatchedPopRequestPublicIpv4Status:
    if value in PATCHED_POP_REQUEST_PUBLIC_IPV_4_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POP_REQUEST_PUBLIC_IPV_4_STATUS_VALUES!r}")
