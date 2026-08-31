from typing import Literal

ApiV1ConversationsMessagesArchiveCreateMetaErrorComponentAttr = Literal["meta"]

API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesArchiveCreateMetaErrorComponentAttr
] = {
    "meta",
}


def check_api_v1_conversations_messages_archive_create_meta_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesArchiveCreateMetaErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
