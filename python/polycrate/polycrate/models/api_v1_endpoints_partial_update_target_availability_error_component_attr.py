from typing import Literal

ApiV1EndpointsPartialUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsPartialUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_endpoints_partial_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1EndpointsPartialUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
