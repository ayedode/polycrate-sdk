from typing import Literal

ApiV1OrganizationsIconUploadCreateGitlabGroupUrlErrorComponentAttr = Literal["gitlab_group_url"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_GITLAB_GROUP_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateGitlabGroupUrlErrorComponentAttr
] = {
    "gitlab_group_url",
}


def check_api_v1_organizations_icon_upload_create_gitlab_group_url_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateGitlabGroupUrlErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_GITLAB_GROUP_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_GITLAB_GROUP_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
