from typing import Literal

ApiV1BlockRolloutItemsListStatus = Literal["completed", "failed", "in_progress", "pending", "retrying", "skipped"]

API_V1_BLOCK_ROLLOUT_ITEMS_LIST_STATUS_VALUES: set[ApiV1BlockRolloutItemsListStatus] = {
    "completed",
    "failed",
    "in_progress",
    "pending",
    "retrying",
    "skipped",
}


def check_api_v1_block_rollout_items_list_status(value: str) -> ApiV1BlockRolloutItemsListStatus:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_LIST_STATUS_VALUES!r}")
