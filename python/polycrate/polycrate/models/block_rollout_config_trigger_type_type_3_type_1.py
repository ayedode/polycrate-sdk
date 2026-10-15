from typing import Literal

BlockRolloutConfigTriggerTypeType3Type1 = Literal["", "reconciliation", "schedule"]

BLOCK_ROLLOUT_CONFIG_TRIGGER_TYPE_TYPE_3_TYPE_1_VALUES: set[BlockRolloutConfigTriggerTypeType3Type1] = {
    "",
    "reconciliation",
    "schedule",
}


def check_block_rollout_config_trigger_type_type_3_type_1(value: str) -> BlockRolloutConfigTriggerTypeType3Type1:
    if value in BLOCK_ROLLOUT_CONFIG_TRIGGER_TYPE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_TRIGGER_TYPE_TYPE_3_TYPE_1_VALUES!r}"
    )
