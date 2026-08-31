from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateDependenciesErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_DEPENDENCIES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateDependenciesErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_catalogue_apps_sync_releases_create_dependencies_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateDependenciesErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_DEPENDENCIES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_DEPENDENCIES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
