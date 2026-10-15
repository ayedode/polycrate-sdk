from typing import Literal

PatchedPopRequestByoipStatus = Literal["no", "planned", "unknown", "yes"]

PATCHED_POP_REQUEST_BYOIP_STATUS_VALUES: set[PatchedPopRequestByoipStatus] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_patched_pop_request_byoip_status(value: str) -> PatchedPopRequestByoipStatus:
    if value in PATCHED_POP_REQUEST_BYOIP_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POP_REQUEST_BYOIP_STATUS_VALUES!r}")
