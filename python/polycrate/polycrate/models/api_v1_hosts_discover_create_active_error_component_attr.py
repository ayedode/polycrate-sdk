from typing import Literal

ApiV1HostsDiscoverCreateActiveErrorComponentAttr = Literal["active"]

API_V1_HOSTS_DISCOVER_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsDiscoverCreateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_hosts_discover_create_active_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreateActiveErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
