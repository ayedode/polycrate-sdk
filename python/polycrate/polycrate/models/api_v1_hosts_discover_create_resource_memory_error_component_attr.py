from typing import Literal

ApiV1HostsDiscoverCreateResourceMemoryErrorComponentAttr = Literal["resource_memory"]

API_V1_HOSTS_DISCOVER_CREATE_RESOURCE_MEMORY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsDiscoverCreateResourceMemoryErrorComponentAttr
] = {
    "resource_memory",
}


def check_api_v1_hosts_discover_create_resource_memory_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreateResourceMemoryErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_RESOURCE_MEMORY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_RESOURCE_MEMORY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
