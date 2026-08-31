from typing import Literal

ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DInBytesErrorComponentAttr = Literal[
    "cached_lb_traffic_30d_in_bytes"
]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_LB_TRAFFIC_30D_IN_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DInBytesErrorComponentAttr
] = {
    "cached_lb_traffic_30d_in_bytes",
}


def check_api_v1_organizations_icon_upload_create_cached_lb_traffic_30d_in_bytes_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DInBytesErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_LB_TRAFFIC_30D_IN_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_LB_TRAFFIC_30D_IN_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
