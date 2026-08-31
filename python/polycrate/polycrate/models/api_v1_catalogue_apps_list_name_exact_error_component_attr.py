from typing import Literal

ApiV1CatalogueAppsListNameExactErrorComponentAttr = Literal["name_exact"]

API_V1_CATALOGUE_APPS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsListNameExactErrorComponentAttr
] = {
    "name_exact",
}


def check_api_v1_catalogue_apps_list_name_exact_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsListNameExactErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
