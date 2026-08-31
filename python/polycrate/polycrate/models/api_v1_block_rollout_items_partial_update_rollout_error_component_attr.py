from typing import Literal

ApiV1BlockRolloutItemsPartialUpdateRolloutErrorComponentAttr = Literal["rollout"]

API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsPartialUpdateRolloutErrorComponentAttr
] = {
    "rollout",
}


def check_api_v1_block_rollout_items_partial_update_rollout_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsPartialUpdateRolloutErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
