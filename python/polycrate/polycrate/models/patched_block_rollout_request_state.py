from typing import Literal

PatchedBlockRolloutRequestState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PATCHED_BLOCK_ROLLOUT_REQUEST_STATE_VALUES: set[PatchedBlockRolloutRequestState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_patched_block_rollout_request_state(value: str) -> PatchedBlockRolloutRequestState:
    if value in PATCHED_BLOCK_ROLLOUT_REQUEST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_REQUEST_STATE_VALUES!r}")
