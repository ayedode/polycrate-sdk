from typing import Literal

ApiV1PrefixesPartialUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_PREFIXES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PrefixesPartialUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_prefixes_partial_update_platform_service_error_component_code(
    value: str,
) -> ApiV1PrefixesPartialUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_PREFIXES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
