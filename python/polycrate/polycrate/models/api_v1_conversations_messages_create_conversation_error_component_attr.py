from typing import Literal

ApiV1ConversationsMessagesCreateConversationErrorComponentAttr = Literal["conversation"]

API_V1_CONVERSATIONS_MESSAGES_CREATE_CONVERSATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesCreateConversationErrorComponentAttr
] = {
    "conversation",
}


def check_api_v1_conversations_messages_create_conversation_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesCreateConversationErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_CREATE_CONVERSATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_CREATE_CONVERSATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
