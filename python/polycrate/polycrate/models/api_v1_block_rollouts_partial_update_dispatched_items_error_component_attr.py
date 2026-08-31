from typing import Literal

ApiV1BlockRolloutsPartialUpdateDispatchedItemsErrorComponentAttr = Literal["dispatched_items"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_DISPATCHED_ITEMS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateDispatchedItemsErrorComponentAttr
] = {
    "dispatched_items",
}


def check_api_v1_block_rollouts_partial_update_dispatched_items_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateDispatchedItemsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_DISPATCHED_ITEMS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_DISPATCHED_ITEMS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
