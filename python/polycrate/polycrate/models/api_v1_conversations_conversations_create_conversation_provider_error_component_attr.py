from typing import Literal

ApiV1ConversationsConversationsCreateConversationProviderErrorComponentAttr = Literal["conversation_provider"]

API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_CONVERSATION_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsConversationsCreateConversationProviderErrorComponentAttr
] = {
    "conversation_provider",
}


def check_api_v1_conversations_conversations_create_conversation_provider_error_component_attr(
    value: str,
) -> ApiV1ConversationsConversationsCreateConversationProviderErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_CONVERSATION_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_CONVERSATION_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
