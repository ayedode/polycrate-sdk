from typing import Literal

ApiV1WorkspacesRepairCreateGitlabProjectIdErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "required", "unique"
]

API_V1_WORKSPACES_REPAIR_CREATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesRepairCreateGitlabProjectIdErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "required",
    "unique",
}


def check_api_v1_workspaces_repair_create_gitlab_project_id_error_component_code(
    value: str,
) -> ApiV1WorkspacesRepairCreateGitlabProjectIdErrorComponentCode:
    if value in API_V1_WORKSPACES_REPAIR_CREATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_REPAIR_CREATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
