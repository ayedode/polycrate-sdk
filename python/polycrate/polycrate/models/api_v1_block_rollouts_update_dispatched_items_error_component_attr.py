from typing import Literal

ApiV1BlockRolloutsUpdateDispatchedItemsErrorComponentAttr = Literal["dispatched_items"]

API_V1_BLOCK_ROLLOUTS_UPDATE_DISPATCHED_ITEMS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsUpdateDispatchedItemsErrorComponentAttr
] = {
    "dispatched_items",
}


def check_api_v1_block_rollouts_update_dispatched_items_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsUpdateDispatchedItemsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_DISPATCHED_ITEMS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_DISPATCHED_ITEMS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
