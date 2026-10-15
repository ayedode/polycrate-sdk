from typing import Literal

MessageRequestKind = Literal["discord", "email", "generic", "msteams", "slack", "telegram", "zammad"]

MESSAGE_REQUEST_KIND_VALUES: set[MessageRequestKind] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_message_request_kind(value: str) -> MessageRequestKind:
    if value in MESSAGE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_REQUEST_KIND_VALUES!r}")
