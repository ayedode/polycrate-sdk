from typing import Literal

ApiV1HostsDiscoverCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_HOSTS_DISCOVER_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsDiscoverCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_hosts_discover_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
