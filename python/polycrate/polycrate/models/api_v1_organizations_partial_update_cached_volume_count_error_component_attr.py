from typing import Literal

ApiV1OrganizationsPartialUpdateCachedVolumeCountErrorComponentAttr = Literal["cached_volume_count"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_VOLUME_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateCachedVolumeCountErrorComponentAttr
] = {
    "cached_volume_count",
}


def check_api_v1_organizations_partial_update_cached_volume_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateCachedVolumeCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_VOLUME_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_VOLUME_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
