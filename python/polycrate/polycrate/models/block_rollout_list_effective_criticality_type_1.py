from typing import Literal

BlockRolloutListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

BLOCK_ROLLOUT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[BlockRolloutListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_block_rollout_list_effective_criticality_type_1(value: str) -> BlockRolloutListEffectiveCriticalityType1:
    if value in BLOCK_ROLLOUT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
