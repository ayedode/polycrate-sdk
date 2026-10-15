from typing import Literal

BlockRolloutCriticalityType3Type1 = Literal["", "high", "low", "medium"]

BLOCK_ROLLOUT_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[BlockRolloutCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_block_rollout_criticality_type_3_type_1(value: str) -> BlockRolloutCriticalityType3Type1:
    if value in BLOCK_ROLLOUT_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
