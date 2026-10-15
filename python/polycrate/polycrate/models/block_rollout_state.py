from typing import Literal

BlockRolloutState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BLOCK_ROLLOUT_STATE_VALUES: set[BlockRolloutState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_block_rollout_state(value: str) -> BlockRolloutState:
    if value in BLOCK_ROLLOUT_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_STATE_VALUES!r}")
