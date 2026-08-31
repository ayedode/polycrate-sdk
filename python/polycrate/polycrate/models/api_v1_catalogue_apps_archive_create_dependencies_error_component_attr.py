from typing import Literal

ApiV1CatalogueAppsArchiveCreateDependenciesErrorComponentAttr = Literal["dependencies"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_DEPENDENCIES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateDependenciesErrorComponentAttr
] = {
    "dependencies",
}


def check_api_v1_catalogue_apps_archive_create_dependencies_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateDependenciesErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_DEPENDENCIES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_DEPENDENCIES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
