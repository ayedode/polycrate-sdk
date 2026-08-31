from typing import Literal

ApiV1ConversationsConversationsListStatusErrorComponentAttr = Literal["status"]

API_V1_CONVERSATIONS_CONVERSATIONS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsConversationsListStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_conversations_conversations_list_status_error_component_attr(
    value: str,
) -> ApiV1ConversationsConversationsListStatusErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
