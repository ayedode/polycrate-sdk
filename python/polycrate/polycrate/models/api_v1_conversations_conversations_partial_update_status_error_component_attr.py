from typing import Literal

ApiV1ConversationsConversationsPartialUpdateStatusErrorComponentAttr = Literal["status"]

API_V1_CONVERSATIONS_CONVERSATIONS_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsConversationsPartialUpdateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_conversations_conversations_partial_update_status_error_component_attr(
    value: str,
) -> ApiV1ConversationsConversationsPartialUpdateStatusErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
