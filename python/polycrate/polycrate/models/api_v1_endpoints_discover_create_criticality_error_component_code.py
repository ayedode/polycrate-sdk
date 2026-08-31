from typing import Literal

ApiV1EndpointsDiscoverCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_ENDPOINTS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsDiscoverCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_endpoints_discover_create_criticality_error_component_code(
    value: str,
) -> ApiV1EndpointsDiscoverCreateCriticalityErrorComponentCode:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
