from typing import Literal

BlockRolloutItemCriticalityType1 = Literal["", "high", "low", "medium"]

BLOCK_ROLLOUT_ITEM_CRITICALITY_TYPE_1_VALUES: set[BlockRolloutItemCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_block_rollout_item_criticality_type_1(value: str) -> BlockRolloutItemCriticalityType1:
    if value in BLOCK_ROLLOUT_ITEM_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_CRITICALITY_TYPE_1_VALUES!r}")
