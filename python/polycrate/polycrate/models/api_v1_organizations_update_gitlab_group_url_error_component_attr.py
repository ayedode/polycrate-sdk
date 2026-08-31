from typing import Literal

ApiV1OrganizationsUpdateGitlabGroupUrlErrorComponentAttr = Literal["gitlab_group_url"]

API_V1_ORGANIZATIONS_UPDATE_GITLAB_GROUP_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateGitlabGroupUrlErrorComponentAttr
] = {
    "gitlab_group_url",
}


def check_api_v1_organizations_update_gitlab_group_url_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateGitlabGroupUrlErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_GITLAB_GROUP_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_GITLAB_GROUP_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
