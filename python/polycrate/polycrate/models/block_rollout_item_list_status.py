from typing import Literal

BlockRolloutItemListStatus = Literal["completed", "failed", "in_progress", "pending", "retrying", "skipped"]

BLOCK_ROLLOUT_ITEM_LIST_STATUS_VALUES: set[BlockRolloutItemListStatus] = {
    "completed",
    "failed",
    "in_progress",
    "pending",
    "retrying",
    "skipped",
}


def check_block_rollout_item_list_status(value: str) -> BlockRolloutItemListStatus:
    if value in BLOCK_ROLLOUT_ITEM_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_LIST_STATUS_VALUES!r}")
