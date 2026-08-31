from typing import Literal

ApiV1BlockRolloutItemsListRolloutErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_BLOCK_ROLLOUT_ITEMS_LIST_ROLLOUT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsListRolloutErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_block_rollout_items_list_rollout_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsListRolloutErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_LIST_ROLLOUT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_LIST_ROLLOUT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
