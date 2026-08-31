from typing import Literal

ApiV1EndpointsUpdateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_ENDPOINTS_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsUpdateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_endpoints_update_actual_availability_error_component_attr(
    value: str,
) -> ApiV1EndpointsUpdateActualAvailabilityErrorComponentAttr:
    if value in API_V1_ENDPOINTS_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
