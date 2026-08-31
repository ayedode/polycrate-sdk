from typing import Literal

ApiV1CatalogueAppsListNameErrorComponentAttr = Literal["name"]

API_V1_CATALOGUE_APPS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CatalogueAppsListNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_catalogue_apps_list_name_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsListNameErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
