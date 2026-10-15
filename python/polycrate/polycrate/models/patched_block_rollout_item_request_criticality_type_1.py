from typing import Literal

PatchedBlockRolloutItemRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedBlockRolloutItemRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_block_rollout_item_request_criticality_type_1(
    value: str,
) -> PatchedBlockRolloutItemRequestCriticalityType1:
    if value in PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_ITEM_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
