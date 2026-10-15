from typing import Literal

BlockRolloutItemRequestCriticalityType1 = Literal["", "high", "low", "medium"]

BLOCK_ROLLOUT_ITEM_REQUEST_CRITICALITY_TYPE_1_VALUES: set[BlockRolloutItemRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_block_rollout_item_request_criticality_type_1(value: str) -> BlockRolloutItemRequestCriticalityType1:
    if value in BLOCK_ROLLOUT_ITEM_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
