from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateBlockConfigTemplateErrorComponentAttr = Literal["block_config_template"]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateBlockConfigTemplateErrorComponentAttr
] = {
    "block_config_template",
}


def check_api_v1_block_rollout_configs_partial_update_block_config_template_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateBlockConfigTemplateErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
