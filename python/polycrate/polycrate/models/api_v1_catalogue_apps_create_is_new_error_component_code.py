from typing import Literal

ApiV1CatalogueAppsCreateIsNewErrorComponentCode = Literal["invalid", "null"]

API_V1_CATALOGUE_APPS_CREATE_IS_NEW_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsCreateIsNewErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_catalogue_apps_create_is_new_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsCreateIsNewErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_CREATE_IS_NEW_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_IS_NEW_ERROR_COMPONENT_CODE_VALUES!r}"
    )
