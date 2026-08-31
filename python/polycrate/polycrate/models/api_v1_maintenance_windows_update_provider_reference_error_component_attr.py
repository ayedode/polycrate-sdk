from typing import Literal

ApiV1MaintenanceWindowsUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_maintenance_windows_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
