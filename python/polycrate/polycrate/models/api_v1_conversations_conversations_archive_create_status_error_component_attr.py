from typing import Literal

ApiV1ConversationsConversationsArchiveCreateStatusErrorComponentAttr = Literal["status"]

API_V1_CONVERSATIONS_CONVERSATIONS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsConversationsArchiveCreateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_conversations_conversations_archive_create_status_error_component_attr(
    value: str,
) -> ApiV1ConversationsConversationsArchiveCreateStatusErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
