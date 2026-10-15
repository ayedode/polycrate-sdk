from typing import Literal

BlockRolloutConfigListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

BLOCK_ROLLOUT_CONFIG_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    BlockRolloutConfigListEffectiveCriticalityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_block_rollout_config_list_effective_criticality_type_2_type_1(
    value: str,
) -> BlockRolloutConfigListEffectiveCriticalityType2Type1:
    if value in BLOCK_ROLLOUT_CONFIG_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
