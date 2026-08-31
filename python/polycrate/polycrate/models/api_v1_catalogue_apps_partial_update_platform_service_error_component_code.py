from typing import Literal

ApiV1CatalogueAppsPartialUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsPartialUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_catalogue_apps_partial_update_platform_service_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
