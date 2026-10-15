from typing import Literal

BlockRolloutEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

BLOCK_ROLLOUT_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[BlockRolloutEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_block_rollout_effective_criticality_type_2_type_1(value: str) -> BlockRolloutEffectiveCriticalityType2Type1:
    if value in BLOCK_ROLLOUT_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
