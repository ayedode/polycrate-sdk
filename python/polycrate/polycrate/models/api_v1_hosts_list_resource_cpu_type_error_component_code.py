from typing import Literal

ApiV1HostsListResourceCpuTypeErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_HOSTS_LIST_RESOURCE_CPU_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsListResourceCpuTypeErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_hosts_list_resource_cpu_type_error_component_code(
    value: str,
) -> ApiV1HostsListResourceCpuTypeErrorComponentCode:
    if value in API_V1_HOSTS_LIST_RESOURCE_CPU_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_RESOURCE_CPU_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
