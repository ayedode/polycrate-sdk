from typing import Literal

ApiV1BlockRolloutConfigsUpdateScopeExpressionsErrorComponentAttr = Literal["scope_expressions"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateScopeExpressionsErrorComponentAttr
] = {
    "scope_expressions",
}


def check_api_v1_block_rollout_configs_update_scope_expressions_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateScopeExpressionsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
