from typing import Literal

ApiV1EndpointsDiscoverCreateTargetAvailabilityErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_ENDPOINTS_DISCOVER_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsDiscoverCreateTargetAvailabilityErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_endpoints_discover_create_target_availability_error_component_code(
    value: str,
) -> ApiV1EndpointsDiscoverCreateTargetAvailabilityErrorComponentCode:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
