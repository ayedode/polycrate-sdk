from typing import Literal

ApiV1MaintenanceWindowsUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_maintenance_windows_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateProviderIdErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
