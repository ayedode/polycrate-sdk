from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_catalogue_apps_sync_releases_create_provider_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateProviderErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
