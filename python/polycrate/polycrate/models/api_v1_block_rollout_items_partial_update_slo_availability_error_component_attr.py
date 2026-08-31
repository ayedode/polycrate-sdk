from typing import Literal

ApiV1BlockRolloutItemsPartialUpdateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsPartialUpdateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_block_rollout_items_partial_update_slo_availability_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsPartialUpdateSloAvailabilityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
