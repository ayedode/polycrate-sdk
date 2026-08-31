from typing import Literal

ApiV1HostsDiscoverCreateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_HOSTS_DISCOVER_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsDiscoverCreateActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_hosts_discover_create_active_error_component_code(
    value: str,
) -> ApiV1HostsDiscoverCreateActiveErrorComponentCode:
    if value in API_V1_HOSTS_DISCOVER_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
