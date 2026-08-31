from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateScreenshotErrorComponentAttr = Literal["screenshot"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SCREENSHOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateScreenshotErrorComponentAttr
] = {
    "screenshot",
}


def check_api_v1_catalogue_apps_sync_releases_create_screenshot_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateScreenshotErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SCREENSHOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SCREENSHOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
