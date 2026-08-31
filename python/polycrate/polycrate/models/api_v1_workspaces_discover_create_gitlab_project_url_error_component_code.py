from typing import Literal

ApiV1WorkspacesDiscoverCreateGitlabProjectUrlErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACES_DISCOVER_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesDiscoverCreateGitlabProjectUrlErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspaces_discover_create_gitlab_project_url_error_component_code(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateGitlabProjectUrlErrorComponentCode:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
