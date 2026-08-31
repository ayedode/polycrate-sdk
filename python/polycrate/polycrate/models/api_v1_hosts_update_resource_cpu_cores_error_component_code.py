from typing import Literal

ApiV1HostsUpdateResourceCpuCoresErrorComponentCode = Literal["invalid", "max_string_length", "max_value", "min_value"]

API_V1_HOSTS_UPDATE_RESOURCE_CPU_CORES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsUpdateResourceCpuCoresErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_hosts_update_resource_cpu_cores_error_component_code(
    value: str,
) -> ApiV1HostsUpdateResourceCpuCoresErrorComponentCode:
    if value in API_V1_HOSTS_UPDATE_RESOURCE_CPU_CORES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_RESOURCE_CPU_CORES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
