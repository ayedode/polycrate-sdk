from typing import Literal

ApiV1AgentsListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_AGENTS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AgentsListWorkspacesErrorComponentAttr] = {
    "workspaces",
}


def check_api_v1_agents_list_workspaces_error_component_attr(value: str) -> ApiV1AgentsListWorkspacesErrorComponentAttr:
    if value in API_V1_AGENTS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_AGENTS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
