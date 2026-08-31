from typing import Literal

ApiV1BlocksCheckCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_BLOCKS_CHECK_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_blocks_check_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
