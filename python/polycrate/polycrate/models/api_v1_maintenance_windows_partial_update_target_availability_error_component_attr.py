from typing import Literal

ApiV1MaintenanceWindowsPartialUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsPartialUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_maintenance_windows_partial_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsPartialUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
