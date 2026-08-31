from typing import Literal

ApiV1ConversationsProvidersListKindItem = Literal[
    "discord", "email", "generic", "msteams", "slack", "telegram", "zammad"
]

API_V1_CONVERSATIONS_PROVIDERS_LIST_KIND_ITEM_VALUES: set[ApiV1ConversationsProvidersListKindItem] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_api_v1_conversations_providers_list_kind_item(value: str) -> ApiV1ConversationsProvidersListKindItem:
    if value in API_V1_CONVERSATIONS_PROVIDERS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_LIST_KIND_ITEM_VALUES!r}"
    )
