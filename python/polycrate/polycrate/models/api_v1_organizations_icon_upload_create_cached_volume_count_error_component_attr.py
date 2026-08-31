from typing import Literal

ApiV1OrganizationsIconUploadCreateCachedVolumeCountErrorComponentAttr = Literal["cached_volume_count"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_VOLUME_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCachedVolumeCountErrorComponentAttr
] = {
    "cached_volume_count",
}


def check_api_v1_organizations_icon_upload_create_cached_volume_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCachedVolumeCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_VOLUME_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_VOLUME_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
