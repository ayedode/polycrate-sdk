from typing import Literal

ApiV1OrganizationsArchiveCreateCachedMemberCountErrorComponentAttr = Literal["cached_member_count"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_MEMBER_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateCachedMemberCountErrorComponentAttr
] = {
    "cached_member_count",
}


def check_api_v1_organizations_archive_create_cached_member_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateCachedMemberCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_MEMBER_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_MEMBER_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
