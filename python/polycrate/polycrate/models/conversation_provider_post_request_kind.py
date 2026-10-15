from typing import Literal

ConversationProviderPostRequestKind = Literal["discord", "email", "generic", "msteams", "slack", "telegram", "zammad"]

CONVERSATION_PROVIDER_POST_REQUEST_KIND_VALUES: set[ConversationProviderPostRequestKind] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_conversation_provider_post_request_kind(value: str) -> ConversationProviderPostRequestKind:
    if value in CONVERSATION_PROVIDER_POST_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_PROVIDER_POST_REQUEST_KIND_VALUES!r}")
