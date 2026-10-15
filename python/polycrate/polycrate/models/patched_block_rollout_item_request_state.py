from typing import Literal

PatchedBlockRolloutItemRequestState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_STATE_VALUES: set[PatchedBlockRolloutItemRequestState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_patched_block_rollout_item_request_state(value: str) -> PatchedBlockRolloutItemRequestState:
    if value in PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_STATE_VALUES!r}")
