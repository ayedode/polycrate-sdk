from typing import Literal

BlockRolloutItemListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BLOCK_ROLLOUT_ITEM_LIST_STATE_VALUES: set[BlockRolloutItemListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_block_rollout_item_list_state(value: str) -> BlockRolloutItemListState:
    if value in BLOCK_ROLLOUT_ITEM_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_LIST_STATE_VALUES!r}")
