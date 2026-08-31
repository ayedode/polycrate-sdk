from typing import Literal

ApiV1OrganizationsCreateCachedWorkspaceCountErrorComponentAttr = Literal["cached_workspace_count"]

API_V1_ORGANIZATIONS_CREATE_CACHED_WORKSPACE_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateCachedWorkspaceCountErrorComponentAttr
] = {
    "cached_workspace_count",
}


def check_api_v1_organizations_create_cached_workspace_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateCachedWorkspaceCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_CACHED_WORKSPACE_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_CACHED_WORKSPACE_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
