from typing import Literal

ApiV1BlockRolloutItemsUpdateNameErrorComponentAttr = Literal["name"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_block_rollout_items_update_name_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateNameErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
