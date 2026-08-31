from typing import Literal

ApiV1ConversationsMessagesPartialUpdateContentKindErrorComponentAttr = Literal["content_kind"]

API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_CONTENT_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesPartialUpdateContentKindErrorComponentAttr
] = {
    "content_kind",
}


def check_api_v1_conversations_messages_partial_update_content_kind_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesPartialUpdateContentKindErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_CONTENT_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_CONTENT_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
