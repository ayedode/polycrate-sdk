from typing import Literal

ApiV1BlockRolloutConfigsCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollout_configs_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateDebugModeErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
