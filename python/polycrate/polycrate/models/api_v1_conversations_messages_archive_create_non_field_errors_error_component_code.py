from typing import Literal

ApiV1ConversationsMessagesArchiveCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsMessagesArchiveCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_conversations_messages_archive_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1ConversationsMessagesArchiveCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
