from typing import Literal

BlockRolloutItemListSource = Literal["manual", "scheduler"]

BLOCK_ROLLOUT_ITEM_LIST_SOURCE_VALUES: set[BlockRolloutItemListSource] = {
    "manual",
    "scheduler",
}


def check_block_rollout_item_list_source(value: str) -> BlockRolloutItemListSource:
    if value in BLOCK_ROLLOUT_ITEM_LIST_SOURCE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_LIST_SOURCE_VALUES!r}")
