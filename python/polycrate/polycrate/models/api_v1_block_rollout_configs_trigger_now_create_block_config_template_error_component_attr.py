from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateBlockConfigTemplateErrorComponentAttr = Literal["block_config_template"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateBlockConfigTemplateErrorComponentAttr
] = {
    "block_config_template",
}


def check_api_v1_block_rollout_configs_trigger_now_create_block_config_template_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateBlockConfigTemplateErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
