from typing import Literal

ApiV1ConversationsMessagesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_CONVERSATIONS_MESSAGES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_conversations_messages_create_kind_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesCreateKindErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
