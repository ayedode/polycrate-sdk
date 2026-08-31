from typing import Literal

ApiV1OrganizationsUpdateCachedMemberActiveCountErrorComponentAttr = Literal["cached_member_active_count"]

API_V1_ORGANIZATIONS_UPDATE_CACHED_MEMBER_ACTIVE_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateCachedMemberActiveCountErrorComponentAttr
] = {
    "cached_member_active_count",
}


def check_api_v1_organizations_update_cached_member_active_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateCachedMemberActiveCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_CACHED_MEMBER_ACTIVE_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_CACHED_MEMBER_ACTIVE_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
