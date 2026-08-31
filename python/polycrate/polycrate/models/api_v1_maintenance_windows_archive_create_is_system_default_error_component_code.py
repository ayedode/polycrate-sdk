from typing import Literal

ApiV1MaintenanceWindowsArchiveCreateIsSystemDefaultErrorComponentCode = Literal["invalid", "null", "unique"]

API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsArchiveCreateIsSystemDefaultErrorComponentCode
] = {
    "invalid",
    "null",
    "unique",
}


def check_api_v1_maintenance_windows_archive_create_is_system_default_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsArchiveCreateIsSystemDefaultErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
