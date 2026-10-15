from typing import Literal

PatchedBlockRolloutConfigRequestTriggerTypeType1 = Literal["", "reconciliation", "schedule"]

PATCHED_BLOCK_ROLLOUT_CONFIG_REQUEST_TRIGGER_TYPE_TYPE_1_VALUES: set[
    PatchedBlockRolloutConfigRequestTriggerTypeType1
] = {
    "",
    "reconciliation",
    "schedule",
}


def check_patched_block_rollout_config_request_trigger_type_type_1(
    value: str,
) -> PatchedBlockRolloutConfigRequestTriggerTypeType1:
    if value in PATCHED_BLOCK_ROLLOUT_CONFIG_REQUEST_TRIGGER_TYPE_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_CONFIG_REQUEST_TRIGGER_TYPE_TYPE_1_VALUES!r}"
    )
