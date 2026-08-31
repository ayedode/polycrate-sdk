from typing import Literal

ApiV1ConversationsConversationsCreateConversationProviderErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type"
]

API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_CONVERSATION_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsConversationsCreateConversationProviderErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_conversations_conversations_create_conversation_provider_error_component_code(
    value: str,
) -> ApiV1ConversationsConversationsCreateConversationProviderErrorComponentCode:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_CONVERSATION_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_CONVERSATION_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
