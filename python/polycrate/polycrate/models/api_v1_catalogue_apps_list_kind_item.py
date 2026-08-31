from typing import Literal

ApiV1CatalogueAppsListKindItem = Literal["generic"]

API_V1_CATALOGUE_APPS_LIST_KIND_ITEM_VALUES: set[ApiV1CatalogueAppsListKindItem] = {
    "generic",
}


def check_api_v1_catalogue_apps_list_kind_item(value: str) -> ApiV1CatalogueAppsListKindItem:
    if value in API_V1_CATALOGUE_APPS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_LIST_KIND_ITEM_VALUES!r}")
