from typing import Literal

ApiV1ConversationsMessagesCreateMetaErrorComponentCode = Literal["invalid", "null"]

API_V1_CONVERSATIONS_MESSAGES_CREATE_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsMessagesCreateMetaErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_conversations_messages_create_meta_error_component_code(
    value: str,
) -> ApiV1ConversationsMessagesCreateMetaErrorComponentCode:
    if value in API_V1_CONVERSATIONS_MESSAGES_CREATE_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_CREATE_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
