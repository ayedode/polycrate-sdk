from typing import Literal

ApiV1ConversationsMessagesListConversationErrorComponentAttr = Literal["conversation"]

API_V1_CONVERSATIONS_MESSAGES_LIST_CONVERSATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesListConversationErrorComponentAttr
] = {
    "conversation",
}


def check_api_v1_conversations_messages_list_conversation_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesListConversationErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_LIST_CONVERSATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_LIST_CONVERSATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
