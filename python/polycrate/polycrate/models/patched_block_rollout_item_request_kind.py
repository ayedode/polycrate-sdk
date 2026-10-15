from typing import Literal

PatchedBlockRolloutItemRequestKind = Literal["generic"]

PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_KIND_VALUES: set[PatchedBlockRolloutItemRequestKind] = {
    "generic",
}


def check_patched_block_rollout_item_request_kind(value: str) -> PatchedBlockRolloutItemRequestKind:
    if value in PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_KIND_VALUES!r}")
