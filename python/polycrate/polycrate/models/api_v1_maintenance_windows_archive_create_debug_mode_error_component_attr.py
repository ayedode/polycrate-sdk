from typing import Literal

ApiV1MaintenanceWindowsArchiveCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsArchiveCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_maintenance_windows_archive_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsArchiveCreateDebugModeErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
