from typing import Literal

ApiV1ConversationsMessagesCreateStatusErrorComponentAttr = Literal["status"]

API_V1_CONVERSATIONS_MESSAGES_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesCreateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_conversations_messages_create_status_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesCreateStatusErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
