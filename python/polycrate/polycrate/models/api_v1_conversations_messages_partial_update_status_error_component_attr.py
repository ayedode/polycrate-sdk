from typing import Literal

ApiV1ConversationsMessagesPartialUpdateStatusErrorComponentAttr = Literal["status"]

API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesPartialUpdateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_conversations_messages_partial_update_status_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesPartialUpdateStatusErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
