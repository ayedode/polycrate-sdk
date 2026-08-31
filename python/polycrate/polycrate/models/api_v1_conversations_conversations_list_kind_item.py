from typing import Literal

ApiV1ConversationsConversationsListKindItem = Literal[
    "discord", "email", "generic", "msteams", "slack", "telegram", "zammad"
]

API_V1_CONVERSATIONS_CONVERSATIONS_LIST_KIND_ITEM_VALUES: set[ApiV1ConversationsConversationsListKindItem] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_api_v1_conversations_conversations_list_kind_item(value: str) -> ApiV1ConversationsConversationsListKindItem:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_LIST_KIND_ITEM_VALUES!r}"
    )
