from typing import Literal

ApiV1OrganizationsUpdateGitlabGroupUrlErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ORGANIZATIONS_UPDATE_GITLAB_GROUP_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdateGitlabGroupUrlErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_organizations_update_gitlab_group_url_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateGitlabGroupUrlErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_GITLAB_GROUP_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_GITLAB_GROUP_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
