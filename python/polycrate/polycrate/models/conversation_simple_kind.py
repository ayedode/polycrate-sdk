from typing import Literal

ConversationSimpleKind = Literal["discord", "email", "generic", "msteams", "slack", "telegram", "zammad"]

CONVERSATION_SIMPLE_KIND_VALUES: set[ConversationSimpleKind] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_conversation_simple_kind(value: str) -> ConversationSimpleKind:
    if value in CONVERSATION_SIMPLE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_SIMPLE_KIND_VALUES!r}")
