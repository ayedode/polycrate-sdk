from typing import Literal

ApiV1MaintenanceWindowsPartialUpdateLeadTimeDaysErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_LEAD_TIME_DAYS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsPartialUpdateLeadTimeDaysErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_maintenance_windows_partial_update_lead_time_days_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsPartialUpdateLeadTimeDaysErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_LEAD_TIME_DAYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_LEAD_TIME_DAYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
