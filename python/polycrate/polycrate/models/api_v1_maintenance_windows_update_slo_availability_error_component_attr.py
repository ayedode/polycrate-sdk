from typing import Literal

ApiV1MaintenanceWindowsUpdateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_maintenance_windows_update_slo_availability_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateSloAvailabilityErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
