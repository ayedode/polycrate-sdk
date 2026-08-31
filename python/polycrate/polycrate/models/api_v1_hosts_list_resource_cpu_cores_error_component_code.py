from typing import Literal

ApiV1HostsListResourceCpuCoresErrorComponentCode = Literal["invalid", "max_value"]

API_V1_HOSTS_LIST_RESOURCE_CPU_CORES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsListResourceCpuCoresErrorComponentCode
] = {
    "invalid",
    "max_value",
}


def check_api_v1_hosts_list_resource_cpu_cores_error_component_code(
    value: str,
) -> ApiV1HostsListResourceCpuCoresErrorComponentCode:
    if value in API_V1_HOSTS_LIST_RESOURCE_CPU_CORES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_RESOURCE_CPU_CORES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
