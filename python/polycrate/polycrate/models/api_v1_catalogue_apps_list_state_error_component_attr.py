from typing import Literal

ApiV1CatalogueAppsListStateErrorComponentAttr = Literal["state"]

API_V1_CATALOGUE_APPS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CatalogueAppsListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_catalogue_apps_list_state_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsListStateErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
