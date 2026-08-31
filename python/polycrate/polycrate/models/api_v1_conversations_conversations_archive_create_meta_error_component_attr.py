from typing import Literal

ApiV1ConversationsConversationsArchiveCreateMetaErrorComponentAttr = Literal["meta"]

API_V1_CONVERSATIONS_CONVERSATIONS_ARCHIVE_CREATE_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsConversationsArchiveCreateMetaErrorComponentAttr
] = {
    "meta",
}


def check_api_v1_conversations_conversations_archive_create_meta_error_component_attr(
    value: str,
) -> ApiV1ConversationsConversationsArchiveCreateMetaErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_ARCHIVE_CREATE_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_ARCHIVE_CREATE_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
