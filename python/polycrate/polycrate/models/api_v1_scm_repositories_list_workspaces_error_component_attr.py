from typing import Literal

ApiV1ScmRepositoriesListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_SCM_REPOSITORIES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_scm_repositories_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesListWorkspacesErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
