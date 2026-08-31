from typing import Literal

ApiV1WorkspacesDiscoverCreateGitlabProjectIdErrorComponentAttr = Literal["gitlab_project_id"]

API_V1_WORKSPACES_DISCOVER_CREATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesDiscoverCreateGitlabProjectIdErrorComponentAttr
] = {
    "gitlab_project_id",
}


def check_api_v1_workspaces_discover_create_gitlab_project_id_error_component_attr(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateGitlabProjectIdErrorComponentAttr:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
