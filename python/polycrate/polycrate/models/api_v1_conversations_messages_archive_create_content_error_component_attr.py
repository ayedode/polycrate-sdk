from typing import Literal

ApiV1ConversationsMessagesArchiveCreateContentErrorComponentAttr = Literal["content"]

API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesArchiveCreateContentErrorComponentAttr
] = {
    "content",
}


def check_api_v1_conversations_messages_archive_create_content_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesArchiveCreateContentErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
