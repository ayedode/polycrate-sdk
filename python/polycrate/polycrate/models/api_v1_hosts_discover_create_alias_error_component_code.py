from typing import Literal

ApiV1HostsDiscoverCreateAliasErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_HOSTS_DISCOVER_CREATE_ALIAS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsDiscoverCreateAliasErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_hosts_discover_create_alias_error_component_code(
    value: str,
) -> ApiV1HostsDiscoverCreateAliasErrorComponentCode:
    if value in API_V1_HOSTS_DISCOVER_CREATE_ALIAS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_ALIAS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
