from typing import Literal

ApiV1EndpointsDiscoverCreateDoNotMonitorErrorComponentAttr = Literal["do_not_monitor"]

API_V1_ENDPOINTS_DISCOVER_CREATE_DO_NOT_MONITOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateDoNotMonitorErrorComponentAttr
] = {
    "do_not_monitor",
}


def check_api_v1_endpoints_discover_create_do_not_monitor_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateDoNotMonitorErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_DO_NOT_MONITOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_DO_NOT_MONITOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
