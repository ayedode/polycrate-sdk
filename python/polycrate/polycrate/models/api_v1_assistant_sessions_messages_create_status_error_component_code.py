from typing import Literal

ApiV1AssistantSessionsMessagesCreateStatusErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsMessagesCreateStatusErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_assistant_sessions_messages_create_status_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreateStatusErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
