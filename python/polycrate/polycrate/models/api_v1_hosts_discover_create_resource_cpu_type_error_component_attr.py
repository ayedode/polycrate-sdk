from typing import Literal

ApiV1HostsDiscoverCreateResourceCpuTypeErrorComponentAttr = Literal["resource_cpu_type"]

API_V1_HOSTS_DISCOVER_CREATE_RESOURCE_CPU_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsDiscoverCreateResourceCpuTypeErrorComponentAttr
] = {
    "resource_cpu_type",
}


def check_api_v1_hosts_discover_create_resource_cpu_type_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreateResourceCpuTypeErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_RESOURCE_CPU_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_RESOURCE_CPU_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
