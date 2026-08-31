from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateCronExpressionErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_CRON_EXPRESSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateCronExpressionErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_block_rollout_configs_trigger_now_create_cron_expression_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateCronExpressionErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_CRON_EXPRESSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_CRON_EXPRESSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
