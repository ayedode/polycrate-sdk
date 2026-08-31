from typing import Literal

ApiV1OrganizationsArchiveCreateGitlabGroupIdErrorComponentAttr = Literal["gitlab_group_id"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_GITLAB_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateGitlabGroupIdErrorComponentAttr
] = {
    "gitlab_group_id",
}


def check_api_v1_organizations_archive_create_gitlab_group_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateGitlabGroupIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_GITLAB_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_GITLAB_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
