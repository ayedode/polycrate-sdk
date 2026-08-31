from typing import Literal

ApiV1ConversationsMessagesArchiveCreateContentKindErrorComponentAttr = Literal["content_kind"]

API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_CONTENT_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesArchiveCreateContentKindErrorComponentAttr
] = {
    "content_kind",
}


def check_api_v1_conversations_messages_archive_create_content_kind_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesArchiveCreateContentKindErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_CONTENT_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_CONTENT_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
