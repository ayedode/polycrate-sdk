from typing import Literal

ApiV1MaintenanceWindowsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_maintenance_windows_update_criticality_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
