from typing import Literal

MessageListContentKind = Literal["html", "json", "markdown", "text", "yaml"]

MESSAGE_LIST_CONTENT_KIND_VALUES: set[MessageListContentKind] = {
    "html",
    "json",
    "markdown",
    "text",
    "yaml",
}


def check_message_list_content_kind(value: str) -> MessageListContentKind:
    if value in MESSAGE_LIST_CONTENT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_LIST_CONTENT_KIND_VALUES!r}")
