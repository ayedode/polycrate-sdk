from typing import Literal

ApiV1BlockRolloutItemsListSearchErrorComponentAttr = Literal["search"]

API_V1_BLOCK_ROLLOUT_ITEMS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_block_rollout_items_list_search_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsListSearchErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
