from typing import Literal

BlockRolloutListStatus = Literal["active", "blocked", "cancelled", "completed", "paused"]

BLOCK_ROLLOUT_LIST_STATUS_VALUES: set[BlockRolloutListStatus] = {
    "active",
    "blocked",
    "cancelled",
    "completed",
    "paused",
}


def check_block_rollout_list_status(value: str) -> BlockRolloutListStatus:
    if value in BLOCK_ROLLOUT_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_LIST_STATUS_VALUES!r}")
