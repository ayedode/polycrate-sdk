from typing import Literal

ApiV1BlockRolloutItemsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_block_rollout_items_update_criticality_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
