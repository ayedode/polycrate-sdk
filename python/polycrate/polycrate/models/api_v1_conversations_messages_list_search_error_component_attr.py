from typing import Literal

ApiV1ConversationsMessagesListSearchErrorComponentAttr = Literal["search"]

API_V1_CONVERSATIONS_MESSAGES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_conversations_messages_list_search_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesListSearchErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
