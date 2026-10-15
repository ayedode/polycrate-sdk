from typing import Literal

MessagePostRequestContentKind = Literal["html", "json", "markdown", "text", "yaml"]

MESSAGE_POST_REQUEST_CONTENT_KIND_VALUES: set[MessagePostRequestContentKind] = {
    "html",
    "json",
    "markdown",
    "text",
    "yaml",
}


def check_message_post_request_content_kind(value: str) -> MessagePostRequestContentKind:
    if value in MESSAGE_POST_REQUEST_CONTENT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_POST_REQUEST_CONTENT_KIND_VALUES!r}")
