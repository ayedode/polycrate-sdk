from typing import Literal

BlockListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BLOCK_LIST_STATE_VALUES: set[BlockListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_block_list_state(value: str) -> BlockListState:
    if value in BLOCK_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_LIST_STATE_VALUES!r}")
