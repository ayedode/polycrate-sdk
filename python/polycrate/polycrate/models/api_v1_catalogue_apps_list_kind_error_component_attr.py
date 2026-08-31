from typing import Literal

ApiV1CatalogueAppsListKindErrorComponentAttr = Literal["kind"]

API_V1_CATALOGUE_APPS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CatalogueAppsListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_catalogue_apps_list_kind_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsListKindErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
