from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_catalogue_apps_sync_releases_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateDebugModeErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
