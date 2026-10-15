from typing import Literal

PatchedBlockRolloutItemRequestScope = Literal["system", "user"]

PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_SCOPE_VALUES: set[PatchedBlockRolloutItemRequestScope] = {
    "system",
    "user",
}


def check_patched_block_rollout_item_request_scope(value: str) -> PatchedBlockRolloutItemRequestScope:
    if value in PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_SCOPE_VALUES!r}")
