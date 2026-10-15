from typing import Literal

PatchedPopRequestColocation = Literal["no", "planned", "unknown", "yes"]

PATCHED_POP_REQUEST_COLOCATION_VALUES: set[PatchedPopRequestColocation] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_patched_pop_request_colocation(value: str) -> PatchedPopRequestColocation:
    if value in PATCHED_POP_REQUEST_COLOCATION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POP_REQUEST_COLOCATION_VALUES!r}")
