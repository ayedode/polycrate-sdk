from typing import Literal

ApiV1ConversationsMessagesCreateContentKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONVERSATIONS_MESSAGES_CREATE_CONTENT_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsMessagesCreateContentKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_conversations_messages_create_content_kind_error_component_code(
    value: str,
) -> ApiV1ConversationsMessagesCreateContentKindErrorComponentCode:
    if value in API_V1_CONVERSATIONS_MESSAGES_CREATE_CONTENT_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_CREATE_CONTENT_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
