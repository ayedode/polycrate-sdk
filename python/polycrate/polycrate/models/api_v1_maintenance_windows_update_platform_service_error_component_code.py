from typing import Literal

ApiV1MaintenanceWindowsUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenance_windows_update_platform_service_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
