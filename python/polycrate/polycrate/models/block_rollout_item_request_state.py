from typing import Literal

BlockRolloutItemRequestState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BLOCK_ROLLOUT_ITEM_REQUEST_STATE_VALUES: set[BlockRolloutItemRequestState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_block_rollout_item_request_state(value: str) -> BlockRolloutItemRequestState:
    if value in BLOCK_ROLLOUT_ITEM_REQUEST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_REQUEST_STATE_VALUES!r}")
