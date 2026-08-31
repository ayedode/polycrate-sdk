from typing import Literal

ApiV1MaintenancesArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_maintenances_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
