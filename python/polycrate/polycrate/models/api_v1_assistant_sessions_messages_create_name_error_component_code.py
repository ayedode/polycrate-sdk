from typing import Literal

ApiV1AssistantSessionsMessagesCreateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsMessagesCreateNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_assistant_sessions_messages_create_name_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreateNameErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
