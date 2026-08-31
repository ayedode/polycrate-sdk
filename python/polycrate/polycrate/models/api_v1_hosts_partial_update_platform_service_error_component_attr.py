from typing import Literal

ApiV1HostsPartialUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_HOSTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsPartialUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_hosts_partial_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
