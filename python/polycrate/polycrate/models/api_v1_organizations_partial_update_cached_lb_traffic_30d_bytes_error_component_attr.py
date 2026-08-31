from typing import Literal

ApiV1OrganizationsPartialUpdateCachedLbTraffic30DBytesErrorComponentAttr = Literal["cached_lb_traffic_30d_bytes"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_LB_TRAFFIC_30D_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateCachedLbTraffic30DBytesErrorComponentAttr
] = {
    "cached_lb_traffic_30d_bytes",
}


def check_api_v1_organizations_partial_update_cached_lb_traffic_30d_bytes_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateCachedLbTraffic30DBytesErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_LB_TRAFFIC_30D_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_LB_TRAFFIC_30D_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
