from typing import Literal

ApiV1HostsDiscoverCreateAliasErrorComponentAttr = Literal["alias"]

API_V1_HOSTS_DISCOVER_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsDiscoverCreateAliasErrorComponentAttr] = {
    "alias",
}


def check_api_v1_hosts_discover_create_alias_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreateAliasErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
