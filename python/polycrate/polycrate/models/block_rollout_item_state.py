from typing import Literal

BlockRolloutItemState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BLOCK_ROLLOUT_ITEM_STATE_VALUES: set[BlockRolloutItemState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_block_rollout_item_state(value: str) -> BlockRolloutItemState:
    if value in BLOCK_ROLLOUT_ITEM_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_STATE_VALUES!r}")
