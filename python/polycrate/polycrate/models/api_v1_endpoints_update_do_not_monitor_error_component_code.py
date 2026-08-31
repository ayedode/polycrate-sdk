from typing import Literal

ApiV1EndpointsUpdateDoNotMonitorErrorComponentCode = Literal["invalid", "null"]

API_V1_ENDPOINTS_UPDATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsUpdateDoNotMonitorErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_endpoints_update_do_not_monitor_error_component_code(
    value: str,
) -> ApiV1EndpointsUpdateDoNotMonitorErrorComponentCode:
    if value in API_V1_ENDPOINTS_UPDATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
