from typing import Literal

ApiV1CatalogueAppsCreateScreenshotErrorComponentCode = Literal[
    "empty", "invalid", "invalid_image", "max_length", "no_name"
]

API_V1_CATALOGUE_APPS_CREATE_SCREENSHOT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsCreateScreenshotErrorComponentCode
] = {
    "empty",
    "invalid",
    "invalid_image",
    "max_length",
    "no_name",
}


def check_api_v1_catalogue_apps_create_screenshot_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsCreateScreenshotErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_CREATE_SCREENSHOT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_SCREENSHOT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
