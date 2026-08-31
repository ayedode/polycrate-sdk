from typing import Literal

ApiV1ConversationsMessagesUpdateContentErrorComponentAttr = Literal["content"]

API_V1_CONVERSATIONS_MESSAGES_UPDATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesUpdateContentErrorComponentAttr
] = {
    "content",
}


def check_api_v1_conversations_messages_update_content_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesUpdateContentErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_UPDATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_UPDATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
