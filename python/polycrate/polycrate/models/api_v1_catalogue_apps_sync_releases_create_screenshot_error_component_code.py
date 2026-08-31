from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateScreenshotErrorComponentCode = Literal[
    "empty", "invalid", "invalid_image", "max_length", "no_name"
]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SCREENSHOT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateScreenshotErrorComponentCode
] = {
    "empty",
    "invalid",
    "invalid_image",
    "max_length",
    "no_name",
}


def check_api_v1_catalogue_apps_sync_releases_create_screenshot_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateScreenshotErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SCREENSHOT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SCREENSHOT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
