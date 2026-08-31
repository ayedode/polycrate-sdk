from typing import Literal

ApiV1BlockRolloutItemsListStateErrorComponentAttr = Literal["state"]

API_V1_BLOCK_ROLLOUT_ITEMS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_block_rollout_items_list_state_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsListStateErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
