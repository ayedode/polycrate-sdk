from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateIsSystemConfigErrorComponentAttr = Literal["is_system_config"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_IS_SYSTEM_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateIsSystemConfigErrorComponentAttr
] = {
    "is_system_config",
}


def check_api_v1_block_rollout_configs_archive_create_is_system_config_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateIsSystemConfigErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_IS_SYSTEM_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_IS_SYSTEM_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
