from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateRegistryUrlErrorComponentAttr = Literal["registry_url"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateRegistryUrlErrorComponentAttr
] = {
    "registry_url",
}


def check_api_v1_catalogue_apps_sync_releases_create_registry_url_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateRegistryUrlErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
