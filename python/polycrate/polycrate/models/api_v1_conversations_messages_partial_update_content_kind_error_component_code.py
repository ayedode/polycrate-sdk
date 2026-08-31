from typing import Literal

ApiV1ConversationsMessagesPartialUpdateContentKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_CONTENT_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsMessagesPartialUpdateContentKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_conversations_messages_partial_update_content_kind_error_component_code(
    value: str,
) -> ApiV1ConversationsMessagesPartialUpdateContentKindErrorComponentCode:
    if value in API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_CONTENT_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_CONTENT_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
