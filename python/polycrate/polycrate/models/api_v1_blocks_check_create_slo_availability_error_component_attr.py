from typing import Literal

ApiV1BlocksCheckCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_BLOCKS_CHECK_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_blocks_check_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
