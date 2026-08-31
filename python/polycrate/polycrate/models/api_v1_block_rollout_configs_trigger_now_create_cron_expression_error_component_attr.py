from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateCronExpressionErrorComponentAttr = Literal["cron_expression"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_CRON_EXPRESSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateCronExpressionErrorComponentAttr
] = {
    "cron_expression",
}


def check_api_v1_block_rollout_configs_trigger_now_create_cron_expression_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateCronExpressionErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_CRON_EXPRESSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_CRON_EXPRESSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
