from typing import Literal

ApiV1CatalogueAppsArchiveCreateSupportsHaErrorComponentAttr = Literal["supports_ha"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateSupportsHaErrorComponentAttr
] = {
    "supports_ha",
}


def check_api_v1_catalogue_apps_archive_create_supports_ha_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateSupportsHaErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
