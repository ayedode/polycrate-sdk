from typing import Literal

ApiV1OrganizationsCreateCachedLbTraffic30DBytesErrorComponentAttr = Literal["cached_lb_traffic_30d_bytes"]

API_V1_ORGANIZATIONS_CREATE_CACHED_LB_TRAFFIC_30D_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateCachedLbTraffic30DBytesErrorComponentAttr
] = {
    "cached_lb_traffic_30d_bytes",
}


def check_api_v1_organizations_create_cached_lb_traffic_30d_bytes_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateCachedLbTraffic30DBytesErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_CACHED_LB_TRAFFIC_30D_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_CACHED_LB_TRAFFIC_30D_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
