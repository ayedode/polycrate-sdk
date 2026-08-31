from typing import Literal

ApiV1AssistantSessionsCreateWorkspaceIdErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_ASSISTANT_SESSIONS_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsCreateWorkspaceIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_assistant_sessions_create_workspace_id_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsCreateWorkspaceIdErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
