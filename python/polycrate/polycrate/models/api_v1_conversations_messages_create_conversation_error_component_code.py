from typing import Literal

ApiV1ConversationsMessagesCreateConversationErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_CONVERSATIONS_MESSAGES_CREATE_CONVERSATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsMessagesCreateConversationErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_conversations_messages_create_conversation_error_component_code(
    value: str,
) -> ApiV1ConversationsMessagesCreateConversationErrorComponentCode:
    if value in API_V1_CONVERSATIONS_MESSAGES_CREATE_CONVERSATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_CREATE_CONVERSATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
