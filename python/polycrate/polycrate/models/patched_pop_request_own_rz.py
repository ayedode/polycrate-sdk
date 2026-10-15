from typing import Literal

PatchedPopRequestOwnRz = Literal["no", "planned", "unknown", "yes"]

PATCHED_POP_REQUEST_OWN_RZ_VALUES: set[PatchedPopRequestOwnRz] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_patched_pop_request_own_rz(value: str) -> PatchedPopRequestOwnRz:
    if value in PATCHED_POP_REQUEST_OWN_RZ_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POP_REQUEST_OWN_RZ_VALUES!r}")
