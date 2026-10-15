from typing import Literal

BlockRolloutConfigListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

BLOCK_ROLLOUT_CONFIG_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[BlockRolloutConfigListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_block_rollout_config_list_effective_criticality_type_1(
    value: str,
) -> BlockRolloutConfigListEffectiveCriticalityType1:
    if value in BLOCK_ROLLOUT_CONFIG_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
