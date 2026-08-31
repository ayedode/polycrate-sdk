from typing import Literal

ApiV1HostsListResourceMemoryErrorComponentAttr = Literal["resource_memory"]

API_V1_HOSTS_LIST_RESOURCE_MEMORY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsListResourceMemoryErrorComponentAttr] = {
    "resource_memory",
}


def check_api_v1_hosts_list_resource_memory_error_component_attr(
    value: str,
) -> ApiV1HostsListResourceMemoryErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_RESOURCE_MEMORY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_RESOURCE_MEMORY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
