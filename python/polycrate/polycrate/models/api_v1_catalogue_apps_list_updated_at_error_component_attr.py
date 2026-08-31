from typing import Literal

ApiV1CatalogueAppsListUpdatedAtErrorComponentAttr = Literal["updated_at"]

API_V1_CATALOGUE_APPS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsListUpdatedAtErrorComponentAttr
] = {
    "updated_at",
}


def check_api_v1_catalogue_apps_list_updated_at_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsListUpdatedAtErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
