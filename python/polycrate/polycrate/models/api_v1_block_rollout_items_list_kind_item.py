from typing import Literal

ApiV1BlockRolloutItemsListKindItem = Literal["generic"]

API_V1_BLOCK_ROLLOUT_ITEMS_LIST_KIND_ITEM_VALUES: set[ApiV1BlockRolloutItemsListKindItem] = {
    "generic",
}


def check_api_v1_block_rollout_items_list_kind_item(value: str) -> ApiV1BlockRolloutItemsListKindItem:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_LIST_KIND_ITEM_VALUES!r}")
