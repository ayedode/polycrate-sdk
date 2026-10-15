from typing import Literal

BlockRequestScope = Literal["system", "user"]

BLOCK_REQUEST_SCOPE_VALUES: set[BlockRequestScope] = {
    "system",
    "user",
}


def check_block_request_scope(value: str) -> BlockRequestScope:
    if value in BLOCK_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_REQUEST_SCOPE_VALUES!r}")
