from typing import Literal

ApiV1CatalogueAppsCreateScreenshotErrorComponentAttr = Literal["screenshot"]

API_V1_CATALOGUE_APPS_CREATE_SCREENSHOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsCreateScreenshotErrorComponentAttr
] = {
    "screenshot",
}


def check_api_v1_catalogue_apps_create_screenshot_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateScreenshotErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_SCREENSHOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_SCREENSHOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
