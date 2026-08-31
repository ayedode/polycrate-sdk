from typing import Literal

ApiV1ConversationsMessagesListKindErrorComponentAttr = Literal["kind"]

API_V1_CONVERSATIONS_MESSAGES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_conversations_messages_list_kind_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesListKindErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
