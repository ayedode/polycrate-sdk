from typing import Literal

ApiV1BlockRolloutsPartialUpdateTotalItemsErrorComponentAttr = Literal["total_items"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_TOTAL_ITEMS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateTotalItemsErrorComponentAttr
] = {
    "total_items",
}


def check_api_v1_block_rollouts_partial_update_total_items_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateTotalItemsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_TOTAL_ITEMS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_TOTAL_ITEMS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
