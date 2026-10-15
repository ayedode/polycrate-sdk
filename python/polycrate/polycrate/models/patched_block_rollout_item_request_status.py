from typing import Literal

PatchedBlockRolloutItemRequestStatus = Literal["completed", "failed", "in_progress", "pending", "retrying", "skipped"]

PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_STATUS_VALUES: set[PatchedBlockRolloutItemRequestStatus] = {
    "completed",
    "failed",
    "in_progress",
    "pending",
    "retrying",
    "skipped",
}


def check_patched_block_rollout_item_request_status(value: str) -> PatchedBlockRolloutItemRequestStatus:
    if value in PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_STATUS_VALUES!r}")
