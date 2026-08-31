from typing import Literal

ApiV1HostsDiscoverCreateHostnameErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_HOSTS_DISCOVER_CREATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsDiscoverCreateHostnameErrorComponentCode
] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_hosts_discover_create_hostname_error_component_code(
    value: str,
) -> ApiV1HostsDiscoverCreateHostnameErrorComponentCode:
    if value in API_V1_HOSTS_DISCOVER_CREATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
