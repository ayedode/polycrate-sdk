from typing import Literal

ConversationKind = Literal["discord", "email", "generic", "msteams", "slack", "telegram", "zammad"]

CONVERSATION_KIND_VALUES: set[ConversationKind] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_conversation_kind(value: str) -> ConversationKind:
    if value in CONVERSATION_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_KIND_VALUES!r}")
