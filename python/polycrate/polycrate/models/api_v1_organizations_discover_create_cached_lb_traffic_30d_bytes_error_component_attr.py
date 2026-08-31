from typing import Literal

ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DBytesErrorComponentAttr = Literal["cached_lb_traffic_30d_bytes"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_LB_TRAFFIC_30D_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DBytesErrorComponentAttr
] = {
    "cached_lb_traffic_30d_bytes",
}


def check_api_v1_organizations_discover_create_cached_lb_traffic_30d_bytes_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DBytesErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_LB_TRAFFIC_30D_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_LB_TRAFFIC_30D_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
