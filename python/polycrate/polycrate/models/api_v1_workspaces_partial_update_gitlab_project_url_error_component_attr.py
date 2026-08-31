from typing import Literal

ApiV1WorkspacesPartialUpdateGitlabProjectUrlErrorComponentAttr = Literal["gitlab_project_url"]

API_V1_WORKSPACES_PARTIAL_UPDATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesPartialUpdateGitlabProjectUrlErrorComponentAttr
] = {
    "gitlab_project_url",
}


def check_api_v1_workspaces_partial_update_gitlab_project_url_error_component_attr(
    value: str,
) -> ApiV1WorkspacesPartialUpdateGitlabProjectUrlErrorComponentAttr:
    if value in API_V1_WORKSPACES_PARTIAL_UPDATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_PARTIAL_UPDATE_GITLAB_PROJECT_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
