from typing import Literal

ApiV1PopsDiscoverCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_POPS_DISCOVER_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PopsDiscoverCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pops_discover_create_platform_service_error_component_code(
    value: str,
) -> ApiV1PopsDiscoverCreatePlatformServiceErrorComponentCode:
    if value in API_V1_POPS_DISCOVER_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_DISCOVER_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
