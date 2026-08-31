from typing import Literal

ApiV1OrganizationsDiscoverCreateGitlabGroupIdErrorComponentAttr = Literal["gitlab_group_id"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_GITLAB_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateGitlabGroupIdErrorComponentAttr
] = {
    "gitlab_group_id",
}


def check_api_v1_organizations_discover_create_gitlab_group_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateGitlabGroupIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_GITLAB_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_GITLAB_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
