from typing import Literal

ApiV1MaintenanceWindowsUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenance_windows_update_tolerations_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateTolerationsErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
