from typing import Literal

ApiV1ConversationsMessagesUpdateMetaErrorComponentCode = Literal["invalid", "null"]

API_V1_CONVERSATIONS_MESSAGES_UPDATE_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsMessagesUpdateMetaErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_conversations_messages_update_meta_error_component_code(
    value: str,
) -> ApiV1ConversationsMessagesUpdateMetaErrorComponentCode:
    if value in API_V1_CONVERSATIONS_MESSAGES_UPDATE_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_UPDATE_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
