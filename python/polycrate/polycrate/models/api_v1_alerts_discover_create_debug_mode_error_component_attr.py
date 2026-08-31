from typing import Literal

ApiV1AlertsDiscoverCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_ALERTS_DISCOVER_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_alerts_discover_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateDebugModeErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
