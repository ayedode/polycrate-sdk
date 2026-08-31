from typing import Literal

ApiV1ConversationsMessagesPartialUpdateMetaErrorComponentCode = Literal["invalid", "null"]

API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsMessagesPartialUpdateMetaErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_conversations_messages_partial_update_meta_error_component_code(
    value: str,
) -> ApiV1ConversationsMessagesPartialUpdateMetaErrorComponentCode:
    if value in API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
