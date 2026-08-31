from typing import Literal

ApiV1MaintenanceWindowsCreateTimeSlotsErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCE_WINDOWS_CREATE_TIME_SLOTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsCreateTimeSlotsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenance_windows_create_time_slots_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsCreateTimeSlotsErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_CREATE_TIME_SLOTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_CREATE_TIME_SLOTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
