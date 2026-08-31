from typing import Literal

ApiV1OrganizationsIconUploadCreateCachedActiveDowntimesCountErrorComponentAttr = Literal[
    "cached_active_downtimes_count"
]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_ACTIVE_DOWNTIMES_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCachedActiveDowntimesCountErrorComponentAttr
] = {
    "cached_active_downtimes_count",
}


def check_api_v1_organizations_icon_upload_create_cached_active_downtimes_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCachedActiveDowntimesCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_ACTIVE_DOWNTIMES_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_ACTIVE_DOWNTIMES_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
