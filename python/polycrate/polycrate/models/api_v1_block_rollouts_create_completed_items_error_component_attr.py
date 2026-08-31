from typing import Literal

ApiV1BlockRolloutsCreateCompletedItemsErrorComponentAttr = Literal["completed_items"]

API_V1_BLOCK_ROLLOUTS_CREATE_COMPLETED_ITEMS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsCreateCompletedItemsErrorComponentAttr
] = {
    "completed_items",
}


def check_api_v1_block_rollouts_create_completed_items_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateCompletedItemsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_COMPLETED_ITEMS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_COMPLETED_ITEMS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
