from typing import Literal

BlockRolloutItemRequestKind = Literal["generic"]

BLOCK_ROLLOUT_ITEM_REQUEST_KIND_VALUES: set[BlockRolloutItemRequestKind] = {
    "generic",
}


def check_block_rollout_item_request_kind(value: str) -> BlockRolloutItemRequestKind:
    if value in BLOCK_ROLLOUT_ITEM_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_REQUEST_KIND_VALUES!r}")
