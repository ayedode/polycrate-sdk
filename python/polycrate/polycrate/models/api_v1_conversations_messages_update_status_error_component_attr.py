from typing import Literal

ApiV1ConversationsMessagesUpdateStatusErrorComponentAttr = Literal["status"]

API_V1_CONVERSATIONS_MESSAGES_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesUpdateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_conversations_messages_update_status_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesUpdateStatusErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
