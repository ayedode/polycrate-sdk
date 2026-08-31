from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateIsSystemConfigErrorComponentCode = Literal["invalid", "null", "required"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_IS_SYSTEM_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateIsSystemConfigErrorComponentCode
] = {
    "invalid",
    "null",
    "required",
}


def check_api_v1_block_rollout_configs_archive_create_is_system_config_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateIsSystemConfigErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_IS_SYSTEM_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_IS_SYSTEM_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
