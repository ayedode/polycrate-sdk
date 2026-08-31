from typing import Literal

ApiV1BlockRolloutConfigsUpdateIsSystemConfigErrorComponentCode = Literal["invalid", "null", "required"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_IS_SYSTEM_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateIsSystemConfigErrorComponentCode
] = {
    "invalid",
    "null",
    "required",
}


def check_api_v1_block_rollout_configs_update_is_system_config_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateIsSystemConfigErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_IS_SYSTEM_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_IS_SYSTEM_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
