from typing import Literal

ApiV1HostsCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_HOSTS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsCreateDebugModeErrorComponentAttr] = {
    "debug_mode",
}


def check_api_v1_hosts_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1HostsCreateDebugModeErrorComponentAttr:
    if value in API_V1_HOSTS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
