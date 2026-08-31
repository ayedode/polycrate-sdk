from typing import Literal

ApiV1ConversationsMessagesListSender = Literal["operator", "user"]

API_V1_CONVERSATIONS_MESSAGES_LIST_SENDER_VALUES: set[ApiV1ConversationsMessagesListSender] = {
    "operator",
    "user",
}


def check_api_v1_conversations_messages_list_sender(value: str) -> ApiV1ConversationsMessagesListSender:
    if value in API_V1_CONVERSATIONS_MESSAGES_LIST_SENDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_LIST_SENDER_VALUES!r}")
