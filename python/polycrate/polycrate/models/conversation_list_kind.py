from typing import Literal

ConversationListKind = Literal["discord", "email", "generic", "msteams", "slack", "telegram", "zammad"]

CONVERSATION_LIST_KIND_VALUES: set[ConversationListKind] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_conversation_list_kind(value: str) -> ConversationListKind:
    if value in CONVERSATION_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_LIST_KIND_VALUES!r}")
