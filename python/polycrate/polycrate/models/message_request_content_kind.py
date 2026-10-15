from typing import Literal

MessageRequestContentKind = Literal["html", "json", "markdown", "text", "yaml"]

MESSAGE_REQUEST_CONTENT_KIND_VALUES: set[MessageRequestContentKind] = {
    "html",
    "json",
    "markdown",
    "text",
    "yaml",
}


def check_message_request_content_kind(value: str) -> MessageRequestContentKind:
    if value in MESSAGE_REQUEST_CONTENT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_REQUEST_CONTENT_KIND_VALUES!r}")
