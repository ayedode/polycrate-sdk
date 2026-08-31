from typing import Literal

ApiV1CatalogueAppsPartialUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_catalogue_apps_partial_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateDebugModeErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
