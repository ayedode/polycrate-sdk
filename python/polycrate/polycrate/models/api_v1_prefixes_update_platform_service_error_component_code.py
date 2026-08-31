from typing import Literal

ApiV1PrefixesUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_PREFIXES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PrefixesUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_prefixes_update_platform_service_error_component_code(
    value: str,
) -> ApiV1PrefixesUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_PREFIXES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
