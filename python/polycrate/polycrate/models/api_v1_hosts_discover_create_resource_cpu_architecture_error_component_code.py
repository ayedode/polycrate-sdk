from typing import Literal

ApiV1HostsDiscoverCreateResourceCpuArchitectureErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_HOSTS_DISCOVER_CREATE_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsDiscoverCreateResourceCpuArchitectureErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_hosts_discover_create_resource_cpu_architecture_error_component_code(
    value: str,
) -> ApiV1HostsDiscoverCreateResourceCpuArchitectureErrorComponentCode:
    if value in API_V1_HOSTS_DISCOVER_CREATE_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
