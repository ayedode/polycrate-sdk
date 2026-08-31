from typing import Literal

ApiV1BlockRolloutItemsListKindErrorComponentCode = Literal["invalid_choice", "invalid_list"]

API_V1_BLOCK_ROLLOUT_ITEMS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsListKindErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
}


def check_api_v1_block_rollout_items_list_kind_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsListKindErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
