from typing import Literal

ApiV1MaintenanceWindowsCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_MAINTENANCE_WINDOWS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_maintenance_windows_create_criticality_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsCreateCriticalityErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
