from typing import Literal

ConversationProviderPostKind = Literal["discord", "email", "generic", "msteams", "slack", "telegram", "zammad"]

CONVERSATION_PROVIDER_POST_KIND_VALUES: set[ConversationProviderPostKind] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_conversation_provider_post_kind(value: str) -> ConversationProviderPostKind:
    if value in CONVERSATION_PROVIDER_POST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_PROVIDER_POST_KIND_VALUES!r}")
