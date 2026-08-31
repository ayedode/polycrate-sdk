from typing import Literal

ApiV1CatalogueAppsPartialUpdateSupportsHaErrorComponentAttr = Literal["supports_ha"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateSupportsHaErrorComponentAttr
] = {
    "supports_ha",
}


def check_api_v1_catalogue_apps_partial_update_supports_ha_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateSupportsHaErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SUPPORTS_HA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
