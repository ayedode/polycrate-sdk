from typing import Literal

ApiV1AssistantSessionsListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_ASSISTANT_SESSIONS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_assistant_sessions_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsListWorkspacesErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
