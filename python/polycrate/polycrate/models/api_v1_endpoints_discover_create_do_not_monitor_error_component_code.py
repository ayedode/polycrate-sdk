from typing import Literal

ApiV1EndpointsDiscoverCreateDoNotMonitorErrorComponentCode = Literal["invalid", "null"]

API_V1_ENDPOINTS_DISCOVER_CREATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsDiscoverCreateDoNotMonitorErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_endpoints_discover_create_do_not_monitor_error_component_code(
    value: str,
) -> ApiV1EndpointsDiscoverCreateDoNotMonitorErrorComponentCode:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
