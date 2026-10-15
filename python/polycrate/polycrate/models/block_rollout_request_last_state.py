from typing import Literal

BlockRolloutRequestLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BLOCK_ROLLOUT_REQUEST_LAST_STATE_VALUES: set[BlockRolloutRequestLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_block_rollout_request_last_state(value: str) -> BlockRolloutRequestLastState:
    if value in BLOCK_ROLLOUT_REQUEST_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_REQUEST_LAST_STATE_VALUES!r}")
