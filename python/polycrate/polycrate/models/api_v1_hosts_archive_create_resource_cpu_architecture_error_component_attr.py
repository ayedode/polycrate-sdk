from typing import Literal

ApiV1HostsArchiveCreateResourceCpuArchitectureErrorComponentAttr = Literal["resource_cpu_architecture"]

API_V1_HOSTS_ARCHIVE_CREATE_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsArchiveCreateResourceCpuArchitectureErrorComponentAttr
] = {
    "resource_cpu_architecture",
}


def check_api_v1_hosts_archive_create_resource_cpu_architecture_error_component_attr(
    value: str,
) -> ApiV1HostsArchiveCreateResourceCpuArchitectureErrorComponentAttr:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
