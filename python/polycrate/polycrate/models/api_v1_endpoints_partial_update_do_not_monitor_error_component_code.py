from typing import Literal

ApiV1EndpointsPartialUpdateDoNotMonitorErrorComponentCode = Literal["invalid", "null"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsPartialUpdateDoNotMonitorErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_endpoints_partial_update_do_not_monitor_error_component_code(
    value: str,
) -> ApiV1EndpointsPartialUpdateDoNotMonitorErrorComponentCode:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
