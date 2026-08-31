from typing import Literal

ApiV1IpaddressesPartialUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_IPADDRESSES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesPartialUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_ipaddresses_partial_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1IpaddressesPartialUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_IPADDRESSES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
