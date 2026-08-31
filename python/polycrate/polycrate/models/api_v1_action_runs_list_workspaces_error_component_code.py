from typing import Literal

ApiV1ActionRunsListWorkspacesErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1_ACTION_RUNS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ActionRunsListWorkspacesErrorComponentCode] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_action_runs_list_workspaces_error_component_code(
    value: str,
) -> ApiV1ActionRunsListWorkspacesErrorComponentCode:
    if value in API_V1_ACTION_RUNS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
