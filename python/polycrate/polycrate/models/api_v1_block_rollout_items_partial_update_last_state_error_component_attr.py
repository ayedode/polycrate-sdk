from typing import Literal

ApiV1BlockRolloutItemsPartialUpdateLastStateErrorComponentAttr = Literal["last_state"]

API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsPartialUpdateLastStateErrorComponentAttr
] = {
    "last_state",
}


def check_api_v1_block_rollout_items_partial_update_last_state_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsPartialUpdateLastStateErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
