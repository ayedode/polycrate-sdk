from typing import Literal

ApiV1HostsDiscoverCreateResourceCpuCoresErrorComponentAttr = Literal["resource_cpu_cores"]

API_V1_HOSTS_DISCOVER_CREATE_RESOURCE_CPU_CORES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsDiscoverCreateResourceCpuCoresErrorComponentAttr
] = {
    "resource_cpu_cores",
}


def check_api_v1_hosts_discover_create_resource_cpu_cores_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreateResourceCpuCoresErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_RESOURCE_CPU_CORES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_RESOURCE_CPU_CORES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
