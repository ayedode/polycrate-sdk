from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateGitlabProjectUrlErrorComponentAttr = Literal["gitlab_project_url"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateGitlabProjectUrlErrorComponentAttr
] = {
    "gitlab_project_url",
}


def check_api_v1_workspaces_run_discovery_create_gitlab_project_url_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateGitlabProjectUrlErrorComponentAttr:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
