from typing import Literal

BlockRolloutConfigCriticalityType1 = Literal["", "high", "low", "medium"]

BLOCK_ROLLOUT_CONFIG_CRITICALITY_TYPE_1_VALUES: set[BlockRolloutConfigCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_block_rollout_config_criticality_type_1(value: str) -> BlockRolloutConfigCriticalityType1:
    if value in BLOCK_ROLLOUT_CONFIG_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_CRITICALITY_TYPE_1_VALUES!r}")
