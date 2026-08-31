from typing import Literal

ApiV1AgentsListWorkspacesErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1_AGENTS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AgentsListWorkspacesErrorComponentCode] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_agents_list_workspaces_error_component_code(value: str) -> ApiV1AgentsListWorkspacesErrorComponentCode:
    if value in API_V1_AGENTS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_AGENTS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
