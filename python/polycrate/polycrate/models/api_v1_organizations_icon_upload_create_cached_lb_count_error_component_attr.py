from typing import Literal

ApiV1OrganizationsIconUploadCreateCachedLbCountErrorComponentAttr = Literal["cached_lb_count"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_LB_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCachedLbCountErrorComponentAttr
] = {
    "cached_lb_count",
}


def check_api_v1_organizations_icon_upload_create_cached_lb_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCachedLbCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_LB_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_LB_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
