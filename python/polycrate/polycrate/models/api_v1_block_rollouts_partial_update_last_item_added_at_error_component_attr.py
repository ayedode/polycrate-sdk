from typing import Literal

ApiV1BlockRolloutsPartialUpdateLastItemAddedAtErrorComponentAttr = Literal["last_item_added_at"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_LAST_ITEM_ADDED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateLastItemAddedAtErrorComponentAttr
] = {
    "last_item_added_at",
}


def check_api_v1_block_rollouts_partial_update_last_item_added_at_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateLastItemAddedAtErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_LAST_ITEM_ADDED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_LAST_ITEM_ADDED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
