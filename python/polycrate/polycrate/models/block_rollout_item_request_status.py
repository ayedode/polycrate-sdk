from typing import Literal

BlockRolloutItemRequestStatus = Literal["completed", "failed", "in_progress", "pending", "retrying", "skipped"]

BLOCK_ROLLOUT_ITEM_REQUEST_STATUS_VALUES: set[BlockRolloutItemRequestStatus] = {
    "completed",
    "failed",
    "in_progress",
    "pending",
    "retrying",
    "skipped",
}


def check_block_rollout_item_request_status(value: str) -> BlockRolloutItemRequestStatus:
    if value in BLOCK_ROLLOUT_ITEM_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_REQUEST_STATUS_VALUES!r}")
