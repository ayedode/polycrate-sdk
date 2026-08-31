from typing import Literal

ApiV1OrganizationsPartialUpdateGitlabGroupUrlErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_GITLAB_GROUP_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsPartialUpdateGitlabGroupUrlErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_organizations_partial_update_gitlab_group_url_error_component_code(
    value: str,
) -> ApiV1OrganizationsPartialUpdateGitlabGroupUrlErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_GITLAB_GROUP_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_GITLAB_GROUP_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
