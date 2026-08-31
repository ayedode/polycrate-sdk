from typing import Literal

ApiV1OrganizationsArchiveCreateGitlabGroupUrlErrorComponentAttr = Literal["gitlab_group_url"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_GITLAB_GROUP_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateGitlabGroupUrlErrorComponentAttr
] = {
    "gitlab_group_url",
}


def check_api_v1_organizations_archive_create_gitlab_group_url_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateGitlabGroupUrlErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_GITLAB_GROUP_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_GITLAB_GROUP_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
