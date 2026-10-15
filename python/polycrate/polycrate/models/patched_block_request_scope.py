from typing import Literal

PatchedBlockRequestScope = Literal["system", "user"]

PATCHED_BLOCK_REQUEST_SCOPE_VALUES: set[PatchedBlockRequestScope] = {
    "system",
    "user",
}


def check_patched_block_request_scope(value: str) -> PatchedBlockRequestScope:
    if value in PATCHED_BLOCK_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_REQUEST_SCOPE_VALUES!r}")
