from typing import Literal

BlockRolloutItemEffectiveCriticalityType1 = Literal["high", "low", "medium"]

BLOCK_ROLLOUT_ITEM_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[BlockRolloutItemEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_block_rollout_item_effective_criticality_type_1(value: str) -> BlockRolloutItemEffectiveCriticalityType1:
    if value in BLOCK_ROLLOUT_ITEM_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_ITEM_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
