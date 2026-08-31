from typing import Literal

ApiV1ConversationsMessagesCreateMetaErrorComponentAttr = Literal["meta"]

API_V1_CONVERSATIONS_MESSAGES_CREATE_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesCreateMetaErrorComponentAttr
] = {
    "meta",
}


def check_api_v1_conversations_messages_create_meta_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesCreateMetaErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_CREATE_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_CREATE_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
