from typing import Literal

ApiV1OrganizationsReconcileCreateCachedVolumeCapacityBytesErrorComponentAttr = Literal["cached_volume_capacity_bytes"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_VOLUME_CAPACITY_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateCachedVolumeCapacityBytesErrorComponentAttr
] = {
    "cached_volume_capacity_bytes",
}


def check_api_v1_organizations_reconcile_create_cached_volume_capacity_bytes_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateCachedVolumeCapacityBytesErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_VOLUME_CAPACITY_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_VOLUME_CAPACITY_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
