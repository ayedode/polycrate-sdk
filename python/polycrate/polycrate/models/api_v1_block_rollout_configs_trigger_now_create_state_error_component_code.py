from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateStateErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateStateErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_block_rollout_configs_trigger_now_create_state_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateStateErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
