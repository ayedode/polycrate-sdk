from typing import Literal

ApiV1OrganizationsPartialUpdateCachedVolumeCapacityBytesErrorComponentAttr = Literal["cached_volume_capacity_bytes"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_VOLUME_CAPACITY_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateCachedVolumeCapacityBytesErrorComponentAttr
] = {
    "cached_volume_capacity_bytes",
}


def check_api_v1_organizations_partial_update_cached_volume_capacity_bytes_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateCachedVolumeCapacityBytesErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_VOLUME_CAPACITY_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_VOLUME_CAPACITY_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
