from typing import Literal

ApiV1HostsPartialUpdateResourceDiskErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_HOSTS_PARTIAL_UPDATE_RESOURCE_DISK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsPartialUpdateResourceDiskErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_hosts_partial_update_resource_disk_error_component_code(
    value: str,
) -> ApiV1HostsPartialUpdateResourceDiskErrorComponentCode:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_RESOURCE_DISK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_RESOURCE_DISK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
