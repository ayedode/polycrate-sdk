from typing import Literal

BlockRolloutStatusEnum = Literal["active", "blocked", "cancelled", "completed", "paused"]

BLOCK_ROLLOUT_STATUS_ENUM_VALUES: set[BlockRolloutStatusEnum] = {
    "active",
    "blocked",
    "cancelled",
    "completed",
    "paused",
}


def check_block_rollout_status_enum(value: str) -> BlockRolloutStatusEnum:
    if value in BLOCK_ROLLOUT_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_STATUS_ENUM_VALUES!r}")
