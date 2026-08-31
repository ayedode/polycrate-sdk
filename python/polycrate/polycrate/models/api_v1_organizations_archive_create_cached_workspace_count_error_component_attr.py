from typing import Literal

ApiV1OrganizationsArchiveCreateCachedWorkspaceCountErrorComponentAttr = Literal["cached_workspace_count"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_WORKSPACE_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateCachedWorkspaceCountErrorComponentAttr
] = {
    "cached_workspace_count",
}


def check_api_v1_organizations_archive_create_cached_workspace_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateCachedWorkspaceCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_WORKSPACE_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_WORKSPACE_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
