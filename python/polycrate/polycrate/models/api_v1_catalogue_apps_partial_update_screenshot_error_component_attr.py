from typing import Literal

ApiV1CatalogueAppsPartialUpdateScreenshotErrorComponentAttr = Literal["screenshot"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SCREENSHOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateScreenshotErrorComponentAttr
] = {
    "screenshot",
}


def check_api_v1_catalogue_apps_partial_update_screenshot_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateScreenshotErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SCREENSHOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SCREENSHOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
