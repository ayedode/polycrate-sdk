from typing import Literal

ApiV1OrganizationsUpdateCachedLbTraffic30DBytesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_ORGANIZATIONS_UPDATE_CACHED_LB_TRAFFIC_30D_BYTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdateCachedLbTraffic30DBytesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_organizations_update_cached_lb_traffic_30d_bytes_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateCachedLbTraffic30DBytesErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_CACHED_LB_TRAFFIC_30D_BYTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_CACHED_LB_TRAFFIC_30D_BYTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
