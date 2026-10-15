from typing import Literal

ConversationPostKind = Literal["discord", "email", "generic", "msteams", "slack", "telegram", "zammad"]

CONVERSATION_POST_KIND_VALUES: set[ConversationPostKind] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_conversation_post_kind(value: str) -> ConversationPostKind:
    if value in CONVERSATION_POST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_POST_KIND_VALUES!r}")
