from typing import Literal

ApiV1ConversationsMessagesListSenderErrorComponentAttr = Literal["sender"]

API_V1_CONVERSATIONS_MESSAGES_LIST_SENDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesListSenderErrorComponentAttr
] = {
    "sender",
}


def check_api_v1_conversations_messages_list_sender_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesListSenderErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_LIST_SENDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_LIST_SENDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
