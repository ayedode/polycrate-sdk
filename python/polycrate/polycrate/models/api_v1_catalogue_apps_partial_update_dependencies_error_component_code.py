from typing import Literal

ApiV1CatalogueAppsPartialUpdateDependenciesErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_DEPENDENCIES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateDependenciesErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_catalogue_apps_partial_update_dependencies_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateDependenciesErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_DEPENDENCIES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_DEPENDENCIES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
