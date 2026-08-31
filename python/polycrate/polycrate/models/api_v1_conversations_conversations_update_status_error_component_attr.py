from typing import Literal

ApiV1ConversationsConversationsUpdateStatusErrorComponentAttr = Literal["status"]

API_V1_CONVERSATIONS_CONVERSATIONS_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsConversationsUpdateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_conversations_conversations_update_status_error_component_attr(
    value: str,
) -> ApiV1ConversationsConversationsUpdateStatusErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
