from typing import Literal

ApiV1WorkspacesRepairCreateGitlabProjectUrlErrorComponentAttr = Literal["gitlab_project_url"]

API_V1_WORKSPACES_REPAIR_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRepairCreateGitlabProjectUrlErrorComponentAttr
] = {
    "gitlab_project_url",
}


def check_api_v1_workspaces_repair_create_gitlab_project_url_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRepairCreateGitlabProjectUrlErrorComponentAttr:
    if value in API_V1_WORKSPACES_REPAIR_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_REPAIR_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
