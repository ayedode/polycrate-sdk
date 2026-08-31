from typing import Literal

ApiV1OrganizationsPartialUpdateCachedWorkspaceCountErrorComponentAttr = Literal["cached_workspace_count"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_WORKSPACE_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateCachedWorkspaceCountErrorComponentAttr
] = {
    "cached_workspace_count",
}


def check_api_v1_organizations_partial_update_cached_workspace_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateCachedWorkspaceCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_WORKSPACE_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_WORKSPACE_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
