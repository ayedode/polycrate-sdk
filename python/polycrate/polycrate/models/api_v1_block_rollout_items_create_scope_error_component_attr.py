from typing import Literal

ApiV1BlockRolloutItemsCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_block_rollout_items_create_scope_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsCreateScopeErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
