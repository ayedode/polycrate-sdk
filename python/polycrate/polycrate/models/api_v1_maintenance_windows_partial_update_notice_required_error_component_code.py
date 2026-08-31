from typing import Literal

ApiV1MaintenanceWindowsPartialUpdateNoticeRequiredErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_NOTICE_REQUIRED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsPartialUpdateNoticeRequiredErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenance_windows_partial_update_notice_required_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsPartialUpdateNoticeRequiredErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_NOTICE_REQUIRED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_NOTICE_REQUIRED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
