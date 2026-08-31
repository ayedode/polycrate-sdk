from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_catalogue_apps_sync_releases_create_provider_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateProviderErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
