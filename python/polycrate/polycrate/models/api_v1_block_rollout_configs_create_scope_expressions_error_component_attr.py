from typing import Literal

ApiV1BlockRolloutConfigsCreateScopeExpressionsErrorComponentAttr = Literal["scope_expressions"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateScopeExpressionsErrorComponentAttr
] = {
    "scope_expressions",
}


def check_api_v1_block_rollout_configs_create_scope_expressions_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateScopeExpressionsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
