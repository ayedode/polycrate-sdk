from typing import Literal

ApiV1MaintenanceWindowsArchiveCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsArchiveCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_maintenance_windows_archive_create_kind_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsArchiveCreateKindErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
