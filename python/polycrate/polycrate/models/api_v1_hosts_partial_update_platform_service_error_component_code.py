from typing import Literal

ApiV1HostsPartialUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_HOSTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsPartialUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_hosts_partial_update_platform_service_error_component_code(
    value: str,
) -> ApiV1HostsPartialUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
