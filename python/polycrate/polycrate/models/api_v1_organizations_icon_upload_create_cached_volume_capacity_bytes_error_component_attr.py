from typing import Literal

ApiV1OrganizationsIconUploadCreateCachedVolumeCapacityBytesErrorComponentAttr = Literal["cached_volume_capacity_bytes"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_VOLUME_CAPACITY_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCachedVolumeCapacityBytesErrorComponentAttr
] = {
    "cached_volume_capacity_bytes",
}


def check_api_v1_organizations_icon_upload_create_cached_volume_capacity_bytes_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCachedVolumeCapacityBytesErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_VOLUME_CAPACITY_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_VOLUME_CAPACITY_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
