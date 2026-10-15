from typing import Literal

PatchedBlockRolloutRequestLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PATCHED_BLOCK_ROLLOUT_REQUEST_LAST_STATE_VALUES: set[PatchedBlockRolloutRequestLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_patched_block_rollout_request_last_state(value: str) -> PatchedBlockRolloutRequestLastState:
    if value in PATCHED_BLOCK_ROLLOUT_REQUEST_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_REQUEST_LAST_STATE_VALUES!r}")
