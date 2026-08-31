from typing import Literal

ApiV1MaintenanceWindowsArchiveCreateNoticeRequiredErrorComponentAttr = Literal["notice_required"]

API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_NOTICE_REQUIRED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsArchiveCreateNoticeRequiredErrorComponentAttr
] = {
    "notice_required",
}


def check_api_v1_maintenance_windows_archive_create_notice_required_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsArchiveCreateNoticeRequiredErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_NOTICE_REQUIRED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_NOTICE_REQUIRED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
