from typing import Literal

ApiV1OrganizationsDiscoverCreateCachedMemberActiveCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_MEMBER_ACTIVE_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreateCachedMemberActiveCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_organizations_discover_create_cached_member_active_count_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateCachedMemberActiveCountErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_MEMBER_ACTIVE_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_MEMBER_ACTIVE_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
