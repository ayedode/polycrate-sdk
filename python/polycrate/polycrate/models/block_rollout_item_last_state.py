from typing import Literal

BlockRolloutItemLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BLOCK_ROLLOUT_ITEM_LAST_STATE_VALUES: set[BlockRolloutItemLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_block_rollout_item_last_state(value: str) -> BlockRolloutItemLastState:
    if value in BLOCK_ROLLOUT_ITEM_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_LAST_STATE_VALUES!r}")
