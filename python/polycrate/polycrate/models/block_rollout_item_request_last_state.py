from typing import Literal

BlockRolloutItemRequestLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BLOCK_ROLLOUT_ITEM_REQUEST_LAST_STATE_VALUES: set[BlockRolloutItemRequestLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_block_rollout_item_request_last_state(value: str) -> BlockRolloutItemRequestLastState:
    if value in BLOCK_ROLLOUT_ITEM_REQUEST_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_REQUEST_LAST_STATE_VALUES!r}")
