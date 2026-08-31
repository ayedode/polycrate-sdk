from typing import Literal

ApiV1PopsDiscoverCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_POPS_DISCOVER_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsDiscoverCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_pops_discover_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1PopsDiscoverCreateDebugModeErrorComponentAttr:
    if value in API_V1_POPS_DISCOVER_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_DISCOVER_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
