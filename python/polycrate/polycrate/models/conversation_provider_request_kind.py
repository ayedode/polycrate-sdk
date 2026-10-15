from typing import Literal

ConversationProviderRequestKind = Literal["discord", "email", "generic", "msteams", "slack", "telegram", "zammad"]

CONVERSATION_PROVIDER_REQUEST_KIND_VALUES: set[ConversationProviderRequestKind] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_conversation_provider_request_kind(value: str) -> ConversationProviderRequestKind:
    if value in CONVERSATION_PROVIDER_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_PROVIDER_REQUEST_KIND_VALUES!r}")
