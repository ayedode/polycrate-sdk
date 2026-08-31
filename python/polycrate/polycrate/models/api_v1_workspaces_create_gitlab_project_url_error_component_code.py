from typing import Literal

ApiV1WorkspacesCreateGitlabProjectUrlErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACES_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCreateGitlabProjectUrlErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspaces_create_gitlab_project_url_error_component_code(
    value: str,
) -> ApiV1WorkspacesCreateGitlabProjectUrlErrorComponentCode:
    if value in API_V1_WORKSPACES_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
