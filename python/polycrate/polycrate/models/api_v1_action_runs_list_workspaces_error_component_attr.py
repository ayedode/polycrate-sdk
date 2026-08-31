from typing import Literal

ApiV1ActionRunsListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_ACTION_RUNS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ActionRunsListWorkspacesErrorComponentAttr] = {
    "workspaces",
}


def check_api_v1_action_runs_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1ActionRunsListWorkspacesErrorComponentAttr:
    if value in API_V1_ACTION_RUNS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
