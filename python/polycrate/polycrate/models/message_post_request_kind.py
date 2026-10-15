from typing import Literal

MessagePostRequestKind = Literal["discord", "email", "generic", "msteams", "slack", "telegram", "zammad"]

MESSAGE_POST_REQUEST_KIND_VALUES: set[MessagePostRequestKind] = {
    "discord",
    "email",
    "generic",
    "msteams",
    "slack",
    "telegram",
    "zammad",
}


def check_message_post_request_kind(value: str) -> MessagePostRequestKind:
    if value in MESSAGE_POST_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_POST_REQUEST_KIND_VALUES!r}")
