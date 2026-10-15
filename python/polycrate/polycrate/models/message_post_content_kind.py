from typing import Literal

MessagePostContentKind = Literal["html", "json", "markdown", "text", "yaml"]

MESSAGE_POST_CONTENT_KIND_VALUES: set[MessagePostContentKind] = {
    "html",
    "json",
    "markdown",
    "text",
    "yaml",
}


def check_message_post_content_kind(value: str) -> MessagePostContentKind:
    if value in MESSAGE_POST_CONTENT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_POST_CONTENT_KIND_VALUES!r}")
