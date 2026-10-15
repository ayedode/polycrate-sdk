from typing import Literal

PatchedBlockRolloutRequestStatus = Literal["active", "blocked", "cancelled", "completed", "paused"]

PATCHED_BLOCK_ROLLOUT_REQUEST_STATUS_VALUES: set[PatchedBlockRolloutRequestStatus] = {
    "active",
    "blocked",
    "cancelled",
    "completed",
    "paused",
}


def check_patched_block_rollout_request_status(value: str) -> PatchedBlockRolloutRequestStatus:
    if value in PATCHED_BLOCK_ROLLOUT_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_REQUEST_STATUS_VALUES!r}")
