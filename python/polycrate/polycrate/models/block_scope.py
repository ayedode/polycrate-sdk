from typing import Literal

BlockScope = Literal["system", "user"]

BLOCK_SCOPE_VALUES: set[BlockScope] = {
    "system",
    "user",
}


def check_block_scope(value: str) -> BlockScope:
    if value in BLOCK_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_SCOPE_VALUES!r}")
