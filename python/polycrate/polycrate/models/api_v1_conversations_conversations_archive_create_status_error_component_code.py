from typing import Literal

ApiV1ConversationsConversationsArchiveCreateStatusErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONVERSATIONS_CONVERSATIONS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsConversationsArchiveCreateStatusErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_conversations_conversations_archive_create_status_error_component_code(
    value: str,
) -> ApiV1ConversationsConversationsArchiveCreateStatusErrorComponentCode:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
