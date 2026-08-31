from typing import Literal

ApiV1HostsArchiveCreateResourceCpuCoresErrorComponentAttr = Literal["resource_cpu_cores"]

API_V1_HOSTS_ARCHIVE_CREATE_RESOURCE_CPU_CORES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsArchiveCreateResourceCpuCoresErrorComponentAttr
] = {
    "resource_cpu_cores",
}


def check_api_v1_hosts_archive_create_resource_cpu_cores_error_component_attr(
    value: str,
) -> ApiV1HostsArchiveCreateResourceCpuCoresErrorComponentAttr:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_RESOURCE_CPU_CORES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_RESOURCE_CPU_CORES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
