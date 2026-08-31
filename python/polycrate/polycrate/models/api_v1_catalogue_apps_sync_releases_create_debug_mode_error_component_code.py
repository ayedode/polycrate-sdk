from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_catalogue_apps_sync_releases_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateDebugModeErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
