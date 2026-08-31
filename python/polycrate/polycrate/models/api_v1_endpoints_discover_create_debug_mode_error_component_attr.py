from typing import Literal

ApiV1EndpointsDiscoverCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_ENDPOINTS_DISCOVER_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_endpoints_discover_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateDebugModeErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
