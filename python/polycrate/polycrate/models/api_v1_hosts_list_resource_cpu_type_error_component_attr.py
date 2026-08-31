from typing import Literal

ApiV1HostsListResourceCpuTypeErrorComponentAttr = Literal["resource_cpu_type"]

API_V1_HOSTS_LIST_RESOURCE_CPU_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsListResourceCpuTypeErrorComponentAttr
] = {
    "resource_cpu_type",
}


def check_api_v1_hosts_list_resource_cpu_type_error_component_attr(
    value: str,
) -> ApiV1HostsListResourceCpuTypeErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_RESOURCE_CPU_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_RESOURCE_CPU_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
