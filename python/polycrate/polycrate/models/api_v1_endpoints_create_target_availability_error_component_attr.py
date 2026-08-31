from typing import Literal

ApiV1EndpointsCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_ENDPOINTS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_endpoints_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1EndpointsCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_ENDPOINTS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
