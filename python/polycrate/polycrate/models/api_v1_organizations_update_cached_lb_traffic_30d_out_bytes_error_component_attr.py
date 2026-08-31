from typing import Literal

ApiV1OrganizationsUpdateCachedLbTraffic30DOutBytesErrorComponentAttr = Literal["cached_lb_traffic_30d_out_bytes"]

API_V1_ORGANIZATIONS_UPDATE_CACHED_LB_TRAFFIC_30D_OUT_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateCachedLbTraffic30DOutBytesErrorComponentAttr
] = {
    "cached_lb_traffic_30d_out_bytes",
}


def check_api_v1_organizations_update_cached_lb_traffic_30d_out_bytes_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateCachedLbTraffic30DOutBytesErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_CACHED_LB_TRAFFIC_30D_OUT_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_CACHED_LB_TRAFFIC_30D_OUT_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
