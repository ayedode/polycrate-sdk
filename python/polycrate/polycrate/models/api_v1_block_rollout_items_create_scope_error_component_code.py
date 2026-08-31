from typing import Literal

ApiV1BlockRolloutItemsCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_block_rollout_items_create_scope_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsCreateScopeErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
