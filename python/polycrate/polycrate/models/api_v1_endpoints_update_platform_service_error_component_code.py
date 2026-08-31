from typing import Literal

ApiV1EndpointsUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_ENDPOINTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_endpoints_update_platform_service_error_component_code(
    value: str,
) -> ApiV1EndpointsUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_ENDPOINTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
