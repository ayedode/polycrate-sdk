from typing import Literal

ApiV1CatalogueAppsPartialUpdateScreenshotErrorComponentCode = Literal[
    "empty", "invalid", "invalid_image", "max_length", "no_name"
]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SCREENSHOT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateScreenshotErrorComponentCode
] = {
    "empty",
    "invalid",
    "invalid_image",
    "max_length",
    "no_name",
}


def check_api_v1_catalogue_apps_partial_update_screenshot_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateScreenshotErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SCREENSHOT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SCREENSHOT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
