from typing import Literal

ApiV1BlockRolloutItemsPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_block_rollout_items_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
