from typing import Literal

ApiV1BlockRolloutItemsListKindErrorComponentAttr = Literal["kind"]

API_V1_BLOCK_ROLLOUT_ITEMS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_block_rollout_items_list_kind_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsListKindErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
