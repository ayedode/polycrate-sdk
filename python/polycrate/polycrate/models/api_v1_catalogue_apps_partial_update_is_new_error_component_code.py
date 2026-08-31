from typing import Literal

ApiV1CatalogueAppsPartialUpdateIsNewErrorComponentCode = Literal["invalid", "null"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_IS_NEW_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateIsNewErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_catalogue_apps_partial_update_is_new_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateIsNewErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_IS_NEW_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_IS_NEW_ERROR_COMPONENT_CODE_VALUES!r}"
    )
