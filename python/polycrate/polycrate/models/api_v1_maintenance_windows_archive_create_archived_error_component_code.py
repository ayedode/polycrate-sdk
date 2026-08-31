from typing import Literal

ApiV1MaintenanceWindowsArchiveCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsArchiveCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenance_windows_archive_create_archived_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsArchiveCreateArchivedErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
