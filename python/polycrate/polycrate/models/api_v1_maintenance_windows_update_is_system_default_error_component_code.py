from typing import Literal

ApiV1MaintenanceWindowsUpdateIsSystemDefaultErrorComponentCode = Literal["invalid", "null", "unique"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsUpdateIsSystemDefaultErrorComponentCode
] = {
    "invalid",
    "null",
    "unique",
}


def check_api_v1_maintenance_windows_update_is_system_default_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateIsSystemDefaultErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
