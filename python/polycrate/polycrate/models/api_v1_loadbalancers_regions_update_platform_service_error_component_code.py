from typing import Literal

ApiV1LoadbalancersRegionsUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_regions_update_platform_service_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
