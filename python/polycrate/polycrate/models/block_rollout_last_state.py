from typing import Literal

BlockRolloutLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BLOCK_ROLLOUT_LAST_STATE_VALUES: set[BlockRolloutLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_block_rollout_last_state(value: str) -> BlockRolloutLastState:
    if value in BLOCK_ROLLOUT_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_LAST_STATE_VALUES!r}")
