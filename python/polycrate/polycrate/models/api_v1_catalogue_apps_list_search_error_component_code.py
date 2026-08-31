from typing import Literal

ApiV1CatalogueAppsListSearchErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_CATALOGUE_APPS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CatalogueAppsListSearchErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_catalogue_apps_list_search_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsListSearchErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES!r}"
    )
