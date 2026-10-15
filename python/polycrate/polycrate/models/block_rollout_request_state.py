from typing import Literal

BlockRolloutRequestState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BLOCK_ROLLOUT_REQUEST_STATE_VALUES: set[BlockRolloutRequestState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_block_rollout_request_state(value: str) -> BlockRolloutRequestState:
    if value in BLOCK_ROLLOUT_REQUEST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_REQUEST_STATE_VALUES!r}")
