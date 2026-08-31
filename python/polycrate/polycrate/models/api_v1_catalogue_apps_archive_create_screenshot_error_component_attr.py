from typing import Literal

ApiV1CatalogueAppsArchiveCreateScreenshotErrorComponentAttr = Literal["screenshot"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_SCREENSHOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateScreenshotErrorComponentAttr
] = {
    "screenshot",
}


def check_api_v1_catalogue_apps_archive_create_screenshot_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateScreenshotErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_SCREENSHOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_SCREENSHOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
