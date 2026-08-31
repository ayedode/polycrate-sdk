from typing import Literal

ApiV1BlockRolloutsListKindItem = Literal["generic"]

API_V1_BLOCK_ROLLOUTS_LIST_KIND_ITEM_VALUES: set[ApiV1BlockRolloutsListKindItem] = {
    "generic",
}


def check_api_v1_block_rollouts_list_kind_item(value: str) -> ApiV1BlockRolloutsListKindItem:
    if value in API_V1_BLOCK_ROLLOUTS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_LIST_KIND_ITEM_VALUES!r}")
