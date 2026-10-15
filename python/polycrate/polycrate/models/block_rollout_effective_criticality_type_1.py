from typing import Literal

BlockRolloutEffectiveCriticalityType1 = Literal["high", "low", "medium"]

BLOCK_ROLLOUT_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[BlockRolloutEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_block_rollout_effective_criticality_type_1(value: str) -> BlockRolloutEffectiveCriticalityType1:
    if value in BLOCK_ROLLOUT_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
