from typing import Literal

ApiV1CatalogueAppsUpdateScreenshotErrorComponentAttr = Literal["screenshot"]

API_V1_CATALOGUE_APPS_UPDATE_SCREENSHOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsUpdateScreenshotErrorComponentAttr
] = {
    "screenshot",
}


def check_api_v1_catalogue_apps_update_screenshot_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsUpdateScreenshotErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_UPDATE_SCREENSHOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_SCREENSHOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
