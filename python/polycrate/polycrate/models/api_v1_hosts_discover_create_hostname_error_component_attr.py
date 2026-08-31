from typing import Literal

ApiV1HostsDiscoverCreateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_HOSTS_DISCOVER_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsDiscoverCreateHostnameErrorComponentAttr
] = {
    "hostname",
}


def check_api_v1_hosts_discover_create_hostname_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreateHostnameErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
