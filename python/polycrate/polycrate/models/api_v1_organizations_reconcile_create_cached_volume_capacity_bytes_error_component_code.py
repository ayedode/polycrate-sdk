from typing import Literal

ApiV1OrganizationsReconcileCreateCachedVolumeCapacityBytesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_VOLUME_CAPACITY_BYTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsReconcileCreateCachedVolumeCapacityBytesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_organizations_reconcile_create_cached_volume_capacity_bytes_error_component_code(
    value: str,
) -> ApiV1OrganizationsReconcileCreateCachedVolumeCapacityBytesErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_VOLUME_CAPACITY_BYTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_VOLUME_CAPACITY_BYTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
