from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateTemplateBlockErrorComponentAttr = Literal["template_block"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateTemplateBlockErrorComponentAttr
] = {
    "template_block",
}


def check_api_v1_block_rollout_configs_archive_create_template_block_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateTemplateBlockErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
