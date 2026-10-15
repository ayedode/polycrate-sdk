from typing import Literal

ConversationPostRequestKind = Literal["discord", "email", "generic", "msteams", "slack", "telegram", "zammad"]

CONVERSATION_POST_REQUEST_KIND_VALUES: set[ConversationPostRequestKind] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_conversation_post_request_kind(value: str) -> ConversationPostRequestKind:
    if value in CONVERSATION_POST_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_POST_REQUEST_KIND_VALUES!r}")
