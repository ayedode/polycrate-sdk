from typing import Literal

ApiV1BlockRolloutItemsUpdateRolloutErrorComponentAttr = Literal["rollout"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsUpdateRolloutErrorComponentAttr
] = {
    "rollout",
}


def check_api_v1_block_rollout_items_update_rollout_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateRolloutErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
