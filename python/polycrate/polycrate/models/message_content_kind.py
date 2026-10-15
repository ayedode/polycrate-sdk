from typing import Literal

MessageContentKind = Literal["html", "json", "markdown", "text", "yaml"]

MESSAGE_CONTENT_KIND_VALUES: set[MessageContentKind] = {
    "html",
    "json",
    "markdown",
    "text",
    "yaml",
}


def check_message_content_kind(value: str) -> MessageContentKind:
    if value in MESSAGE_CONTENT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_CONTENT_KIND_VALUES!r}")
