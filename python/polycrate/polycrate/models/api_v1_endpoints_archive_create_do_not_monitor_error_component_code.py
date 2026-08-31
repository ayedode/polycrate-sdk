from typing import Literal

ApiV1EndpointsArchiveCreateDoNotMonitorErrorComponentCode = Literal["invalid", "null"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsArchiveCreateDoNotMonitorErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_endpoints_archive_create_do_not_monitor_error_component_code(
    value: str,
) -> ApiV1EndpointsArchiveCreateDoNotMonitorErrorComponentCode:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
