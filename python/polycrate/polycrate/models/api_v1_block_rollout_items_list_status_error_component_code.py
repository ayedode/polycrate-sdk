from typing import Literal

ApiV1BlockRolloutItemsListStatusErrorComponentCode = Literal["invalid_choice"]

API_V1_BLOCK_ROLLOUT_ITEMS_LIST_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsListStatusErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_block_rollout_items_list_status_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsListStatusErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_LIST_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_LIST_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
