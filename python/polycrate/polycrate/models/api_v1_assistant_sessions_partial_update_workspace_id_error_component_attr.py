from typing import Literal

ApiV1AssistantSessionsPartialUpdateWorkspaceIdErrorComponentAttr = Literal["workspace_id"]

API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsPartialUpdateWorkspaceIdErrorComponentAttr
] = {
    "workspace_id",
}


def check_api_v1_assistant_sessions_partial_update_workspace_id_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsPartialUpdateWorkspaceIdErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
