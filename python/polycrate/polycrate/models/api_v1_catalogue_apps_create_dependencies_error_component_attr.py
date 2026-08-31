from typing import Literal

ApiV1CatalogueAppsCreateDependenciesErrorComponentAttr = Literal["dependencies"]

API_V1_CATALOGUE_APPS_CREATE_DEPENDENCIES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsCreateDependenciesErrorComponentAttr
] = {
    "dependencies",
}


def check_api_v1_catalogue_apps_create_dependencies_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateDependenciesErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_DEPENDENCIES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_DEPENDENCIES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
