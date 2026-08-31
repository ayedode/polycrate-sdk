from typing import Literal

ApiV1HostsReconcileCreateResourceDiskErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_HOSTS_RECONCILE_CREATE_RESOURCE_DISK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsReconcileCreateResourceDiskErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_hosts_reconcile_create_resource_disk_error_component_code(
    value: str,
) -> ApiV1HostsReconcileCreateResourceDiskErrorComponentCode:
    if value in API_V1_HOSTS_RECONCILE_CREATE_RESOURCE_DISK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_RESOURCE_DISK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
