from typing import Literal

ApiV1AssistantSessionsMessagesCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsMessagesCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_assistant_sessions_messages_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
