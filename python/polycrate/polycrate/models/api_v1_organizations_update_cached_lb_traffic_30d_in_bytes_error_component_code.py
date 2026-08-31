from typing import Literal

ApiV1OrganizationsUpdateCachedLbTraffic30DInBytesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_ORGANIZATIONS_UPDATE_CACHED_LB_TRAFFIC_30D_IN_BYTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdateCachedLbTraffic30DInBytesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_organizations_update_cached_lb_traffic_30d_in_bytes_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateCachedLbTraffic30DInBytesErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_CACHED_LB_TRAFFIC_30D_IN_BYTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_CACHED_LB_TRAFFIC_30D_IN_BYTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
