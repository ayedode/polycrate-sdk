from typing import Literal

BlockRolloutConfigRequestTriggerTypeType1 = Literal["", "reconciliation", "schedule"]

BLOCK_ROLLOUT_CONFIG_REQUEST_TRIGGER_TYPE_TYPE_1_VALUES: set[BlockRolloutConfigRequestTriggerTypeType1] = {
    "",
    "reconciliation",
    "schedule",
}


def check_block_rollout_config_request_trigger_type_type_1(value: str) -> BlockRolloutConfigRequestTriggerTypeType1:
    if value in BLOCK_ROLLOUT_CONFIG_REQUEST_TRIGGER_TYPE_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_REQUEST_TRIGGER_TYPE_TYPE_1_VALUES!r}"
    )
