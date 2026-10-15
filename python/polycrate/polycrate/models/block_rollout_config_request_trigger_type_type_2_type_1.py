from typing import Literal

BlockRolloutConfigRequestTriggerTypeType2Type1 = Literal["", "reconciliation", "schedule"]

BLOCK_ROLLOUT_CONFIG_REQUEST_TRIGGER_TYPE_TYPE_2_TYPE_1_VALUES: set[BlockRolloutConfigRequestTriggerTypeType2Type1] = {
    "",
    "reconciliation",
    "schedule",
}


def check_block_rollout_config_request_trigger_type_type_2_type_1(
    value: str,
) -> BlockRolloutConfigRequestTriggerTypeType2Type1:
    if value in BLOCK_ROLLOUT_CONFIG_REQUEST_TRIGGER_TYPE_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_REQUEST_TRIGGER_TYPE_TYPE_2_TYPE_1_VALUES!r}"
    )
