from typing import Literal

ApiV1ConversationsMessagesListKindItem = Literal[
    "discord", "email", "generic", "msteams", "slack", "telegram", "zammad"
]

API_V1_CONVERSATIONS_MESSAGES_LIST_KIND_ITEM_VALUES: set[ApiV1ConversationsMessagesListKindItem] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_api_v1_conversations_messages_list_kind_item(value: str) -> ApiV1ConversationsMessagesListKindItem:
    if value in API_V1_CONVERSATIONS_MESSAGES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_LIST_KIND_ITEM_VALUES!r}"
    )
