from typing import Literal

ApiV1HostsUpdateResourceCpuArchitectureErrorComponentAttr = Literal["resource_cpu_architecture"]

API_V1_HOSTS_UPDATE_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsUpdateResourceCpuArchitectureErrorComponentAttr
] = {
    "resource_cpu_architecture",
}


def check_api_v1_hosts_update_resource_cpu_architecture_error_component_attr(
    value: str,
) -> ApiV1HostsUpdateResourceCpuArchitectureErrorComponentAttr:
    if value in API_V1_HOSTS_UPDATE_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
