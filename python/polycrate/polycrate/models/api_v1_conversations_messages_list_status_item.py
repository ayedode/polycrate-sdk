from typing import Literal

ApiV1ConversationsMessagesListStatusItem = Literal["deleted", "delivered", "error", "pending", "requested"]

API_V1_CONVERSATIONS_MESSAGES_LIST_STATUS_ITEM_VALUES: set[ApiV1ConversationsMessagesListStatusItem] = {
    "deleted",
    "delivered",
    "error",
    "pending",
    "requested",
}


def check_api_v1_conversations_messages_list_status_item(value: str) -> ApiV1ConversationsMessagesListStatusItem:
    if value in API_V1_CONVERSATIONS_MESSAGES_LIST_STATUS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_LIST_STATUS_ITEM_VALUES!r}"
    )
