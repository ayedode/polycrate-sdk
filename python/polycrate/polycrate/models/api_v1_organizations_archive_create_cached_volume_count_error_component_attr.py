from typing import Literal

ApiV1OrganizationsArchiveCreateCachedVolumeCountErrorComponentAttr = Literal["cached_volume_count"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_VOLUME_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateCachedVolumeCountErrorComponentAttr
] = {
    "cached_volume_count",
}


def check_api_v1_organizations_archive_create_cached_volume_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateCachedVolumeCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_VOLUME_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_VOLUME_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
