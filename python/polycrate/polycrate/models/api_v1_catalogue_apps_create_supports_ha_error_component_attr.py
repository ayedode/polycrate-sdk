from typing import Literal

ApiV1CatalogueAppsCreateSupportsHaErrorComponentAttr = Literal["supports_ha"]

API_V1_CATALOGUE_APPS_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsCreateSupportsHaErrorComponentAttr
] = {
    "supports_ha",
}


def check_api_v1_catalogue_apps_create_supports_ha_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateSupportsHaErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
