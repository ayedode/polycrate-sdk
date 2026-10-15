from typing import Literal

MessageUpdateRequestContentKind = Literal["html", "json", "markdown", "text", "yaml"]

MESSAGE_UPDATE_REQUEST_CONTENT_KIND_VALUES: set[MessageUpdateRequestContentKind] = {
    "html",
    "json",
    "markdown",
    "text",
    "yaml",
}


def check_message_update_request_content_kind(value: str) -> MessageUpdateRequestContentKind:
    if value in MESSAGE_UPDATE_REQUEST_CONTENT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_UPDATE_REQUEST_CONTENT_KIND_VALUES!r}")
