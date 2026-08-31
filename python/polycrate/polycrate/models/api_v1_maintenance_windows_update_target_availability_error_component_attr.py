from typing import Literal

ApiV1MaintenanceWindowsUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_maintenance_windows_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
