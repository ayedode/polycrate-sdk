from typing import Literal

ApiV1BlockRolloutItemsCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_block_rollout_items_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
