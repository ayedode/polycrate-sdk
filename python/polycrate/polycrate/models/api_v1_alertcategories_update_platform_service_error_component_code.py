from typing import Literal

ApiV1AlertcategoriesUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTCATEGORIES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoriesUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alertcategories_update_platform_service_error_component_code(
    value: str,
) -> ApiV1AlertcategoriesUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_ALERTCATEGORIES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
