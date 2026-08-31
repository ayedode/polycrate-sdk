from typing import Literal

ApiV1MaintenanceWindowsPartialUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsPartialUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_maintenance_windows_partial_update_criticality_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsPartialUpdateCriticalityErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
