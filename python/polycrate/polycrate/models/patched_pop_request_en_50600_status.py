from typing import Literal

PatchedPopRequestEn50600Status = Literal["no", "planned", "unknown", "yes"]

PATCHED_POP_REQUEST_EN_50600_STATUS_VALUES: set[PatchedPopRequestEn50600Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_patched_pop_request_en_50600_status(value: str) -> PatchedPopRequestEn50600Status:
    if value in PATCHED_POP_REQUEST_EN_50600_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POP_REQUEST_EN_50600_STATUS_VALUES!r}")
