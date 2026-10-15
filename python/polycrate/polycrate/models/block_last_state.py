from typing import Literal

BlockLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BLOCK_LAST_STATE_VALUES: set[BlockLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_block_last_state(value: str) -> BlockLastState:
    if value in BLOCK_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_LAST_STATE_VALUES!r}")
