from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_catalogue_apps_sync_releases_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateProviderIdErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
