from typing import Literal

ApiV1WorkspacesLogsReloadCreateGitlabProjectUrlErrorComponentAttr = Literal["gitlab_project_url"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateGitlabProjectUrlErrorComponentAttr
] = {
    "gitlab_project_url",
}


def check_api_v1_workspaces_logs_reload_create_gitlab_project_url_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateGitlabProjectUrlErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
