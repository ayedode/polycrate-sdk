from typing import Literal

ApiV1ConversationsMessagesCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_CONVERSATIONS_MESSAGES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsMessagesCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_conversations_messages_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1ConversationsMessagesCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_CONVERSATIONS_MESSAGES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
