from typing import Literal

MessagePostKind = Literal["discord", "email", "generic", "msteams", "slack", "telegram", "zammad"]

MESSAGE_POST_KIND_VALUES: set[MessagePostKind] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_message_post_kind(value: str) -> MessagePostKind:
    if value in MESSAGE_POST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_POST_KIND_VALUES!r}")
