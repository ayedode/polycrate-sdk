from typing import Literal

MessageKind = Literal["discord", "email", "generic", "msteams", "slack", "telegram", "zammad"]

MESSAGE_KIND_VALUES: set[MessageKind] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_message_kind(value: str) -> MessageKind:
    if value in MESSAGE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_KIND_VALUES!r}")
