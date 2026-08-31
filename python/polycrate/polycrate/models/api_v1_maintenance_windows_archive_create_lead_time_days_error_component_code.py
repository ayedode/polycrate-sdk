from typing import Literal

ApiV1MaintenanceWindowsArchiveCreateLeadTimeDaysErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_LEAD_TIME_DAYS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsArchiveCreateLeadTimeDaysErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_maintenance_windows_archive_create_lead_time_days_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsArchiveCreateLeadTimeDaysErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_LEAD_TIME_DAYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_LEAD_TIME_DAYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
