from typing import Literal

ApiV1WorkspacesRepairCreateGitlabProjectIdErrorComponentAttr = Literal["gitlab_project_id"]

API_V1_WORKSPACES_REPAIR_CREATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRepairCreateGitlabProjectIdErrorComponentAttr
] = {
    "gitlab_project_id",
}


def check_api_v1_workspaces_repair_create_gitlab_project_id_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRepairCreateGitlabProjectIdErrorComponentAttr:
    if value in API_V1_WORKSPACES_REPAIR_CREATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_REPAIR_CREATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
