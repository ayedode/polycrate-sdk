from typing import Literal

ApiV1OrganizationsUpdateCachedLbTraffic30DBytesErrorComponentAttr = Literal["cached_lb_traffic_30d_bytes"]

API_V1_ORGANIZATIONS_UPDATE_CACHED_LB_TRAFFIC_30D_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateCachedLbTraffic30DBytesErrorComponentAttr
] = {
    "cached_lb_traffic_30d_bytes",
}


def check_api_v1_organizations_update_cached_lb_traffic_30d_bytes_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateCachedLbTraffic30DBytesErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_CACHED_LB_TRAFFIC_30D_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_CACHED_LB_TRAFFIC_30D_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
