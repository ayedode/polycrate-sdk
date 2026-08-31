from typing import Literal

ApiV1BlockRolloutItemsListRolloutErrorComponentAttr = Literal["rollout"]

API_V1_BLOCK_ROLLOUT_ITEMS_LIST_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsListRolloutErrorComponentAttr
] = {
    "rollout",
}


def check_api_v1_block_rollout_items_list_rollout_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsListRolloutErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_LIST_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_LIST_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
