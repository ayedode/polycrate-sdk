from typing import Literal

ApiV1CatalogueAppsPartialUpdateRegistryUrlErrorComponentAttr = Literal["registry_url"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateRegistryUrlErrorComponentAttr
] = {
    "registry_url",
}


def check_api_v1_catalogue_apps_partial_update_registry_url_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateRegistryUrlErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
