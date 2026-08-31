from typing import Literal

ApiV1HostsDiscoverCreateResourceMemoryErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_HOSTS_DISCOVER_CREATE_RESOURCE_MEMORY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsDiscoverCreateResourceMemoryErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_hosts_discover_create_resource_memory_error_component_code(
    value: str,
) -> ApiV1HostsDiscoverCreateResourceMemoryErrorComponentCode:
    if value in API_V1_HOSTS_DISCOVER_CREATE_RESOURCE_MEMORY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_RESOURCE_MEMORY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
