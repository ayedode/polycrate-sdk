from typing import Literal

ApiV1ConversationsMessagesListConversationErrorComponentCode = Literal["invalid_choice"]

API_V1_CONVERSATIONS_MESSAGES_LIST_CONVERSATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsMessagesListConversationErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_conversations_messages_list_conversation_error_component_code(
    value: str,
) -> ApiV1ConversationsMessagesListConversationErrorComponentCode:
    if value in API_V1_CONVERSATIONS_MESSAGES_LIST_CONVERSATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_LIST_CONVERSATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
