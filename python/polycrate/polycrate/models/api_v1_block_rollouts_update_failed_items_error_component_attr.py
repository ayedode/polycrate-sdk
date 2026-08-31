from typing import Literal

ApiV1BlockRolloutsUpdateFailedItemsErrorComponentAttr = Literal["failed_items"]

API_V1_BLOCK_ROLLOUTS_UPDATE_FAILED_ITEMS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsUpdateFailedItemsErrorComponentAttr
] = {
    "failed_items",
}


def check_api_v1_block_rollouts_update_failed_items_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsUpdateFailedItemsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_FAILED_ITEMS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_FAILED_ITEMS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
