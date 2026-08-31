from typing import Literal

ApiV1ConversationsMessagesArchiveCreateNameErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsMessagesArchiveCreateNameErrorComponentCode
] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_conversations_messages_archive_create_name_error_component_code(
    value: str,
) -> ApiV1ConversationsMessagesArchiveCreateNameErrorComponentCode:
    if value in API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
