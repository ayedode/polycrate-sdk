from typing import Literal

ApiV1BlockRolloutItemsUpdateBlockErrorComponentAttr = Literal["block"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsUpdateBlockErrorComponentAttr
] = {
    "block",
}


def check_api_v1_block_rollout_items_update_block_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateBlockErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
