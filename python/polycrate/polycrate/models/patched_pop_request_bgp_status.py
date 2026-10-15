from typing import Literal

PatchedPopRequestBgpStatus = Literal["no", "planned", "unknown", "yes"]

PATCHED_POP_REQUEST_BGP_STATUS_VALUES: set[PatchedPopRequestBgpStatus] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_patched_pop_request_bgp_status(value: str) -> PatchedPopRequestBgpStatus:
    if value in PATCHED_POP_REQUEST_BGP_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POP_REQUEST_BGP_STATUS_VALUES!r}")
