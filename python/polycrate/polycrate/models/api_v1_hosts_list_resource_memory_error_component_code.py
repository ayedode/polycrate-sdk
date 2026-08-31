from typing import Literal

ApiV1HostsListResourceMemoryErrorComponentCode = Literal["invalid", "max_value"]

API_V1_HOSTS_LIST_RESOURCE_MEMORY_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsListResourceMemoryErrorComponentCode] = {
    "invalid",
    "max_value",
}


def check_api_v1_hosts_list_resource_memory_error_component_code(
    value: str,
) -> ApiV1HostsListResourceMemoryErrorComponentCode:
    if value in API_V1_HOSTS_LIST_RESOURCE_MEMORY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_RESOURCE_MEMORY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
