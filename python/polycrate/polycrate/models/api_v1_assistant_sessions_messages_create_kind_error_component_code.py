from typing import Literal

ApiV1AssistantSessionsMessagesCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsMessagesCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_assistant_sessions_messages_create_kind_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreateKindErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
