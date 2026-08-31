from typing import Literal

ApiV1CatalogueAppsUpdateScreenshotErrorComponentCode = Literal[
    "empty", "invalid", "invalid_image", "max_length", "no_name"
]

API_V1_CATALOGUE_APPS_UPDATE_SCREENSHOT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsUpdateScreenshotErrorComponentCode
] = {
    "empty",
    "invalid",
    "invalid_image",
    "max_length",
    "no_name",
}


def check_api_v1_catalogue_apps_update_screenshot_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsUpdateScreenshotErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_UPDATE_SCREENSHOT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_SCREENSHOT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
