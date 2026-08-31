from typing import Literal

ConversationKindEnum = Literal["discord", "email", "generic", "msteams", "slack", "telegram", "zammad"]

CONVERSATION_KIND_ENUM_VALUES: set[ConversationKindEnum] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_conversation_kind_enum(value: str) -> ConversationKindEnum:
    if value in CONVERSATION_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_KIND_ENUM_VALUES!r}")
