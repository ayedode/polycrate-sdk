from typing import Literal

ApiV1OrganizationsDiscoverCreateCachedEndpointDownCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_ENDPOINT_DOWN_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreateCachedEndpointDownCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_organizations_discover_create_cached_endpoint_down_count_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateCachedEndpointDownCountErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_ENDPOINT_DOWN_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_ENDPOINT_DOWN_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
