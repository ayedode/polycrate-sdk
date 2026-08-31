from typing import Literal

ApiV1HostsDiscoverCreateDefaultIpv4ErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_HOSTS_DISCOVER_CREATE_DEFAULT_IPV_4_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsDiscoverCreateDefaultIpv4ErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_hosts_discover_create_default_ipv_4_error_component_code(
    value: str,
) -> ApiV1HostsDiscoverCreateDefaultIpv4ErrorComponentCode:
    if value in API_V1_HOSTS_DISCOVER_CREATE_DEFAULT_IPV_4_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_DEFAULT_IPV_4_ERROR_COMPONENT_CODE_VALUES!r}"
    )
