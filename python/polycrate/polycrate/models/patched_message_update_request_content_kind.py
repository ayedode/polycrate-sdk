from typing import Literal

PatchedMessageUpdateRequestContentKind = Literal["html", "json", "markdown", "text", "yaml"]

PATCHED_MESSAGE_UPDATE_REQUEST_CONTENT_KIND_VALUES: set[PatchedMessageUpdateRequestContentKind] = {
    "html",
    "json",
    "markdown",
    "text",
    "yaml",
}


def check_patched_message_update_request_content_kind(value: str) -> PatchedMessageUpdateRequestContentKind:
    if value in PATCHED_MESSAGE_UPDATE_REQUEST_CONTENT_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_MESSAGE_UPDATE_REQUEST_CONTENT_KIND_VALUES!r}"
    )
