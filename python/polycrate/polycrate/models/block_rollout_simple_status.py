from typing import Literal

BlockRolloutSimpleStatus = Literal["active", "blocked", "cancelled", "completed", "paused"]

BLOCK_ROLLOUT_SIMPLE_STATUS_VALUES: set[BlockRolloutSimpleStatus] = {
    "active",
    "blocked",
    "cancelled",
    "completed",
    "paused",
}


def check_block_rollout_simple_status(value: str) -> BlockRolloutSimpleStatus:
    if value in BLOCK_ROLLOUT_SIMPLE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_SIMPLE_STATUS_VALUES!r}")
