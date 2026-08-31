from typing import Literal

ApiV1ConversationsMessagesUpdateContentKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONVERSATIONS_MESSAGES_UPDATE_CONTENT_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsMessagesUpdateContentKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_conversations_messages_update_content_kind_error_component_code(
    value: str,
) -> ApiV1ConversationsMessagesUpdateContentKindErrorComponentCode:
    if value in API_V1_CONVERSATIONS_MESSAGES_UPDATE_CONTENT_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_UPDATE_CONTENT_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
