from typing import Literal

ApiV1BlockRolloutItemsUpdateSourceUserErrorComponentAttr = Literal["source_user"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_SOURCE_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsUpdateSourceUserErrorComponentAttr
] = {
    "source_user",
}


def check_api_v1_block_rollout_items_update_source_user_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateSourceUserErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_SOURCE_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_SOURCE_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
