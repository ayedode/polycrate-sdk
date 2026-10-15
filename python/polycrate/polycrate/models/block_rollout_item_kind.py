from typing import Literal

BlockRolloutItemKind = Literal["generic"]

BLOCK_ROLLOUT_ITEM_KIND_VALUES: set[BlockRolloutItemKind] = {
    "generic",
}


def check_block_rollout_item_kind(value: str) -> BlockRolloutItemKind:
    if value in BLOCK_ROLLOUT_ITEM_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_KIND_VALUES!r}")
