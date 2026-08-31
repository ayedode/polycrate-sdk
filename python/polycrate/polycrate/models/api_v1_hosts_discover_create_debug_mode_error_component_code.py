from typing import Literal

ApiV1HostsDiscoverCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_HOSTS_DISCOVER_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsDiscoverCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_hosts_discover_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1HostsDiscoverCreateDebugModeErrorComponentCode:
    if value in API_V1_HOSTS_DISCOVER_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
