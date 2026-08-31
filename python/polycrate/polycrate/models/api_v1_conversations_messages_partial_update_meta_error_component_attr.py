from typing import Literal

ApiV1ConversationsMessagesPartialUpdateMetaErrorComponentAttr = Literal["meta"]

API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesPartialUpdateMetaErrorComponentAttr
] = {
    "meta",
}


def check_api_v1_conversations_messages_partial_update_meta_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesPartialUpdateMetaErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
