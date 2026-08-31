from typing import Literal

ApiV1OrganizationsDiscoverCreateCachedVolumeCountErrorComponentAttr = Literal["cached_volume_count"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_VOLUME_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateCachedVolumeCountErrorComponentAttr
] = {
    "cached_volume_count",
}


def check_api_v1_organizations_discover_create_cached_volume_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateCachedVolumeCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_VOLUME_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_VOLUME_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
