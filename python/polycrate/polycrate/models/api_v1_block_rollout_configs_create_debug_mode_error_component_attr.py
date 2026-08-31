from typing import Literal

ApiV1BlockRolloutConfigsCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_block_rollout_configs_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateDebugModeErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
