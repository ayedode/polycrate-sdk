from typing import Literal

ApiV1MaintenanceWindowsUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_maintenance_windows_update_provider_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateProviderErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
