from typing import Literal

ApiV1BlockRolloutConfigsCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_block_rollout_configs_create_scope_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateScopeErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
