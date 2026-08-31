from typing import Literal

ApiV1EndpointsCreateDoNotMonitorErrorComponentCode = Literal["invalid", "null"]

API_V1_ENDPOINTS_CREATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsCreateDoNotMonitorErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_endpoints_create_do_not_monitor_error_component_code(
    value: str,
) -> ApiV1EndpointsCreateDoNotMonitorErrorComponentCode:
    if value in API_V1_ENDPOINTS_CREATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
