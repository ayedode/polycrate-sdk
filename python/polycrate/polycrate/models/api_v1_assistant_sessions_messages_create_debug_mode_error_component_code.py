from typing import Literal

ApiV1AssistantSessionsMessagesCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsMessagesCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_assistant_sessions_messages_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreateDebugModeErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
