from typing import Literal

ApiV1CatalogueAppsListScope = Literal["system", "user"]

API_V1_CATALOGUE_APPS_LIST_SCOPE_VALUES: set[ApiV1CatalogueAppsListScope] = {
    "system",
    "user",
}


def check_api_v1_catalogue_apps_list_scope(value: str) -> ApiV1CatalogueAppsListScope:
    if value in API_V1_CATALOGUE_APPS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_LIST_SCOPE_VALUES!r}")
