from typing import Literal

ApiV1HostsUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_HOSTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_hosts_update_platform_service_error_component_code(
    value: str,
) -> ApiV1HostsUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_HOSTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
