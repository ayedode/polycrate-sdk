from typing import Literal

ApiV1MaintenanceWindowsArchiveCreateTimeSlotsErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_TIME_SLOTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsArchiveCreateTimeSlotsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenance_windows_archive_create_time_slots_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsArchiveCreateTimeSlotsErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_TIME_SLOTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_TIME_SLOTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
