from typing import Literal

BlockRolloutConfigTriggerTypeType2Type1 = Literal["", "reconciliation", "schedule"]

BLOCK_ROLLOUT_CONFIG_TRIGGER_TYPE_TYPE_2_TYPE_1_VALUES: set[BlockRolloutConfigTriggerTypeType2Type1] = {
    "",
    "reconciliation",
    "schedule",
}


def check_block_rollout_config_trigger_type_type_2_type_1(value: str) -> BlockRolloutConfigTriggerTypeType2Type1:
    if value in BLOCK_ROLLOUT_CONFIG_TRIGGER_TYPE_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_TRIGGER_TYPE_TYPE_2_TYPE_1_VALUES!r}"
    )
