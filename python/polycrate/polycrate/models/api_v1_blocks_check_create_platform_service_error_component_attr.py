from typing import Literal

ApiV1BlocksCheckCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_BLOCKS_CHECK_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_blocks_check_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
