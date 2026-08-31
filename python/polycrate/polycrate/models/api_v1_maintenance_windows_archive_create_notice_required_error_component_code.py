from typing import Literal

ApiV1MaintenanceWindowsArchiveCreateNoticeRequiredErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_NOTICE_REQUIRED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsArchiveCreateNoticeRequiredErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenance_windows_archive_create_notice_required_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsArchiveCreateNoticeRequiredErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_NOTICE_REQUIRED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_NOTICE_REQUIRED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
