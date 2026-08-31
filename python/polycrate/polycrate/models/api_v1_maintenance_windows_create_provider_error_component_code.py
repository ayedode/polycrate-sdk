from typing import Literal

ApiV1MaintenanceWindowsCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_MAINTENANCE_WINDOWS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_maintenance_windows_create_provider_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsCreateProviderErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
