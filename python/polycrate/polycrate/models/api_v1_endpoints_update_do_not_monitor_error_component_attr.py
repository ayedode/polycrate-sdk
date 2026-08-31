from typing import Literal

ApiV1EndpointsUpdateDoNotMonitorErrorComponentAttr = Literal["do_not_monitor"]

API_V1_ENDPOINTS_UPDATE_DO_NOT_MONITOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsUpdateDoNotMonitorErrorComponentAttr
] = {
    "do_not_monitor",
}


def check_api_v1_endpoints_update_do_not_monitor_error_component_attr(
    value: str,
) -> ApiV1EndpointsUpdateDoNotMonitorErrorComponentAttr:
    if value in API_V1_ENDPOINTS_UPDATE_DO_NOT_MONITOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_DO_NOT_MONITOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
