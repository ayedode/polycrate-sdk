from typing import Literal

ApiV1OrganizationsPartialUpdateCachedMemberCountErrorComponentAttr = Literal["cached_member_count"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_MEMBER_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateCachedMemberCountErrorComponentAttr
] = {
    "cached_member_count",
}


def check_api_v1_organizations_partial_update_cached_member_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateCachedMemberCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_MEMBER_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_MEMBER_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
