from typing import Literal

ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DOutBytesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_LB_TRAFFIC_30D_OUT_BYTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DOutBytesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_organizations_icon_upload_create_cached_lb_traffic_30d_out_bytes_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DOutBytesErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_LB_TRAFFIC_30D_OUT_BYTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_LB_TRAFFIC_30D_OUT_BYTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
