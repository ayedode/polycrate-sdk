from typing import Literal

ApiV1MaintenanceWindowsCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_MAINTENANCE_WINDOWS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_maintenance_windows_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
