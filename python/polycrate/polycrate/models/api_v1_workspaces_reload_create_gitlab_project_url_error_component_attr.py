from typing import Literal

ApiV1WorkspacesReloadCreateGitlabProjectUrlErrorComponentAttr = Literal["gitlab_project_url"]

API_V1_WORKSPACES_RELOAD_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReloadCreateGitlabProjectUrlErrorComponentAttr
] = {
    "gitlab_project_url",
}


def check_api_v1_workspaces_reload_create_gitlab_project_url_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReloadCreateGitlabProjectUrlErrorComponentAttr:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
