from typing import Literal

ApiV1HostsArchiveCreateResourceMemoryErrorComponentAttr = Literal["resource_memory"]

API_V1_HOSTS_ARCHIVE_CREATE_RESOURCE_MEMORY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsArchiveCreateResourceMemoryErrorComponentAttr
] = {
    "resource_memory",
}


def check_api_v1_hosts_archive_create_resource_memory_error_component_attr(
    value: str,
) -> ApiV1HostsArchiveCreateResourceMemoryErrorComponentAttr:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_RESOURCE_MEMORY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_RESOURCE_MEMORY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
