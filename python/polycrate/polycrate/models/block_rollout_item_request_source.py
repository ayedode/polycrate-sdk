from typing import Literal

BlockRolloutItemRequestSource = Literal["manual", "scheduler"]

BLOCK_ROLLOUT_ITEM_REQUEST_SOURCE_VALUES: set[BlockRolloutItemRequestSource] = {
    "manual",
    "scheduler",
}


def check_block_rollout_item_request_source(value: str) -> BlockRolloutItemRequestSource:
    if value in BLOCK_ROLLOUT_ITEM_REQUEST_SOURCE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_REQUEST_SOURCE_VALUES!r}")
