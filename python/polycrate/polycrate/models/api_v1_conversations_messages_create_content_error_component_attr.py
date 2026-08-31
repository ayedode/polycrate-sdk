from typing import Literal

ApiV1ConversationsMessagesCreateContentErrorComponentAttr = Literal["content"]

API_V1_CONVERSATIONS_MESSAGES_CREATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesCreateContentErrorComponentAttr
] = {
    "content",
}


def check_api_v1_conversations_messages_create_content_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesCreateContentErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_CREATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_CREATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
