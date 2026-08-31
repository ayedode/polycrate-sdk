from typing import Literal

ApiV1HostsDiscoverCreateRoleErrorComponentAttr = Literal["role"]

API_V1_HOSTS_DISCOVER_CREATE_ROLE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsDiscoverCreateRoleErrorComponentAttr] = {
    "role",
}


def check_api_v1_hosts_discover_create_role_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreateRoleErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_ROLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_ROLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
