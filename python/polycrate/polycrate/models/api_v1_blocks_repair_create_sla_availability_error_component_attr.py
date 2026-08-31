from typing import Literal

ApiV1BlocksRepairCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_BLOCKS_REPAIR_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_blocks_repair_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
