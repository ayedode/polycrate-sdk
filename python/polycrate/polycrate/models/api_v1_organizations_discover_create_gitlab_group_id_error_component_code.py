from typing import Literal

ApiV1OrganizationsDiscoverCreateGitlabGroupIdErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "unique"
]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_GITLAB_GROUP_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreateGitlabGroupIdErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "unique",
}


def check_api_v1_organizations_discover_create_gitlab_group_id_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateGitlabGroupIdErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_GITLAB_GROUP_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_GITLAB_GROUP_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
