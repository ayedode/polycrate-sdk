from typing import Literal

ApiV1LoadbalancersRegionsPartialUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsPartialUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_loadbalancers_regions_partial_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsPartialUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
