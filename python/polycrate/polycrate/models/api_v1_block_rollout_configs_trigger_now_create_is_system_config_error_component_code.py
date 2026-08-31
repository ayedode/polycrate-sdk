from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateIsSystemConfigErrorComponentCode = Literal["invalid", "null", "required"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_IS_SYSTEM_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateIsSystemConfigErrorComponentCode
] = {
    "invalid",
    "null",
    "required",
}


def check_api_v1_block_rollout_configs_trigger_now_create_is_system_config_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateIsSystemConfigErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_IS_SYSTEM_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_IS_SYSTEM_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
