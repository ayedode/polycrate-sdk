from typing import Literal

ApiV1BlockRolloutConfigsUpdateTemplateBlockErrorComponentAttr = Literal["template_block"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateTemplateBlockErrorComponentAttr
] = {
    "template_block",
}


def check_api_v1_block_rollout_configs_update_template_block_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateTemplateBlockErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
