from typing import Literal

ApiV1OrganizationsIconUploadCreateCachedEndpointDownCountErrorComponentAttr = Literal["cached_endpoint_down_count"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_ENDPOINT_DOWN_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCachedEndpointDownCountErrorComponentAttr
] = {
    "cached_endpoint_down_count",
}


def check_api_v1_organizations_icon_upload_create_cached_endpoint_down_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCachedEndpointDownCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_ENDPOINT_DOWN_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_ENDPOINT_DOWN_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
