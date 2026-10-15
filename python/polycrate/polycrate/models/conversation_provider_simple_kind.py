from typing import Literal

ConversationProviderSimpleKind = Literal["discord", "email", "generic", "msteams", "slack", "telegram", "zammad"]

CONVERSATION_PROVIDER_SIMPLE_KIND_VALUES: set[ConversationProviderSimpleKind] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_conversation_provider_simple_kind(value: str) -> ConversationProviderSimpleKind:
    if value in CONVERSATION_PROVIDER_SIMPLE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_PROVIDER_SIMPLE_KIND_VALUES!r}")
