from typing import Literal

BlockRolloutItemRequestScope = Literal["system", "user"]

BLOCK_ROLLOUT_ITEM_REQUEST_SCOPE_VALUES: set[BlockRolloutItemRequestScope] = {
    "system",
    "user",
}


def check_block_rollout_item_request_scope(value: str) -> BlockRolloutItemRequestScope:
    if value in BLOCK_ROLLOUT_ITEM_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_REQUEST_SCOPE_VALUES!r}")
