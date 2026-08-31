from typing import Literal

ApiV1CatalogueAppsUpdateIsNewErrorComponentCode = Literal["invalid", "null"]

API_V1_CATALOGUE_APPS_UPDATE_IS_NEW_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsUpdateIsNewErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_catalogue_apps_update_is_new_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsUpdateIsNewErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_UPDATE_IS_NEW_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_IS_NEW_ERROR_COMPONENT_CODE_VALUES!r}"
    )
