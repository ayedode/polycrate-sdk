from typing import Literal

BlockRolloutRequestStatus = Literal["active", "blocked", "cancelled", "completed", "paused"]

BLOCK_ROLLOUT_REQUEST_STATUS_VALUES: set[BlockRolloutRequestStatus] = {
    "active",
    "blocked",
    "cancelled",
    "completed",
    "paused",
}


def check_block_rollout_request_status(value: str) -> BlockRolloutRequestStatus:
    if value in BLOCK_ROLLOUT_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_REQUEST_STATUS_VALUES!r}")
