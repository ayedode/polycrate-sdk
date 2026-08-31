from typing import Literal

ApiV1CatalogueAppsCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_CATALOGUE_APPS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_catalogue_apps_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsCreateDebugModeErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
