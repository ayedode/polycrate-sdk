from typing import Literal

ApiV1WorkspacesPartialUpdateGitlabProjectUrlErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACES_PARTIAL_UPDATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesPartialUpdateGitlabProjectUrlErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspaces_partial_update_gitlab_project_url_error_component_code(
    value: str,
) -> ApiV1WorkspacesPartialUpdateGitlabProjectUrlErrorComponentCode:
    if value in API_V1_WORKSPACES_PARTIAL_UPDATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_PARTIAL_UPDATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
