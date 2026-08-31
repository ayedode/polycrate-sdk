from typing import Literal

ApiV1BlockRolloutItemsPartialUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsPartialUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_block_rollout_items_partial_update_display_name_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsPartialUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
