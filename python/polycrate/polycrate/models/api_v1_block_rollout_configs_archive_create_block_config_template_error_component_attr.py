from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateBlockConfigTemplateErrorComponentAttr = Literal["block_config_template"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateBlockConfigTemplateErrorComponentAttr
] = {
    "block_config_template",
}


def check_api_v1_block_rollout_configs_archive_create_block_config_template_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateBlockConfigTemplateErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
