from typing import Literal

ApiV1HostsDiscoverCreateDefaultIpv6ErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_HOSTS_DISCOVER_CREATE_DEFAULT_IPV_6_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsDiscoverCreateDefaultIpv6ErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_hosts_discover_create_default_ipv_6_error_component_code(
    value: str,
) -> ApiV1HostsDiscoverCreateDefaultIpv6ErrorComponentCode:
    if value in API_V1_HOSTS_DISCOVER_CREATE_DEFAULT_IPV_6_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_DEFAULT_IPV_6_ERROR_COMPONENT_CODE_VALUES!r}"
    )
