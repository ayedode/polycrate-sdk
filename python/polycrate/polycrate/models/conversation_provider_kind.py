from typing import Literal

ConversationProviderKind = Literal["discord", "email", "generic", "msteams", "slack", "telegram", "zammad"]

CONVERSATION_PROVIDER_KIND_VALUES: set[ConversationProviderKind] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_conversation_provider_kind(value: str) -> ConversationProviderKind:
    if value in CONVERSATION_PROVIDER_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_PROVIDER_KIND_VALUES!r}")
