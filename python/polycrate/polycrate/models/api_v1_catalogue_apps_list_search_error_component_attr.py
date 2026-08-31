from typing import Literal

ApiV1CatalogueAppsListSearchErrorComponentAttr = Literal["search"]

API_V1_CATALOGUE_APPS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CatalogueAppsListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_catalogue_apps_list_search_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsListSearchErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
