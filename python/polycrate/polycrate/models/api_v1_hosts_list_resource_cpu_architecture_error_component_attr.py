from typing import Literal

ApiV1HostsListResourceCpuArchitectureErrorComponentAttr = Literal["resource_cpu_architecture"]

API_V1_HOSTS_LIST_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsListResourceCpuArchitectureErrorComponentAttr
] = {
    "resource_cpu_architecture",
}


def check_api_v1_hosts_list_resource_cpu_architecture_error_component_attr(
    value: str,
) -> ApiV1HostsListResourceCpuArchitectureErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
