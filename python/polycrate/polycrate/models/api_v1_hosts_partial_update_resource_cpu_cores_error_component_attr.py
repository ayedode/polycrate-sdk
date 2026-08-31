from typing import Literal

ApiV1HostsPartialUpdateResourceCpuCoresErrorComponentAttr = Literal["resource_cpu_cores"]

API_V1_HOSTS_PARTIAL_UPDATE_RESOURCE_CPU_CORES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsPartialUpdateResourceCpuCoresErrorComponentAttr
] = {
    "resource_cpu_cores",
}


def check_api_v1_hosts_partial_update_resource_cpu_cores_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateResourceCpuCoresErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_RESOURCE_CPU_CORES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_RESOURCE_CPU_CORES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
