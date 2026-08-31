from typing import Literal

ApiV1ConversationsMessagesCreateContentKindErrorComponentAttr = Literal["content_kind"]

API_V1_CONVERSATIONS_MESSAGES_CREATE_CONTENT_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesCreateContentKindErrorComponentAttr
] = {
    "content_kind",
}


def check_api_v1_conversations_messages_create_content_kind_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesCreateContentKindErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_CREATE_CONTENT_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_CREATE_CONTENT_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
