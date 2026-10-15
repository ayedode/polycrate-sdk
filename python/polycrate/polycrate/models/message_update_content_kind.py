from typing import Literal

MessageUpdateContentKind = Literal["html", "json", "markdown", "text", "yaml"]

MESSAGE_UPDATE_CONTENT_KIND_VALUES: set[MessageUpdateContentKind] = {
    "html",
    "json",
    "markdown",
    "text",
    "yaml",
}


def check_message_update_content_kind(value: str) -> MessageUpdateContentKind:
    if value in MESSAGE_UPDATE_CONTENT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_UPDATE_CONTENT_KIND_VALUES!r}")
