from typing import Literal

ConversationProviderListKind = Literal["discord", "email", "generic", "msteams", "slack", "telegram", "zammad"]

CONVERSATION_PROVIDER_LIST_KIND_VALUES: set[ConversationProviderListKind] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_conversation_provider_list_kind(value: str) -> ConversationProviderListKind:
    if value in CONVERSATION_PROVIDER_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_PROVIDER_LIST_KIND_VALUES!r}")
