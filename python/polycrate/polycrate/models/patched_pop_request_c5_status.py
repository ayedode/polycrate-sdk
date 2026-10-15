from typing import Literal

PatchedPopRequestC5Status = Literal["none", "planned", "typ1", "typ2"]

PATCHED_POP_REQUEST_C5_STATUS_VALUES: set[PatchedPopRequestC5Status] = {
    "none",
    "planned",
    "typ1",
    "typ2",
}


def check_patched_pop_request_c5_status(value: str) -> PatchedPopRequestC5Status:
    if value in PATCHED_POP_REQUEST_C5_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POP_REQUEST_C5_STATUS_VALUES!r}")
