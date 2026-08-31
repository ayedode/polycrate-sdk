from typing import Literal

ApiV1HostsPartialUpdateResourceDiskErrorComponentAttr = Literal["resource_disk"]

API_V1_HOSTS_PARTIAL_UPDATE_RESOURCE_DISK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsPartialUpdateResourceDiskErrorComponentAttr
] = {
    "resource_disk",
}


def check_api_v1_hosts_partial_update_resource_disk_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateResourceDiskErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_RESOURCE_DISK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_RESOURCE_DISK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
