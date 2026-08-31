from typing import Literal

ApiV1OrganizationsCreateGitlabGroupUrlErrorComponentAttr = Literal["gitlab_group_url"]

API_V1_ORGANIZATIONS_CREATE_GITLAB_GROUP_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateGitlabGroupUrlErrorComponentAttr
] = {
    "gitlab_group_url",
}


def check_api_v1_organizations_create_gitlab_group_url_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateGitlabGroupUrlErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_GITLAB_GROUP_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_GITLAB_GROUP_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
