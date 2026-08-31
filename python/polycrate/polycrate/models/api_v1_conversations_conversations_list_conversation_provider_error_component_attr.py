from typing import Literal

ApiV1ConversationsConversationsListConversationProviderErrorComponentAttr = Literal["conversation_provider"]

API_V1_CONVERSATIONS_CONVERSATIONS_LIST_CONVERSATION_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsConversationsListConversationProviderErrorComponentAttr
] = {
    "conversation_provider",
}


def check_api_v1_conversations_conversations_list_conversation_provider_error_component_attr(
    value: str,
) -> ApiV1ConversationsConversationsListConversationProviderErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_LIST_CONVERSATION_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_LIST_CONVERSATION_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
