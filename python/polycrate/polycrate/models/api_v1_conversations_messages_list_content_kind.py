from typing import Literal

ApiV1ConversationsMessagesListContentKind = Literal["html", "json", "markdown", "text", "yaml"]

API_V1_CONVERSATIONS_MESSAGES_LIST_CONTENT_KIND_VALUES: set[ApiV1ConversationsMessagesListContentKind] = {
    "html",
    "json",
    "markdown",
    "text",
    "yaml",
}


def check_api_v1_conversations_messages_list_content_kind(value: str) -> ApiV1ConversationsMessagesListContentKind:
    if value in API_V1_CONVERSATIONS_MESSAGES_LIST_CONTENT_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_LIST_CONTENT_KIND_VALUES!r}"
    )
