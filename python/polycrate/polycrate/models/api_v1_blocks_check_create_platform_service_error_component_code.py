from typing import Literal

ApiV1BlocksCheckCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_CHECK_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksCheckCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_check_create_platform_service_error_component_code(
    value: str,
) -> ApiV1BlocksCheckCreatePlatformServiceErrorComponentCode:
    if value in API_V1_BLOCKS_CHECK_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
