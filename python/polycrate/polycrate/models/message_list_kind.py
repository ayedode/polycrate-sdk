from typing import Literal

MessageListKind = Literal["discord", "email", "generic", "msteams", "slack", "telegram", "zammad"]

MESSAGE_LIST_KIND_VALUES: set[MessageListKind] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_message_list_kind(value: str) -> MessageListKind:
    if value in MESSAGE_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_LIST_KIND_VALUES!r}")
