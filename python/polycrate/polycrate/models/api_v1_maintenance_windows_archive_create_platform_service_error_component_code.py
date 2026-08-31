from typing import Literal

ApiV1MaintenanceWindowsArchiveCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsArchiveCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenance_windows_archive_create_platform_service_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsArchiveCreatePlatformServiceErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
