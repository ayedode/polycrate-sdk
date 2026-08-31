from typing import Literal

ApiV1MaintenanceWindowsPartialUpdateTimeSlotsErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_TIME_SLOTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsPartialUpdateTimeSlotsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenance_windows_partial_update_time_slots_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsPartialUpdateTimeSlotsErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_TIME_SLOTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_TIME_SLOTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
