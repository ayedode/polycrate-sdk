from typing import Literal

ApiV1OrganizationsUpdateGitlabGroupIdErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "unique"
]

API_V1_ORGANIZATIONS_UPDATE_GITLAB_GROUP_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdateGitlabGroupIdErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "unique",
}


def check_api_v1_organizations_update_gitlab_group_id_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateGitlabGroupIdErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_GITLAB_GROUP_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_GITLAB_GROUP_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
