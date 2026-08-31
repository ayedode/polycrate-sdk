from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollout_configs_trigger_now_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateDebugModeErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
