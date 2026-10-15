from typing import Literal

PatchedBlockRolloutItemRequestLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_LAST_STATE_VALUES: set[PatchedBlockRolloutItemRequestLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_patched_block_rollout_item_request_last_state(value: str) -> PatchedBlockRolloutItemRequestLastState:
    if value in PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_LAST_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_LAST_STATE_VALUES!r}"
    )
