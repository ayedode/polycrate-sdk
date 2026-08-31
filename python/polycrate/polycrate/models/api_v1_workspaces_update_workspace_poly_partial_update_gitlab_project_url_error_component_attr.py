from typing import Literal

ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectUrlErrorComponentAttr = Literal["gitlab_project_url"]

API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectUrlErrorComponentAttr
] = {
    "gitlab_project_url",
}


def check_api_v1_workspaces_update_workspace_poly_partial_update_gitlab_project_url_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGitlabProjectUrlErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
