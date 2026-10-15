from typing import Literal

BlockRolloutItemSource = Literal["manual", "scheduler"]

BLOCK_ROLLOUT_ITEM_SOURCE_VALUES: set[BlockRolloutItemSource] = {
    "manual",
    "scheduler",
}


def check_block_rollout_item_source(value: str) -> BlockRolloutItemSource:
    if value in BLOCK_ROLLOUT_ITEM_SOURCE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_SOURCE_VALUES!r}")
