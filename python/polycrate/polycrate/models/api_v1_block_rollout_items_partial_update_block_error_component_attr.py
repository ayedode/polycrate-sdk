from typing import Literal

ApiV1BlockRolloutItemsPartialUpdateBlockErrorComponentAttr = Literal["block"]

API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsPartialUpdateBlockErrorComponentAttr
] = {
    "block",
}


def check_api_v1_block_rollout_items_partial_update_block_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsPartialUpdateBlockErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
