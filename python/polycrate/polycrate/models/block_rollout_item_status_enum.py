from typing import Literal

BlockRolloutItemStatusEnum = Literal["completed", "failed", "in_progress", "pending", "retrying", "skipped"]

BLOCK_ROLLOUT_ITEM_STATUS_ENUM_VALUES: set[BlockRolloutItemStatusEnum] = {
    "completed",
    "failed",
    "in_progress",
    "pending",
    "retrying",
    "skipped",
}


def check_block_rollout_item_status_enum(value: str) -> BlockRolloutItemStatusEnum:
    if value in BLOCK_ROLLOUT_ITEM_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_STATUS_ENUM_VALUES!r}")
