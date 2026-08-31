from typing import Literal

ApiV1CatalogueAppsListScopeErrorComponentAttr = Literal["scope"]

API_V1_CATALOGUE_APPS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CatalogueAppsListScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_catalogue_apps_list_scope_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsListScopeErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
