from typing import Literal

PatchedBlockRolloutItemRequestSource = Literal["manual", "scheduler"]

PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_SOURCE_VALUES: set[PatchedBlockRolloutItemRequestSource] = {
    "manual",
    "scheduler",
}


def check_patched_block_rollout_item_request_source(value: str) -> PatchedBlockRolloutItemRequestSource:
    if value in PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_SOURCE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_SOURCE_VALUES!r}")
