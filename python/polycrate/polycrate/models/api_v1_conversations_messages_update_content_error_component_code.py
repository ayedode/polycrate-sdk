from typing import Literal

ApiV1ConversationsMessagesUpdateContentErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CONVERSATIONS_MESSAGES_UPDATE_CONTENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsMessagesUpdateContentErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_conversations_messages_update_content_error_component_code(
    value: str,
) -> ApiV1ConversationsMessagesUpdateContentErrorComponentCode:
    if value in API_V1_CONVERSATIONS_MESSAGES_UPDATE_CONTENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_UPDATE_CONTENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
