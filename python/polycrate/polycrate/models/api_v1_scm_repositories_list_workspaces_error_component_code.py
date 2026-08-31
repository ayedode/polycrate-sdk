from typing import Literal

ApiV1ScmRepositoriesListWorkspacesErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1_SCM_REPOSITORIES_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesListWorkspacesErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_scm_repositories_list_workspaces_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesListWorkspacesErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
