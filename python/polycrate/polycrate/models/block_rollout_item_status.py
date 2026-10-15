from typing import Literal

BlockRolloutItemStatus = Literal["completed", "failed", "in_progress", "pending", "retrying", "skipped"]

BLOCK_ROLLOUT_ITEM_STATUS_VALUES: set[BlockRolloutItemStatus] = {
    "completed",
    "failed",
    "in_progress",
    "pending",
    "retrying",
    "skipped",
}


def check_block_rollout_item_status(value: str) -> BlockRolloutItemStatus:
    if value in BLOCK_ROLLOUT_ITEM_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_STATUS_VALUES!r}")
