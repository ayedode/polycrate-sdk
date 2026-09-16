from typing import Literal

ApiV1CatalogueAppsListMaintainerErrorComponentAttr = Literal["maintainer"]

API_V1_CATALOGUE_APPS_LIST_MAINTAINER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsListMaintainerErrorComponentAttr
] = {
    "maintainer",
}


def check_api_v1_catalogue_apps_list_maintainer_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsListMaintainerErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_LIST_MAINTAINER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_LIST_MAINTAINER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
