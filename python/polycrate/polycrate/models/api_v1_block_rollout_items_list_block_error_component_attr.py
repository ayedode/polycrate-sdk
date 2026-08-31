from typing import Literal

ApiV1BlockRolloutItemsListBlockErrorComponentAttr = Literal["block"]

API_V1_BLOCK_ROLLOUT_ITEMS_LIST_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsListBlockErrorComponentAttr
] = {
    "block",
}


def check_api_v1_block_rollout_items_list_block_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsListBlockErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_LIST_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_LIST_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
