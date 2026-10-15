from typing import Literal

PatchedPopRequestIso27001Status = Literal["no", "planned", "unknown", "yes"]

PATCHED_POP_REQUEST_ISO_27001_STATUS_VALUES: set[PatchedPopRequestIso27001Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_patched_pop_request_iso_27001_status(value: str) -> PatchedPopRequestIso27001Status:
    if value in PATCHED_POP_REQUEST_ISO_27001_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POP_REQUEST_ISO_27001_STATUS_VALUES!r}")
