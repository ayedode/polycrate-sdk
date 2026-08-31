from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateBlockConfigTemplateErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateBlockConfigTemplateErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_block_rollout_configs_partial_update_block_config_template_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateBlockConfigTemplateErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
