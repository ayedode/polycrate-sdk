from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateSupportsHaErrorComponentAttr = Literal["supports_ha"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateSupportsHaErrorComponentAttr
] = {
    "supports_ha",
}


def check_api_v1_catalogue_apps_sync_releases_create_supports_ha_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateSupportsHaErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
