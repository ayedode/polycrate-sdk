from typing import Literal

BlockRolloutStatus = Literal["active", "blocked", "cancelled", "completed", "paused"]

BLOCK_ROLLOUT_STATUS_VALUES: set[BlockRolloutStatus] = {
    "active",
    "blocked",
    "cancelled",
    "completed",
    "paused",
}


def check_block_rollout_status(value: str) -> BlockRolloutStatus:
    if value in BLOCK_ROLLOUT_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_STATUS_VALUES!r}")
