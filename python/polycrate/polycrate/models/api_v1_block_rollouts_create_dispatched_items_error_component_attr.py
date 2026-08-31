from typing import Literal

ApiV1BlockRolloutsCreateDispatchedItemsErrorComponentAttr = Literal["dispatched_items"]

API_V1_BLOCK_ROLLOUTS_CREATE_DISPATCHED_ITEMS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsCreateDispatchedItemsErrorComponentAttr
] = {
    "dispatched_items",
}


def check_api_v1_block_rollouts_create_dispatched_items_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateDispatchedItemsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_DISPATCHED_ITEMS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_DISPATCHED_ITEMS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
