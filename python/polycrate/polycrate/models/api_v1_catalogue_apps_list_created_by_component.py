from typing import Literal

ApiV1CatalogueAppsListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_CATALOGUE_APPS_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1CatalogueAppsListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_catalogue_apps_list_created_by_component(value: str) -> ApiV1CatalogueAppsListCreatedByComponent:
    if value in API_V1_CATALOGUE_APPS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
