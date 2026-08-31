from typing import Literal

ApiV1BlockRolloutConfigsUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_block_rollout_configs_update_scope_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateScopeErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
