from typing import Literal

ApiV1MaintenanceWindowsUpdateTimeSlotsErrorComponentAttr = Literal["time_slots"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_TIME_SLOTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateTimeSlotsErrorComponentAttr
] = {
    "time_slots",
}


def check_api_v1_maintenance_windows_update_time_slots_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateTimeSlotsErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_TIME_SLOTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_TIME_SLOTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
