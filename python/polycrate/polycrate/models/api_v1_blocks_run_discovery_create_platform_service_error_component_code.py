from typing import Literal

ApiV1BlocksRunDiscoveryCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRunDiscoveryCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_run_discovery_create_platform_service_error_component_code(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreatePlatformServiceErrorComponentCode:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
