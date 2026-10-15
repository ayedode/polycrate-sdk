from typing import Literal

BlockRolloutItemScope = Literal["system", "user"]

BLOCK_ROLLOUT_ITEM_SCOPE_VALUES: set[BlockRolloutItemScope] = {
    "system",
    "user",
}


def check_block_rollout_item_scope(value: str) -> BlockRolloutItemScope:
    if value in BLOCK_ROLLOUT_ITEM_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_SCOPE_VALUES!r}")
