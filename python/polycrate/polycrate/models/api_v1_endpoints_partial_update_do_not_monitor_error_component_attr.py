from typing import Literal

ApiV1EndpointsPartialUpdateDoNotMonitorErrorComponentAttr = Literal["do_not_monitor"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_DO_NOT_MONITOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsPartialUpdateDoNotMonitorErrorComponentAttr
] = {
    "do_not_monitor",
}


def check_api_v1_endpoints_partial_update_do_not_monitor_error_component_attr(
    value: str,
) -> ApiV1EndpointsPartialUpdateDoNotMonitorErrorComponentAttr:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_DO_NOT_MONITOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_DO_NOT_MONITOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
