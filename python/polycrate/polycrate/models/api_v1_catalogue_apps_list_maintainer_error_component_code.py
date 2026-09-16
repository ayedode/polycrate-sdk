from typing import Literal

ApiV1CatalogueAppsListMaintainerErrorComponentCode = Literal["invalid", "max_value"]

API_V1_CATALOGUE_APPS_LIST_MAINTAINER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsListMaintainerErrorComponentCode
] = {
    "invalid",
    "max_value",
}


def check_api_v1_catalogue_apps_list_maintainer_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsListMaintainerErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_LIST_MAINTAINER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_LIST_MAINTAINER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
