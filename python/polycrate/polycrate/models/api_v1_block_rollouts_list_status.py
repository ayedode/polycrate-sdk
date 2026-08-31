from typing import Literal

ApiV1BlockRolloutsListStatus = Literal["active", "blocked", "cancelled", "completed", "paused"]

API_V1_BLOCK_ROLLOUTS_LIST_STATUS_VALUES: set[ApiV1BlockRolloutsListStatus] = {
    "active",
    "blocked",
    "cancelled",
    "completed",
    "paused",
}


def check_api_v1_block_rollouts_list_status(value: str) -> ApiV1BlockRolloutsListStatus:
    if value in API_V1_BLOCK_ROLLOUTS_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_LIST_STATUS_VALUES!r}")
