from typing import Literal

ApiV1MaintenanceWindowsPartialUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsPartialUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenance_windows_partial_update_archived_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsPartialUpdateArchivedErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
